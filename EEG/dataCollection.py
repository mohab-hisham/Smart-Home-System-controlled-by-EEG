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


def filter_alpha_beta(eeg_data, fs=256, wind_len=51, lower_alpha=0.5, upper_alpha=4, lower_beta=14, upper_beta=25, r_or_l=1, plot=0):
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
        if LE_ch_STD < 80 and LF_ch_STD < 80 and RF_ch_STD < 80 and RE_ch_STD < 80:
            ch_Quality = True
            

        #i think we will check the std of every channel from it we can check the quality
        if ch_Quality:
            print("good signal quality!!")
            return




if __name__ == "__main__":


    
    
    """ 1. CONNECT TO EEG STREAM """
    
    
        
    print('Looking for an EEG stream...')
    streams = resolve_byprop('type', 'EEG', timeout=2) #maxchunklenght = 12
    # Name: Muse-D222 (00:55:da:b5:d2:22) EEG - Nominal Rate: 256 - Channels (5): TP9,AF7,AF8,TP10,Right AUX	1685755616.05209	262.686567164179
    # streams = resolve_byprop('type', 'Accelerometer', timeout=2)#0:x, 1:y, 2:z #maxchunklenght = 1
    # Name: Muse-D222 (00:55:da:b5:d2:22) Accelerometer - Nominal Rate: 52 - Channels (3): X,Y,Z	1685755057.94798	53.7735849056604
    # streams = resolve_byprop('type', 'Gyroscope', timeout=2)#0:x, 1:y, 2:z #maxchunklenght = 1
    # Name: Muse-D222 (00:55:da:b5:d2:22) Gyroscope - Nominal Rate: 52 - Channels (3): X,Y,Z	1685755371.95998	53.8384845463609
    # streams = resolve_byprop('type', 'PPG', timeout=2)#PPG1:0, PPG2:1, PPG3:2 #maxchunklenght = 6
    # Name: Muse-D222 (00:55:da:b5:d2:22) PPG - Nominal Rate: 64 - Channels (3): PPG1,PPG2,PPG3	1685755453.57998	63.8297872340426


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

    # Get the sampling frequency
    # This is an important value that represents how many EEG data points are
    # collected in a second. This influences our frequency band calculation.
    # for the Muse 2016, this should always be 256
    fs = int(info.nominal_srate())
    
    
    # view()

    """ 2. INITIALIZE BUFFERS """

    # Initialize raw EEG data buffer
    #eeg_buffer = np.zeros((int(fs * BUFFER_LENGTH), 1))
    #filter_state = None  # for use with the notch filter

    # Compute the number of epochs in "buffer_length"
    #n_win_test = int(np.floor((BUFFER_LENGTH - EPOCH_LENGTH) /
    #                          SHIFT_LENGTH + 1))

    # Initialize the band power buffer (for plotting)
    # bands will be ordered: [delta, theta, alpha, beta]
    #band_buffer = np.zeros((n_win_test, 4))

    """ 3. GET DATA """

    # The try/except structure allows to quit the while loop by aborting the
    # script with <Ctrl-C>
    print('Press Ctrl-C in the console to break the while loop.')
    # CheckSignalQuality(inlet)
    
    # calbCount = 0
    # input("input any key to start calibration")

    # The following loop acquires data, computes band powers, and calculates neurofeedback metrics based on those band powers
    while True:


        """ 3.1 ACQUIRE DATA """
        # Obtain EEG data from the LSL stream
        eeg_data, timestamp = inlet.pull_chunk(
            timeout=1, max_samples=int(SHIFT_LENGTH*fs))

        # Only keep the channel we're interested in
        
        ch_data = np.array(eeg_data)[:, 2]
        print(ch_data)
        
            
        
        # rData,lData = filter_alpha_beta(eeg_data,fs=fs,wind_len=int(SHIFT_LENGTH * fs))
        # print(rData,lData)

        #print(calibratingFlag,type(calibratingFlag))
        
                
                

    
