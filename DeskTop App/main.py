import time
from PyQt5.QtCore import *

import numpy as np  # Module that simplifies computations on matrices
import matplotlib.pyplot as plt  # Module used for plotting
from pylsl import StreamInlet, resolve_byprop  # Module to receive EEG data
# import utils  # Our own utility functions
import time
from muselsl import stream, list_muses, view
import threading
import asyncio
# import variables
from types import SimpleNamespace
from scipy import signal
import pyautogui as pg

ns = SimpleNamespace()

# Handy little enum to make code more readable


class Band:
    Delta = 0
    Theta = 1
    Alpha = 2
    Beta = 3
    Gamma = 4


# blink length -> to get the time of eye close (make it array to determine blink limit if upper limit is 0 then no upper limit)
#duration after Blink -> to get the open time after Blink (make it array to determine after blink limit if upper limit is 0 then no upper limit)

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



rightSeqArr = Sequence([Blink(length=[0,0.5],durationAfterBlink=[0,1]),Blink(length=[0,0.5],durationAfterBlink=[0,0])],whatToControll="rightSequence")
leftSeqArr = Sequence([Blink(length=[0,0.5],durationAfterBlink=[0,1]),Blink(length=[0,0.5],durationAfterBlink=[0,1]),Blink(length=[0,0.5],durationAfterBlink=[0,0])],whatToControll="leftSequence")
selectSeqArr = Sequence([Blink(length=[0.6,0],durationAfterBlink=[0,0])],whatToControll="selectSequence")
outSeqArr = Sequence([Blink(length=[0,0.5],durationAfterBlink=[0,1]),Blink(length=[0,0.5],durationAfterBlink=[0,1]),Blink(length=[0,0.5],durationAfterBlink=[0,1]),Blink(length=[0,0.5],durationAfterBlink=[0,0])],whatToControll="outSequence")
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
endCommand = 0
endcommand2 = 0
command = ""
finalCommand = ""
startBlinkCount = 0
firstStartBlinkTime = 0
secondStartBlinkTime = 0
thirdBlink = 0
moving = 0
blinkCounter = 0

SeqArray = [rightSeqArr,leftSeqArr,selectSeqArr,outSeqArr]

inputSeqArr = []

openTime = time.time()
closeTime = time.time()
firstClose = 1
openCloseState = 0

################################3
testData = np.array([])
testcounttest = 0
upperTH = 20
lowerTH = -120
setTH = 0
###############################
ns.continueFlag = 0
ns.reconectFlag = 0

inlet = None

fs = 0

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



openCloseTime = 0
closeOpenTime = 0

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
    global homeorroom

    returnValue = 0

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
            if openCloseTime > 1:
                startCommand = 0
                endCommand = 1
                firstClose = 1
                openCloseState = 0
                openCloseTime = 0
                closeOpenTime = 0
                outputSeq = checkSeq(Sequence(inputSeqArr))
                print("choosed Sequence is: ",outputSeq)
                if outputSeq == "rightSequence":
                    returnValue = 1
                        
                elif outputSeq == "leftSequence":
                    returnValue = 2
                        
                elif outputSeq == "outSequence":
                    returnValue = 3
                elif  outputSeq == "selectSequence":
                    returnValue = 4
                else:
                    returnValue = 0
                inputSeqArr = []
                outputSeq = ""
                return returnValue
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
    return returnValue


    
            
    




# def compareSeq(sequence:Sequence,compSeq:Sequence)-> bool:
#     maching = False
#     machingArr = []
#     if int(sequence.SeqLength) == int(compSeq.SeqLength):
#         for i in range(compSeq.SeqLength):
#             if float(compSeq.Seq[i].length[0]) <= float(sequence.Seq[i].length[0]) <= float(compSeq.Seq[i].length[1])\
#                   and float(compSeq.Seq[i].durationAfterBlink[0]) <=float(sequence.Seq[i].durationAfterBlink[0]) <= float(compSeq.Seq[i].durationAfterBlink[1]):
#                 machingArr.append(True)
#             else:
#                 machingArr.append(False)

#             # print(machingArr)
#         for cheq in machingArr:
#             if cheq == True:
#                 maching = True
#             else:
#                 maching = False
#                 break
#         machingArr = []
                
#         if maching == True:
#             maching = False
#             # print("done")
#             return True
#         else:
#             maching = False
#     if maching == False:
#         return False

        
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




############################################################

def filter_delta_theta(eeg_data, fs=256, wind_len=51, lower_delta=0.5, upper_delta=4, lower_beta=14, upper_beta=25, r_or_l=1, plot=0):
    freq_step = fs / wind_len
    delta_band = (int(lower_delta / freq_step), int(upper_delta / freq_step))
    beta_band = (int(lower_beta / freq_step), int(upper_beta / freq_step))

    right_data = np.array(eeg_data)[:, 3] - np.array(eeg_data)[:, 2]
    left_data = np.array(eeg_data)[:, 0] - np.array(eeg_data)[:, 1]
    right_fft = np.fft.rfft(right_data)
    left_fft = np.fft.rfft(left_data)

    r_delta_freq = np.zeros(int(wind_len / 2) + 1, dtype="complex_")
    r_delta_freq[delta_band[0]: delta_band[1] + 1] = right_fft[delta_band[0]: delta_band[1] + 1]

    l_delta_freq = np.zeros(int(wind_len / 2) + 1, dtype="complex_")
    l_delta_freq[delta_band[0]: delta_band[1] + 1] = left_fft[delta_band[0]: delta_band[1] + 1]


    r_delta = np.fft.irfft(r_delta_freq)
    l_delta = np.fft.irfft(l_delta_freq)
    
    return(r_delta,l_delta)




def startEEG():
    global inlet
    global fs

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

    # Get the sampling frequency
    # This is an important value that represents how many EEG data points are
    # collected in a second. This influences our frequency band calculation.
    # for the Muse 2016, this should always be 256
    fs = int(info.nominal_srate())
    
    # view()



    # The try/except structure allows to quit the while loop by aborting the
    # script with <Ctrl-C>
    print('Press Ctrl-C in the console to break the while loop.')
    # time.sleep(5)
    # input("input any key to start calibration")

    # print("blink once in the following 2 seconds")
    # counter1 = 0
    ##########################3
    # firstSequence = 1
    ##########################
    # try:
    # The following loop acquires data, computes band powers, and calculates neurofeedback metrics based on those band powers
    
                
def start_threads():
    thread = threading.Thread(target=startEEG)
    thread.daemon = True
    thread.start()


class CntWorker(QObject):
    eeg_cnt = pyqtSignal(int)
    fin = pyqtSignal()
    

    def getinput(self):
        global lowerTH
        global upperTH
        global inlet
        global fs
        while inlet == None or fs == 0:
            # time.sleep(5)
            # print("waiting")
            pass
        while True:

            """ 3.1 ACQUIRE DATA """
            # Obtain EEG data from the LSL stream
            eeg_data, timestamp = inlet.pull_chunk(
                timeout=1, max_samples=int(SHIFT_LENGTH * fs))

            # Only keep the channel we're interested in
            # ch_data = np.array(eeg_data)[:, INDEX_CHANNEL]

        
            # print(fs)
            rData,lData = filter_delta_theta(eeg_data,fs=fs,wind_len=int(SHIFT_LENGTH * fs))

            
            

            # BlinkHandler(rData,lData,lowerTH,upperTH,True)
            # if firstSequence == 1:
            #     firstSequence = 0
            #     # for i in range(3):
            #     readSeq()   
            # else:
            outValue = readFullinputedSeq(rData,lData,lowerTH,upperTH)
            # print(outValue)
            # outValue = 0
            # time.sleep(5)
            # print(sum(rData))
            # if sum(rData)> 100:
            #     return 1
                # break

            if outValue != 0 and outValue:
                return outValue

    def choose(self):
        # time.sleep(5)
        print("started")
        code = self.getinput()
        # code = int(code)
        # print("In choose")
        # print(code)
        # time.sleep(5)
        self.eeg_cnt.emit(code)
        print("sig is emitted")
        time.sleep(2)
        self.fin.emit()
        print("fin is emitted")


class EEG_Worker(QObject):
    eeg_sig = pyqtSignal()
    fin = pyqtSignal()
    cnt_return = pyqtSignal()
    def navigate(self):
        # time.sleep(5)
        self.eeg_sig.emit()
        time.sleep(5)
        self.cnt_return.emit()
        self.fin.emit()






