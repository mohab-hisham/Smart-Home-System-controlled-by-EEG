import numpy as np  # Module that simplifies computations on matrices
import matplotlib.pyplot as plt  # Module used for plotting
from pylsl import StreamInlet, resolve_byprop  # Module to receive EEG data
# import utils  # Our own utility functions
import os
import threading
import asyncio
from muselsl import stream, list_muses
import time
from types import SimpleNamespace
from scipy import signal
from pandas import *
import pyautogui as pg
from Utils.MUSEutils import MUSEns,startMUSEconnection
import tensorflow as tf
# from MQTTutils import MQTTns


########### classes ############################

# Handy little enum to make code more readable
class Band:
    Delta = 0
    Theta = 1
    Alpha = 2
    Beta = 3
    Gamma = 4

# blink length -> to get the time of eye close (make it array to determine blink limit if upper limit is 0 then no upper limit)
# duration after Blink -> to get the open time after Blink (make it array to determine after blink limit if upper limit is 0 then no upper limit)
class Blink:
    def __init__(self , length:float = [0,0.2] , durationAfterBlink:float = [0,0]) -> None:
        try:
            if length[1] == 0:
                length[1] = 1000
        except:
            pass
        self.length = length
        try:
            if durationAfterBlink[1] == 0:
                durationAfterBlink[1] = 1000
        except:
            pass
        self.durationAfterBlink = durationAfterBlink # 0 if no limit after blink else there is limit 
        

    def printBlink(self):
        print("blink length: ", self.length, "duration after Blink: ",self.durationAfterBlink)
    
    def blinkType(self):
        if self.length[0] < 0.2:
            return "short BL"
        else:
            return "long BL"
    
    def durationAfterBlinkType(self):
        if self.durationAfterBlink[0] < 1:
            return "short DAB"
        else:
            return "long DAB"

class Sequence:
    def __init__(self,seqArr,whatToControll = None) -> None:
        self.SeqLength = int(np.array(seqArr).shape[0])
        self.controles = whatToControll
        self.Seq = seqArr
    def printSeq(self):
        print("seq length: ", self.SeqLength)
        print("what it's controlls: ", self.controles)
        for choosedSeq in self.Seq:
            choosedSeq.printBlink()


EEGns = SimpleNamespace()
# the four devices to be controled
relay1State = 0
relay2State = 0
relay3State = 0
relay4State = 0

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
BlinkMorseCode = ""
finalCommand = ""
startBlinkCount = 0
firstStartBlinkTime = 0
secondStartBlinkTime = 0
moving = 0
streamRetryCounter = 0
blinkCounter = 0
testcounttest = 0
testData = np.array([])
setTH = 0
EEGns.calibratingFlag = 1
EEGns.lowerTH = -140
EEGns.upperTH = 40
serverIsConnected = False

EEGns.signalQuality = False

muses = []

homeOrCar = 1

# modular sequence variables
StartSeq = Sequence([Blink(length=[0,0.2],durationAfterBlink=[0,0.5]),Blink(length=[0,0.2],durationAfterBlink=[0,0])],whatToControll="startSequence")
EndSeq = Sequence([Blink(length=[0,0.2],durationAfterBlink=[0,0.5]),Blink(length=[0,0.2],durationAfterBlink=[0,0.5]),Blink(length=[0,0.2],durationAfterBlink=[0,0])],whatToControll="endSequence")
# SeqArray = [Sequence([Blink(length=[0,1],durationAfterBlink=[0,0]),Blink(length=[0,1],durationAfterBlink=[0,0])],whatToControll="home")]
rightSeq = Sequence([Blink(length=[0,0.2],durationAfterBlink=[0,1]),Blink(length=[0,0.2],durationAfterBlink=[0,0])],whatToControll="rightSequence")
leftSeq = Sequence([Blink(length=[0,0.2],durationAfterBlink=[0,1]),Blink(length=[0,0.2],durationAfterBlink=[0,1]),Blink(length=[0,0.2],durationAfterBlink=[0,0])],whatToControll="leftSequence")
selectSeq = Sequence([Blink(length=[0.6,2],durationAfterBlink=[0,0])],whatToControll="selectSequence")
outSeq = Sequence([Blink(length=[0,0.2],durationAfterBlink=[0,1]),Blink(length=[0,0.2],durationAfterBlink=[0,1]),Blink(length=[0,0.2],durationAfterBlink=[0,1]),Blink(length=[0,0.2],durationAfterBlink=[0,0])],whatToControll="outSequence")
blinkNavSeqArray = [rightSeq,leftSeq,selectSeq,outSeq]
tabOneSeq = Sequence([Blink(length=[0,0.2],durationAfterBlink=[0,1]),Blink(length=[0,0.2],durationAfterBlink=[0,0])],whatToControll="tabOne") # ..
tabTwoSeq = Sequence([Blink(length=[0,0.2],durationAfterBlink=[0,1]),Blink(length=[0.2,1],durationAfterBlink=[0,0])],whatToControll="tabTwo") # .-
tabThreeSeq = Sequence([Blink(length=[0.2,1],durationAfterBlink=[0,1]),Blink(length=[0,0.2],durationAfterBlink=[0,0])],whatToControll="tabThree") # -.
tabFourSeq = Sequence([Blink(length=[0.2,1],durationAfterBlink=[0,1]),Blink(length=[0.2,1],durationAfterBlink=[0,0])],whatToControll="tabFour") # --
tabFiveSeq = Sequence([Blink(length=[0,0.2],durationAfterBlink=[0,1]),Blink(length=[0,0.2],durationAfterBlink=[0,1]),Blink(length=[0,0.2],durationAfterBlink=[0,0])],whatToControll="tabFive") #...
tabSixSeq = Sequence([Blink(length=[0,0.2],durationAfterBlink=[0,1]),Blink(length=[0,0.2],durationAfterBlink=[0,1]),Blink(length=[0.2,1],durationAfterBlink=[0,0])],whatToControll="tabSix") # ..-
tabSevenSeq = Sequence([Blink(length=[0,0.2],durationAfterBlink=[0,1]),Blink(length=[0.2,1],durationAfterBlink=[0,1]),Blink(length=[0,0.2],durationAfterBlink=[0,0])],whatToControll="tabSeven") # .-.
tabEightSeq = Sequence([Blink(length=[0,0.2],durationAfterBlink=[0,1]),Blink(length=[0.2,1],durationAfterBlink=[0,1]),Blink(length=[0.2,1],durationAfterBlink=[0,0])],whatToControll="tabEight") # .--
tabNineSeq = Sequence([Blink(length=[0.2,1],durationAfterBlink=[0,1]),Blink(length=[0,0.2],durationAfterBlink=[0,1]),Blink(length=[0,0.2],durationAfterBlink=[0,0])],whatToControll="tabNine") # -..
tabTenSeq = Sequence([Blink(length=[0.2,1],durationAfterBlink=[0,1]),Blink(length=[0,0.2],durationAfterBlink=[0,1]),Blink(length=[0.2,1],durationAfterBlink=[0,0])],whatToControll="tabTen") # -.-
tabSelectSeqArr = [tabOneSeq,tabTwoSeq,tabThreeSeq,tabFourSeq,tabFiveSeq,tabSixSeq,tabSevenSeq,tabEightSeq,tabNineSeq,tabTenSeq]
roomSelectSeqArr = [tabOneSeq,tabTwoSeq,tabThreeSeq,tabFourSeq,tabFiveSeq]
falseFallSeq = Sequence([Blink(length=[0,0.2],durationAfterBlink=[0,1]),Blink(length=[0.2,1],durationAfterBlink=[0,0])],whatToControll="falseFall") # .-
falseFallSeqArr = [falseFallSeq]
SeqArray = [rightSeq,leftSeq,selectSeq,outSeq]
inputSeqArr = []
openTime = time.time()
closeTime = time.time()
firstClose = 1
openCloseState = 0
openCloseTime = 0
closeOpenTime = 0
endCommand = 0

# concentration variables 
consbuffer = []   
databuff = 0

# Dictionary representing the morse code chart
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
                    '-.--.':'(', '-.--.-':')', '......':'save',
                    '..-..':'clr'}


########### check signal quality ###############

def CheckSignalQuality():
    #check deviation of every channel to determine if it's right fit or not
    while True:
        ch_Quality = False
        
        eegData, timestamp = MUSEns.EEGinlet.pull_chunk(
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
        if LE_ch_STD < 25 and LF_ch_STD < 25 and RF_ch_STD < 25 and RE_ch_STD < 25:
            ch_Quality = True
            

        #i think we will check the std of every channel from it we can check the quality
        if ch_Quality:
            print("good signal quality!!")
            EEGns.signalQuality = True
            return
        

########### data colection and filtration ######

def filter_dataFreq(eeg_data, fs=256, wind_len=10, lower_freq=0.5, upper_freq=4):
    freq_step = fs / wind_len
    alpha_band = (int(lower_freq / freq_step), int(upper_freq / freq_step))
    
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

def filter_PPGdataFreq(PPG_data, fs=62, wind_len=60, lower_freq=0.5, upper_freq=4):
    freq_step = fs / wind_len
    alpha_band = (int(lower_freq / freq_step), int(upper_freq / freq_step))
    
    PPG2_data = np.array(PPG_data)[:, 1] 
    PPG3_data = np.array(PPG_data)[:, 2] 
    PPG2_fft = np.fft.rfft(PPG2_data)
    PPG3_fft = np.fft.rfft(PPG3_data)

    PPG2_alpha_freq = np.zeros(int(wind_len / 2) + 1, dtype="complex_")
    PPG2_alpha_freq[alpha_band[0]: alpha_band[1] + 1] = PPG2_fft[alpha_band[0]: alpha_band[1] + 1]

    PPG3_alpha_freq = np.zeros(int(wind_len / 2) + 1, dtype="complex_")
    PPG3_alpha_freq[alpha_band[0]: alpha_band[1] + 1] = PPG3_fft[alpha_band[0]: alpha_band[1] + 1]

    PPG2_alpha = np.fft.irfft(PPG2_alpha_freq)
    PPG3_alpha = np.fft.irfft(PPG3_alpha_freq)

    return(PPG2_alpha,PPG3_alpha)
########### calibration functions ##############

def calibrate():
    rtestData = []
    ltestData = []
    # global calibratingFlag
    calbStartTime = time.time()
    
    rlowerarr = []
    rupperarr = []
    llowerarr = []
    lupperarr = []
    EEGns.calibratingFlag = 1
    while (time.time() - calbStartTime) < 5:
        if EEGns.calibratingFlag == 0:
            return
        eegData, timestamp = MUSEns.EEGinlet.pull_chunk(
                timeout=1, max_samples=int(255))
        rdata, ldata = filter_dataFreq(eegData,wind_len=255)
        rtestData= np.append(rtestData, rdata)
        ltestData= np.append(ltestData, ldata)
        
        # print("counter = ", testcounttest)
        # mqttClient.publish("/calibrate/counter",testcounttest)
        # setTH = 0
        
    
        
    print("done calibrating")
    # mqttClient.publish("/calibrate","done calibrating")
    rupperPeaks, _ = signal.find_peaks(rtestData,width=25)
    rlowerPeaks, _ = signal.find_peaks(-rtestData,width=25)
    lupperPeaks, _ = signal.find_peaks(ltestData,width=25)
    llowerPeaks, _ = signal.find_peaks(-ltestData,width=25)
    for i in range(rupperPeaks.size-1):
        for j in range(rlowerPeaks.size):
            if rupperPeaks[i]<rlowerPeaks[j]<rupperPeaks[i+1]:
                if np.std(rtestData[rupperPeaks[i]:rlowerPeaks[j]]) < 200:
                    if -100< rtestData[rlowerPeaks[j]] < -160:
                        rlowerarr.append(rtestData[rlowerPeaks[j]])
                    if 10 < rtestData[rupperPeaks[i]] < 60:
                        rupperarr.append(rtestData[rupperPeaks[i]])
                break
            elif rupperPeaks[i+1]<rlowerPeaks[j]:
                break
    for i in range(lupperPeaks.size-1):
        for j in range(llowerPeaks.size):
            if lupperPeaks[i]<llowerPeaks[j]<lupperPeaks[i+1]:
                if np.std(ltestData[lupperPeaks[i]:llowerPeaks[j]]) < 200:
                    if -100< ltestData[llowerPeaks[j]] < -160:
                        llowerarr.append(ltestData[llowerPeaks[j]])
                    if 10 < ltestData[lupperPeaks[i]] < 60:
                        lupperarr.append(ltestData[lupperPeaks[i]])
                break
            elif lupperPeaks[i+1]<llowerPeaks[j]:
                break
    try:
        rtestLowerTH = np.min(rlowerarr)
        rtestUpperTH = np.mean(rupperarr)
        ltestLowerTH = np.min(llowerarr)
        ltestUpperTH = np.mean(lupperarr)
        calbLowerTH = -140
        calbUpperTH = 40

        if rtestLowerTH < ltestLowerTH:
            calbLowerTH = ltestLowerTH
        else:
            calbLowerTH = rtestLowerTH
        if rtestUpperTH > ltestUpperTH:
            calbUpperTH = ltestUpperTH
        else:
            calbUpperTH = rtestUpperTH
        # mqttClient.publish("/calibrate/minTH",calbLowerTH)
        # mqttClient.publish("/calibrate/maxTH",calbUpperTH)
        print("min= ",calbLowerTH)
        print("max= ",calbUpperTH)
        print(np.max(rtestData),np.min(rtestData))
        print("avr= ",np.mean(rtestData))
        
        
        # setTH = 1
        EEGns.calibratingFlag = 0
        # testData = np.array([])
        EEGns.lowerTH = calbLowerTH
        EEGns.upperTH = calbUpperTH
        print(EEGns.lowerTH,EEGns.upperTH )
    except:
        print("retrying")
        calibrate()
    # return calbLowerTH, calbUpperTH

########### concentration functions ############ not finished

def concentrationLevel(EEGData):
    global databuff
    global consbuffer
    if databuff < 100:
        ch_data = np.array(EEGData)[:, INDEX_CHANNEL] # right forehead
        consbuffer.append(ch_data)
        databuff += 1
    else: 
         
        freqStep = 256/1000
        consFFt = abs(np.fft.rfft(consbuffer))
        maxfft = np.array(consFFt[1:300]).argmax()
        print("max FFT",maxfft)
        betalevel = sum(consFFt[int(14/freqStep):int(300/freqStep)])
        alphalevel = sum(consFFt[int(1/freqStep):int(4/freqStep)])
        print("beta level: ", betalevel)
        print("alpha level: ", alphalevel)
        if betalevel > alphalevel:
            print("concentrated")

        else:
            print("relaxed")
        levelOfConcentration = betalevel-alphalevel
        #get the concentration level from the live raw eeg data
        print(levelOfConcentration)
        databuff = 0
        consbuffer = []  


########### Blink detection functions ##########

def getBlinklength(EEGData,windowLength = 10):
    global blinkState
    global blinkCounter
    global timerStart
    global timerEnd
    global blinkLength
    global homeOrCar
    blinkLength = -1
    rightData, leftData = filter_dataFreq(EEGData,wind_len=windowLength) 
    if (min(rightData) < EEGns.lowerTH) and (min(leftData) < EEGns.lowerTH) and blinkState == 0:
        blinkCounter = blinkCounter + 1
        print("close eye")
        # mqttClient.publish("/EEGDetector/BlinkState","eye closed")
        # print('Delta: ', smooth_band_powers[Band.Delta], ' Theta: ', smooth_band_powers[Band.Theta])
        timerStart = time.time()
        blinkState = 1
    if (300 > max(rightData) > EEGns.upperTH) and (300 > max(leftData) > EEGns.upperTH) and blinkState == 1:
        print("opend eye")
        # mqttClient.publish("/EEGDetector/BlinkState","eye opened")
        # mqttClient.publish("/EEGDetector/BlinkCount",blinkCounter)
        print(blinkCounter)
        # print('Delta: ', smooth_band_powers[Band.Delta], ' Theta: ', smooth_band_powers[Band.Theta])
        timerEnd = time.time()
        blinkLength = timerEnd - timerStart
        print(blinkLength)
        # mqttClient.publish("/EEGDetector/BlinkLength",blinkLength)
        timerStart = 0
        timerEnd = 0
        blinkState = 0
    return blinkLength

########### modular sequence functions #########

def SeqSort(arr):
    n = np.array(arr).shape[0]
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j].SeqLength < arr[j+1].SeqLength:
                arr[j], arr[j+1] = arr[j+1], arr[j]

########### enter modified sequences ########### need modification

def readSeq():
    global SeqArray
    addedSeq = []
    test = True
    while test:
        SeqChar = input("input the type of first char(*,/)")
        if SeqChar == '/':
            newSeq = Sequence(addedSeq,input("what do you want to controll?"))
            SeqArray.append(newSeq)
            addedSeq = []
            SeqSort(SeqArray)
            # newSeq.printSeq()
            for element in SeqArray:
                element.printSeq()
                print("\n \n")
            test = False
        else:
            addedSeq.append(getBlinkData(SeqChar))

def getBlinkData(inputChar):
    BlinkLenght = []
    BlinkDurationAfterBlink = []
    if inputChar == '*':
        
        BlinkLenght.append(float(input("Blink lower time: ")))
        BlinkLenght.append(float(input("Blink upper time: ")))
        BlinkDurationAfterBlink.append(float(input("min duration after Blink: ")))
        BlinkDurationAfterBlink.append(float(input("max duration after Blink: ")))
         
   
    addedBlink = Blink(BlinkLenght,BlinkDurationAfterBlink)
    return addedBlink

########### construct sequence from blinks #####
def readInputedSeq(ns, windowLength=10,homeOrRoom = True,eyeNav = 0):
    outSeqValue = 0
    startTime = time.time()
    while True:
        if ns.intr_val[0]:
            # ns.intr_val[0]=0
            return -1
        if eyeNav == 2:
            AccX, AccY, AccZ,_,_,_ = getGyroAccData(windowLength)
        else:
            eeg_data, timestamp = MUSEns.EEGinlet.pull_chunk(
                timeout=3, max_samples=int(windowLength))
        if eyeNav == 1:
            getL_R_eyeMovement(ns=ns,eegData=eeg_data)
        elif eyeNav == 2:
            # AccX, AccY, AccZ,_,_,_ = getGyroAccData()
            outSeqValue = gyroController(ns = ns,accX = AccX, accY = AccY, accZ = AccZ,currentTime=startTime)
        else:
            outSeqValue = readFullinputedSeq(ns = ns,EEGData=eeg_data,windowLength=windowLength,homeOrRoom=homeOrRoom)

        if outSeqValue != 0:
            return outSeqValue


def readFullinputedSeq(ns,EEGData,windowLength = 10,startSeq = False,endSeq = False, controllMethod = "tabSelect",homeOrRoom = True):
    global inputSeqArr
    global openTime 
    global closeTime 
    global firstClose 
    global openCloseState
    global openCloseTime
    global closeOpenTime
    global startCommand 
    global endCommand
    global SeqArray
    global tabSelectSeqArr
    global blinkNavSeqArray
    global roomSelectSeqArr
    returnValue = 0
    compSeqArr = tabSelectSeqArr
    mesageController = ns.type_of_blink_msg

    if controllMethod == "tabSelect":
        if homeOrRoom:
            compSeqArr = tabSelectSeqArr
            mesageController = ns.type_of_blink_msg
        else:
            compSeqArr = roomSelectSeqArr
            # mesageController = ns.
            # print("in room")
    elif controllMethod == "blinkNavigator":
        compSeqArr = blinkNavSeqArray
    elif controllMethod == "falseFallDetection":
        compSeqArr = falseFallSeqArr
    try:
        rightData, leftData = filter_dataFreq(EEGData, wind_len=windowLength) 
        if (min(rightData) < EEGns.lowerTH ) and (min(leftData) < EEGns.lowerTH ) and openCloseState == 0: #close
            print("eye closed")
            openCloseState = 1
            if firstClose == 1:
                closeTime = time.time()
                firstClose = 0
            else:
                closeTime = time.time()
                openCloseTime = closeTime-openTime
                # inputSeqArr.append(Blink(openCloseTime,BlinkType="eyeOpen"))
                # print("added a Blink!")
                
                inputSeqArr[-1].durationAfterBlink = [openCloseTime]
                if mesageController != None:
                    mesageController.emit(inputSeqArr[-1].durationAfterBlinkType())
                Sequence(inputSeqArr).printSeq()
                # print("eyeOpen: ", openCloseTime)
        elif (300 > max(rightData) > EEGns.upperTH) and (300 > max(leftData) > EEGns.upperTH) and openCloseState == 1: #open
            print("eye opend")
            openCloseState = 0
            openTime = time.time()
            closeOpenTime = openTime-closeTime
            inputSeqArr.append(Blink(length=[closeOpenTime]))
            if mesageController != None:
                mesageController.emit(inputSeqArr[-1].blinkType())
            Sequence(inputSeqArr).printSeq()
        # return returnValue
    
        if startSeq == True:
            if int(np.array(inputSeqArr).shape[0]) >= StartSeq.SeqLength and startCommand == 0:
                
                if compareSeq(Sequence(inputSeqArr[-StartSeq.SeqLength:]),StartSeq):
                    startCommand = 1
                    firstClose = 1
                    endCommand = 0
                    inputSeqArr = []
                    
                    print("started the command")
        if endSeq == True:
            if int(np.array(inputSeqArr).shape[0]) >= EndSeq.SeqLength and endCommand == 0 and startCommand == 1:
                if compareSeq(Sequence(inputSeqArr[-EndSeq.SeqLength:]),EndSeq):
                    print("ended the command")
                    startCommand = 0
                    endCommand = 1
                    firstClose = 1
                    openCloseState = 0
                    openCloseTime = 0
                    closeOpenTime = 0
                    for i in range(EndSeq.SeqLength):
                        inputSeqArr.pop()
                    Sequence(inputSeqArr).printSeq()
                    returnCommand = checkSeq(Sequence(inputSeqArr),compSeqArr)
                    print("choosed Sequence is: ",returnCommand)
                    inputSeqArr = []
            return applyCommand(mesageController,returnCommand,controllMethod)
            
        else:
            if openCloseTime > 1:
                startCommand = 0
                endCommand = 1
                firstClose = 1
                openCloseState = 0
                openCloseTime = 0
                closeOpenTime = 0
                outputSeq = checkSeq(Sequence(inputSeqArr),compSeqArr)
                print("choosed Sequence is: ",outputSeq)
                returnValue = applyCommand(mesageController,outputSeq,controllMethod)
                inputSeqArr = []
                # outputSeq = ""
            return returnValue
    except:
        return 0
         
            
def applyCommand(mesageController,command,controlMethod):
    if controlMethod == "tabSelect":
        if command == "tabOne":
            return 1
        elif command == "tabTwo":
            return 2
        elif command == "tabThree":
            return 3
        elif command == "tabFour":
            return 4
        elif command == "tabFive":
            return 5
        elif command == "tabSix":
            return 6
        elif command == "tabSeven":
            return 7
        elif command == "tabEight":
            return 8
        elif command == "tabNine":
            return 9
        elif command == "tabTen":
            return 10
        else:
            if mesageController != None:
                mesageController.emit("Error: Unknown sequence is entered, Try again!!!! ")
            return 0
    elif controlMethod == "blinkNavigator":
        if command == "rightSequence":
            pg.typewrite(["right"])
                    
        elif command == "leftSequence":
            pg.typewrite(["left"])
                
        elif command == "outSequence":
            # pg.typewrite(["right"])
            pass
        elif  command == "selectSequence":
            pg.typewrite(["space"])
        else:
            if mesageController != None:
                mesageController.emit("Error: Unknown sequence is entered, Try again!!!! ")
            return 0
        return 0
    elif controlMethod == "falseFallDetection":
        if command == "falseFall":
            return 1
        else:
            if mesageController != None:
                mesageController.emit("Real Fall Detected, Calling Help!!! ")
            return 0
    
        
    

########### check inputed sequence functions ###

def compareSeq(sequence:Sequence,compSeq:Sequence)-> bool:
    maching = False
    machingArr = []
    if int(sequence.SeqLength) == int(compSeq.SeqLength):
        for i in range(compSeq.SeqLength):
            if float(compSeq.Seq[i].length[0]) <= float(sequence.Seq[i].length[0]) <= float(compSeq.Seq[i].length[1])\
                  and float(compSeq.Seq[i].durationAfterBlink[0]) <=float(sequence.Seq[i].durationAfterBlink[0]) <= float(compSeq.Seq[i].durationAfterBlink[1]):
                machingArr.append(True)
            else:
                machingArr.append(False)

            # print(machingArr)
        for cheq in machingArr:
            if cheq == True:
                maching = True
            else:
                maching = False
                break
        machingArr = []
                
        if maching == True:
            maching = False
            # print("done")
            return True
        else:
            maching = False
    if maching == False:
        return False

def checkSeq(sequence:Sequence , selectedSeqArr):
    # global SeqArray
    maching = False
    machingArr = []
    for contSeq in selectedSeqArr:
        if int(sequence.SeqLength) == int(contSeq.SeqLength):
            for i in range(contSeq.SeqLength):
                if contSeq.Seq[i].length[0] <= sequence.Seq[i].length[0] <= contSeq.Seq[i].length[1] \
                    and contSeq.Seq[i].durationAfterBlink[0] <=sequence.Seq[i].durationAfterBlink[0] <= contSeq.Seq[i].durationAfterBlink[1]:
                    machingArr.append(True)
                else:
                    machingArr.append(False)

            print(machingArr)
            for cheq in machingArr:
                if cheq == True:
                    maching = True
                else:
                    maching = False
                    break
            machingArr = []
                    
            if maching == True:
                maching = False
                print("done")
                return contSeq.controles
            else:
                maching = False
    if maching == False:
        return 'no match!'

############### L R eye movement ##################
def TFModelInit():
    path = "E:/Graduation_Project/"
    lite_file = "model.tflite"
    EEGns.fulleegData = []
    ####################### INITIALIZE TF Lite #########################
    # Load TFLite model and allocate tensors.
    EEGns.interpreter = tf.lite.Interpreter(model_path=path + lite_file)

    # Get input and output tensors.
    EEGns.input_details = EEGns.interpreter.get_input_details()
    EEGns.output_details = EEGns.interpreter.get_output_details()

    # Allocate tensors
    EEGns.interpreter.allocate_tensors()
    
def getL_R_eyeMovement(ns,eegData):
    mesageController = ns.eye_state
    EEGns.fulleegData = np.vstack([EEGns.fulleegData, np.array(eegData)[:,1:-2]]) if len(EEGns.fulleegData) else np.array(eegData)[:,1:-2]
   
    print(EEGns.fulleegData.shape)
    

    EEGns.fulleegData = np.float32(EEGns.fulleegData)
    
    EEGns.interpreter.set_tensor(EEGns.input_details[0]['index'], [EEGns.fulleegData])

    # run the inference
    EEGns.interpreter.invoke()

    # output_details[0]['index'] = the index which provides the input
    output_data = EEGns.interpreter.get_tensor(EEGns.output_details[0]['index'])

    print(output_data)

    if int(np.array(output_data[0]).argmax()) == 0:
        mesageController.emit("left")
        pg.typewrite(["left"])
        print("look Left")
    elif int(np.array(output_data[0]).argmax()) == 1:
        print("look center")
    elif int(np.array(output_data[0]).argmax()) == 2:
        mesageController.emit("right")
        pg.typewrite(["right"])
        print("look right")

    EEGns.fulleegData = []

########### MORSE code functions ############### need modification

def readMorseCode(ns):
    global startCommand
    global BlinkMorseCode
    morseBlinkLength = -1
    startCommand = 1
    BlinkMorseCode = ""
    ns.type_of_blink_msg.emit("Helllllloooooo")
    while True:

        if ns.intr_val[0]:
            ns.selected_item_code_msg.emit(ns.intr_val[1])
            ns.intr_val = [0, 0]
            break
        # if end signal is sent break from this loop
        eegData, timestamp = MUSEns.EEGinlet.pull_chunk(
                timeout=1, max_samples=int(10))
        # rdata, ldata = filter_dataFreq(eegData)
        morseBlinkLength = getBlinklength(eegData,windowLength=10)
        # if morseBlinkLength >= 1 :
        #     paragraph += " "
        if morseBlinkLength > 0.6:
            print("Very Long Blink")
            startCommand = 0
            morseBlinkLength = -1
            letter = decodeMorse(BlinkMorseCode)
            print(BlinkMorseCode)
            print(letter)
            if letter == 'save':
                ns.selected_item_code_msg.emit(5)
                
            elif letter == 'clr':
                ns.selected_item_code_msg.emit(1)
            elif letter != None:
                ns.morse_statment_msg.emit(letter)
                ns.selected_item_code_msg.emit(2)
                print("after emitting letter")
            else:
                print("in Error")
                ns.type_of_blink_msg.emit("Error")
                ns.selected_item_code_msg.emit(3)
            break
        else:
            if startCommand == 1:
                if 0.2 > morseBlinkLength >= 0:
                    BlinkMorseCode = BlinkMorseCode + '.'
                    morseBlinkLength = -1
                    print("short Blink")
                    ns.type_of_blink_msg.emit(BlinkMorseCode)
                elif 0.6 > morseBlinkLength >= 0.2:
                    BlinkMorseCode = BlinkMorseCode + '-'
                    morseBlinkLength = -1
                    print("long Blink")
                    ns.type_of_blink_msg.emit(BlinkMorseCode)

    

def decodeMorse(morseCode):
    try:
        # mqttClient.publish("/Morse/char",MORSE_CODE_DICT[morseCode])
        return MORSE_CODE_DICT[morseCode]
    except:
        return None

############ Gyro Acc functions ###################################
def getGyroAccData(windowLenght = 10):
    acc_data, accTimestamp = MUSEns.ACCinlet.pull_chunk(
            timeout=1, max_samples=int(windowLenght))
        
    gyro_data, gyroTimestamp = MUSEns.GYROinlet.pull_chunk(
        timeout=1, max_samples=int(windowLenght))
    
    accelerationX = np.mean(np.array(acc_data)[:,0]) #* np.pi
    accelerationY = np.mean(np.array(acc_data)[:,1]) #* np.pi
    accelerationZ = np.mean(np.array(acc_data)[:,2]) #* np.pi
    gyroscpeX = np.mean(np.array(gyro_data)[:,0]) * np.pi
    gyroscpeY = np.mean(np.array(gyro_data)[:,1]) * np.pi
    gyroscpeZ = np.mean(np.array(gyro_data)[:,2]) * np.pi
    return accelerationX,accelerationY,accelerationZ,gyroscpeX,gyroscpeY,gyroscpeZ

def gyroController(ns,accX,accY,accZ,currentTime):
    mesageController = ns.eye_state
    returnVal = 0
    if accY > 0.35 and accX < 0.05:
        mesageController.emit("tab 3")
        returnVal = 3
        print("tab 3") # x: -0.001 , y: 0.4
    elif accY < -0.2 and accX < 0:
        mesageController.emit("tab 1")
        returnVal = 1
        print("tab 1") # x: -0.03 , y: -0.25
    elif accY > 0.2 and accX > 0.1:
        mesageController.emit("tab 6")
        returnVal = 6
        print("tab 6") # x: 0.22 , y: 0.38
    elif accY < -0.2 and accX > 0.1:
        mesageController.emit("tab 4")
        returnVal = 4
        print("tab 4") # x: 0.13 , y: -0.25
    elif -0.2 < accY < 0.2 and accX < 0:
        mesageController.emit("tab 2")
        returnVal = 2
        print("tab 2") # x: -0.001 , y: 0.10
    else:
        mesageController.emit("tab 5")
        returnVal = 5
        print("tab 5") # x: 0.15 , y: 0.15
    print("")
    if time.time()-currentTime > 5:
        return returnVal
    return 0
################### fall detection Handler ############################
def handelFalls(accX,accY,accZ,gyroX,gyroY,gyroZ):
    #if fall is detected 
    #give user five seconds to do the false fall sequence to terminate it
    falseFallFlage = 0
    calbStartTime = time.time()
    while (time.time() - calbStartTime) < 10:
        eeg_data, timestamp = MUSEns.EEGinlet.pull_chunk(
                timeout=0.5, max_samples=int(10))

        # print(eeg_data)
        falseFallFlage = readFullinputedSeq(eeg_data,controllMethod="falseFallDetection")
        if falseFallFlage == 1:
            print("false fall")
            break
    if falseFallFlage == 0:
        print("fall detected!!!")   
        # send message to the one who in charge of the user

################### heart rate ############################
def heartRate():
    # currentTime = time.time()
    # PPGBuffer = []
    # PPG3Buffer = []
    # PPG2 = []
    # PPG3 = []
    # while (time.time() - currentTime) < 5:
    ppg_data, ppgTimestamp = MUSEns.PPGinlet.pull_chunk(
            timeout=5, max_samples=int(300)) 

    print(np.array(ppg_data).shape)
    PPG2, PPG3 = filter_PPGdataFreq(ppg_data,wind_len=300)
    PPG2_peaks, _ = signal.find_peaks(PPG2,width=10)
    PPG3_peaks, _ = signal.find_peaks(PPG3,width=10)
    print(np.array(PPG2_peaks).shape[0],np.array(PPG3_peaks).shape[0])

    heartRateValue = int(np.max([np.array(PPG2_peaks).shape[0] , np.array(PPG3_peaks).shape[0]])) * 12
    return heartRateValue

# if __name__ == '__main__':
#     print(MORSE_CODE_DICT['-.'])
#     startMUSEconnection()
#     HR = 0
#     while True:
#         HR = heartRate()
#         print(HR)