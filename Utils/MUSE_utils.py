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
from server_utils import mqttClient

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

ns = SimpleNamespace()




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

# modular sequence variables
StartSeqArr = Sequence([Blink(length=[0,0.5],durationAfterBlink=[0,0.5]),Blink(length=[0,0.5],durationAfterBlink=[0,0])],whatToControll="startSequence")
EndSeqArr = Sequence([Blink(length=[0,0.5],durationAfterBlink=[0,0.5]),Blink(length=[0,0.5],durationAfterBlink=[0,0.5]),Blink(length=[0,0.5],durationAfterBlink=[0,0])],whatToControll="endSequence")
SeqArray = [Sequence([Blink(length=[0,1],durationAfterBlink=[0,0]),Blink(length=[0,1],durationAfterBlink=[0,0])],whatToControll="home")]
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
                    '-.--.':'(', '-.--.-':')'}

########### MUSE2 connection functions #########
def streamEEG():
    global streamRetryCounter
    global mqttClient
    global muses
    #asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    # loop.run_forever()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    #loop.run_until_complete(streamEEG())
    #muses = list_muses()
    while True:
        
        if not muses:
            muses = list_muses()
        #mqttClient.publish("/auto/working2","yaaay")
        
        try:
            print("entered stream")
            ns.reconectFlag = 0
            ns.continueFlag = 0
            stream(ns , muses[0]['address'])
            # Note: Streaming is synchronous, so code here will not execute until the stream has been closed
            print('Stream has ended')
            #raise RuntimeError('reconecting EEG stream.')
        except:
            streamRetryCounter += 1
            ns.reconectFlag = 0
            mqttClient.publish("/muse/retrying",streamRetryCounter)
            print("something went wrong")
            if streamRetryCounter == 15:
                print("restarting")
                mqttClient.publish("/server","Restarting")
                time.sleep(2)
                #os.system("sudo reboot")
            print("retrying")
            
        time.sleep(5)

########### check signal quality ###############

def CheckSignalQuality(inputInlet:StreamInlet):
    #check deviation of every channel to determine if it's right fit or not
    while True:
        ch_Quality = False
        
        eegData, timestamp = inputInlet.pull_chunk(
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
        

########### data colection and filtration ######

def filter_dataFreq(eeg_data, fs=256, wind_len=51, lower_freq=0.5, upper_freq=4):
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

########### calibration functions ##############

def calibrate(inputInlet:StreamInlet):
    global testData
    global calibratingFlag
    calbStartTime = time.time
    
    lowerarr = []
    upperarr = []
    calibratingFlag = 1
    while time.time - calbStartTime < 5:
        if calibratingFlag == 0:
            return
        eegData, timestamp = inputInlet.pull_chunk(
                timeout=1, max_samples=int(255))
        rdata, ldata = filter_dataFreq(eegData,wind_len=255)
        testData= np.append(testData, rdata)
        
        print("counter = ", testcounttest)
        # mqttClient.publish("/calibrate/counter",testcounttest)
        # setTH = 0
        
    
        
    print("done calibrating")
    # mqttClient.publish("/calibrate","done calibrating")
    upperPeaks, _ = signal.find_peaks(testData,width=45)
    lowerPeaks, _ = signal.find_peaks(-testData,width=45)
    for i in range(upperPeaks.size-1):
        for j in range(lowerPeaks.size):
            if upperPeaks[i]<lowerPeaks[j]<upperPeaks[i+1]:
                if np.std(testData[upperPeaks[i]:lowerPeaks[j]]) < 150:
                    lowerarr.append(testData[lowerPeaks[j]])
                    upperarr.append(testData[upperPeaks[i]])
                break
            elif upperPeaks[i+1]<lowerPeaks[j]:
                break
    calbLowerTH = np.min(lowerarr)
    calbUpperTH = np.mean(upperarr)-30
    # mqttClient.publish("/calibrate/minTH",calbLowerTH)
    # mqttClient.publish("/calibrate/maxTH",calbUpperTH)
    print("min= ",calbLowerTH)
    print("max= ",calbUpperTH)
    print(np.max(testData),np.min(testData))
    print("avr= ",np.mean(testData))
    
    
    # setTH = 1
    calibratingFlag = 0
    testData = np.array([])
    return calbLowerTH, calbUpperTH

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

def readFullinputedSeq(rightData,leftData,lowerlimit,upperlimit):
    global inputSeqArr
    global openTime 
    global closeTime 
    global firstClose 
    global openCloseState
    global openCloseTime
    global closeOpenTime
    global startCommand 
    global endCommand

    if (min(rightData) < lowerlimit ) and (min(leftData) < lowerlimit ) and openCloseState == 0: #close
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
            Sequence(inputSeqArr).printSeq()
            # print("eyeOpen: ", openCloseTime)
    elif (300 > max(rightData) > upperlimit) and (300 > max(leftData) > upperlimit) and openCloseState == 1: #open
        print("eye opend")
        openCloseState = 0
        openTime = time.time()
        closeOpenTime = openTime-closeTime
        inputSeqArr.append(Blink(length=[closeOpenTime]))
        Sequence(inputSeqArr).printSeq()


    if int(np.array(inputSeqArr).shape[0]) >= StartSeqArr.SeqLength and startCommand == 0:
        
        if compareSeq(Sequence(inputSeqArr[-StartSeqArr.SeqLength:]),StartSeqArr):
            startCommand = 1
            firstClose = 1
            endCommand = 0
            inputSeqArr = []
            
            print("started the command")
    elif int(np.array(inputSeqArr).shape[0]) >= EndSeqArr.SeqLength and endCommand == 0 and startCommand == 1:
        if compareSeq(Sequence(inputSeqArr[-EndSeqArr.SeqLength:]),EndSeqArr):
            print("ended the command")
            startCommand = 0
            endCommand = 1
            firstClose = 1
            openCloseState = 0
            openCloseTime = 0
            closeOpenTime = 0
            for i in range(EndSeqArr.SeqLength):
                inputSeqArr.pop()
            Sequence(inputSeqArr).printSeq()
            print("choosed Sequence is: ",checkSeq(Sequence(inputSeqArr)))
            inputSeqArr = []
            
    

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

def checkSeq(sequence:Sequence):
    global SeqArray
    maching = False
    machingArr = []
    for contSeq in SeqArray:
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

########### MORSE code functions ############### need modification

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


########### ACC & GYRO & PPG data collection ### need modification

def readAccGyroPPG():
    AccStream = resolve_byprop('type', 'Accelerometer', timeout=2)
    AccInlet = StreamInlet(AccStream[0], max_chunklen=12)
    GyroStream = resolve_byprop('type', 'Gyroscope', timeout=2)
    GyroInlet = StreamInlet(GyroStream[0], max_chunklen=12)
    PPGStream = resolve_byprop('type', 'PPG', timeout=2)
    PPGInlet = StreamInlet(PPGStream[0], max_chunklen=12)
    while True:
        Acc_data, Acctimestamp = AccInlet.pull_chunk(timeout=1, max_samples=int(52))
        mqttClient.publish("/ACC/X",np.array(Acc_data)[:,0])
        mqttClient.publish("/ACC/Y",np.array(Acc_data)[:,1])
        mqttClient.publish("/ACC/Z",np.array(Acc_data)[:,2])
        Gyro_data, Gyrotimestamp = GyroInlet.pull_chunk(timeout=1, max_samples=int(52))
        mqttClient.publish("/Gyro/X",np.array(Gyro_data)[:,0])
        mqttClient.publish("/Gyro/Y",np.array(Gyro_data)[:,1])
        mqttClient.publish("/Gyro/Z",np.array(Gyro_data)[:,2])
        PPG_data, PPGtimestamp = PPGInlet.pull_chunk(timeout=1, max_samples=int(64))
        mqttClient.publish("/PPG/PPG1",np.array(PPG_data)[:,0])
        mqttClient.publish("/PPG/PPG2",np.array(PPG_data)[:,1])
        mqttClient.publish("/PPG/PPG3",np.array(PPG_data)[:,2])

# def readPPG():
#     PPGStream = resolve_byprop('type', 'PPG', timeout=2)
#     PPGInlet = StreamInlet(PPGStream[0], max_chunklen=12)
#     while True:
#         PPG_data, PPGtimestamp = PPGInlet.pull_chunk(timeout=1, max_samples=int(64))
#         mqttClient.publish("/PPG/PPG1",np.array(PPG_data)[:,0])
#         mqttClient.publish("/PPG/PPG2",np.array(PPG_data)[:,1])
#         mqttClient.publish("/PPG/PPG3",np.array(PPG_data)[:,2])
    
