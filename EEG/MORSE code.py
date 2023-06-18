# -*- coding: utf-8 -*-
"""
Estimate Relaxation from Band Powers

This example shows how to buffer, epoch, and transform EEG data from a single
electrode into values for each of the classic frequencies (e.g. alpha, beta, theta)
Furthermore, it shows how ratios of the band powers can be used to estimate
mental state for neurofeedback.

The neurofeedback protocols described here are inspired by
*Neurofeedback: A Comprehensive Review on System Design, Methodology and Clinical Applications* by Marzbani et. al

Adapted from https://github.com/NeuroTechX/bci-workshop
"""

import numpy as np  # Module that simplifies computations on matrices
import matplotlib.pyplot as plt  # Module used for plotting
from pylsl import StreamInlet, resolve_byprop  # Module to receive EEG data
# import utils  # Our own utility functions
import os
import paho.mqtt.client as mqtt
import threading
import asyncio
from muselsl import stream, list_muses
import time
from types import SimpleNamespace
from scipy import signal

ns = SimpleNamespace()

serverAddress = "raspberrypi.local"
# Handy little enum to make code more readable
clientName = "PiBot"

mqttClient = mqtt.Client(clientName)
# Flag to indicate subscribe confirmation hasn't been printed yet.
didPrintSubscribeMessage = False

blinkCount = 0

relay1State = 0
relay2State = 0
relay3State = 0
relay4State = 0



class Band:
    Delta = 0
    Theta = 1
    Alpha = 2
    Beta = 3


""" EXPERIMENTAL PARAMETERS """
# Modify these to change aspects of the signal processing

# Length of the EEG data buffer (in seconds)
# This buffer will hold last n seconds of data and be used for calculations
BUFFER_LENGTH = 5

# Length of the epochs used to compute the FFT (in seconds)
EPOCH_LENGTH = 1

# Amount of overlap between two consecutive epochs (in seconds)
OVERLAP_LENGTH = 0.96

# Amount to 'shift' the start of each next consecutive epoch
SHIFT_LENGTH = EPOCH_LENGTH - OVERLAP_LENGTH

# Index of the channel(s) (electrodes) to be used
# 0 = left ear, 1 = left forehead, 2 = right forehead, 3 = right ear
INDEX_CHANNEL = [3]

blinkState = 0
counter = 0
timerStart = 0
timerEnd = 0
blinkLength = -1
startCommand = 0
command = ""
finalCommand = ""
startBlinkCount = 0
firstStartBlinkTime = 0
secondStartBlinkTime = 0
moving = 0
streamRetryCounter = 0
blinkCounter = 0
testcounttest = 0
ns.continueFlag = 0
ns.testenter=0
ns.reconectFlag =0
testData = np.array([])
setTH = 0
calibratingFlag = 1
lowerTH = -140
upperTH = 40
serverIsConnected = False

muses = []

homeOrCar = 1


MORSE_CODE_DICT = { '.-':'A', '-...':'B',
                    '-.-.':'C', '-..':'D', '.':'E',
                    '..-.':'F', '--.':'G', '....':'H',
                    '..':'I', '.---':'J', '-.-':'K',
                    '.-..':'L', '--':'M', '-.':'N',
                    '---':'O', '.--.':'P', '--.-':'Q',
                    '.-.':'R', '...':'S', '-':'T',
                    '..-':'U', '...-':'V', '.--':'W',
                    '-..-':'X', '-.--':'Y', '--..':'Z',
                    '.----':'1', '..---':'2', '...--':'3',
                    '....-':'4', '.....':'5', '-....':'6',
                    '--...':'7', '---..':'8', '----.':'9',
                    '-----':'0', '--..--':', ', '.-.-.-':'.',
                    '..--..':'?', '-..-.':'/', '-....-':'-',
                    '-.--.':'(', '-.--.-':')'}




def filter_dataFreq(eeg_data, fs=256, wind_len=51, lower_alpha=0.5, upper_alpha=4, lower_beta=14, upper_beta=25, r_or_l=1, plot=0):
    freq_step = fs / wind_len
    alpha_band = (int(lower_alpha / freq_step), int(upper_alpha / freq_step))
    beta_band = (int(lower_beta / freq_step), int(upper_beta / freq_step))

    right_data = np.array(eeg_data)[:, 3] - np.array(eeg_data)[:, 2]
    left_data = np.array(eeg_data)[:, 0] - np.array(eeg_data)[:, 1]
    right_fft = np.fft.rfft(right_data)
    left_fft = np.fft.rfft(left_data)

    r_alpha_freq = np.zeros(int(wind_len / 2) + 1, dtype="complex_")
    r_alpha_freq[alpha_band[0]: alpha_band[1] + 1] = right_fft[alpha_band[0]: alpha_band[1] + 1]

    l_alpha_freq = np.zeros(int(wind_len / 2) + 1, dtype="complex_")
    l_alpha_freq[alpha_band[0]: alpha_band[1] + 1] = left_fft[alpha_band[0]: alpha_band[1] + 1]

    r_alpha = np.fft.irfft(r_alpha_freq)
    l_alpha = np.fft.irfft(l_alpha_freq)

    return(r_alpha,l_alpha)



def getBlinklength(rightData,leftData,lowerlimit,upperlimit):
    global blinkState
    global blinkCounter
    global timerStart
    global timerEnd
    global blinkLength
    global homeOrCar
    blinkLength = -1
    if (min(rightData) < lowerlimit) and (min(leftData) < lowerlimit) and blinkState == 0:
        blinkCounter = blinkCounter + 1
        print("close eye")
        mqttClient.publish("/EEGDetector/BlinkState","eye closed")
        # print('Delta: ', smooth_band_powers[Band.Delta], ' Theta: ', smooth_band_powers[Band.Theta])
        timerStart = time.time()
        blinkState = 1
    if (300 > max(rightData) > upperlimit) and (300 > max(leftData) > upperlimit) and blinkState == 1:
        print("opend eye")
        mqttClient.publish("/EEGDetector/BlinkState","eye opened")
        mqttClient.publish("/EEGDetector/BlinkCount",blinkCounter)
        print(blinkCounter)
        # print('Delta: ', smooth_band_powers[Band.Delta], ' Theta: ', smooth_band_powers[Band.Theta])
        timerEnd = time.time()
        blinkLength = timerEnd - timerStart
        print(blinkLength)
        mqttClient.publish("/EEGDetector/BlinkLength",blinkLength)
        timerStart = 0
        timerEnd = 0
        blinkState = 0
    return blinkLength
    
    
##### the function that need to work on ##########
def readMorseCode(inputInlet:StreamInlet):
    global lowerTH
    global upperTH
    global startCommand
    global secondStartBlinkTime
    global firstStartBlinkTime
    global startTime
    global command
    morseBlinkLength = -1
    startCommand = 1
    while True:
        # if end signal is sent reak from this loop
        eegData, timestamp = inputInlet.pull_chunk(
                timeout=1, max_samples=int(51))
        rdata, ldata = filter_dataFreq(eegData)
        morseBlinkLength = getBlinklength(rdata,ldata,lowerTH,upperTH)
        if morseBlinkLength > 0.6:
            print("LongBlink")
            startCommand = 0
            morseBlinkLength = -1
            print(command)
            print(decodeMorse(command))
            command = ""
            startCommand = 1
        else:
            if startCommand == 1:
                if 0.2 > morseBlinkLength >= 0:
                    command = command + '.'
                    morseBlinkLength = -1
                    print("short Blink")
                elif 0.6 > morseBlinkLength > 0.2:
                    command = command + '-'
                    morseBlinkLength = -1
                    print("long Blink")

    

def decodeMorse(morseCode):
    try:
        mqttClient.publish("/Morse/char",MORSE_CODE_DICT[morseCode])
        return MORSE_CODE_DICT[morseCode]
    except:
        return None


def CheckSignalQuality(inputInlet:StreamInlet):
    #check deviation of every channel to determine if it's right fit or not
    while True:
        ch_Quality = False
        
        eegData, timestamp = inlet.pull_chunk(
            timeout=1, max_samples=int(255))
        LE_ch_data = np.array(eegData)[:, [0]]
        LF_ch_data = np.array(eegData)[:, [1]]
        RF_ch_data = np.array(eegData)[:, [2]]
        RE_ch_data = np.array(eegData)[:, [3]]
        LE_ch_STD = np.std(LE_ch_data)
        LF_ch_STD = np.std(LF_ch_data)
        RF_ch_STD = np.std(RF_ch_data)
        RE_ch_STD = np.std(RE_ch_data)
        print(LE_ch_STD,LF_ch_STD,RF_ch_STD,RE_ch_STD)
        if LE_ch_STD < 80 and LF_ch_STD < 80 and RF_ch_STD < 80 and RE_ch_STD < 80:
            ch_Quality = True
            

        #i think we will check the std of every channel from it we can check the quality
        if ch_Quality:
            print("good signal quality!!")
            return




if __name__ == "__main__":


    
    
    """ 1. CONNECT TO EEG STREAM """
    
    
        
    print('Looking for an EEG stream...')
    streams = resolve_byprop('type', 'EEG', timeout=2)
    if len(streams) == 0:
        # continueFlag = 0
        raise RuntimeError('Can\'t find EEG stream.')


   

    # Set active EEG stream to inlet and apply time correction
    print("Start acquiring data")
    inlet = StreamInlet(streams[0], max_chunklen=12)
    eeg_time_correction = inlet.time_correction()

    # Get the stream info and description
    info = inlet.info()
    description = info.desc()

    
    fs = int(info.nominal_srate())
    
    
    print('Press Ctrl-C in the console to break the while loop.')
    CheckSignalQuality(inlet)

    readMorseCode(inlet)
    
    

   
        
                
                

    
