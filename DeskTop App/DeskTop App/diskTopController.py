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

# from pythonosc.dispatcher import Dispatcher
# from pythonosc.osc_server import BlockingOSCUDPServer

import threading
import numpy as np
# import tensorflow as tf
from nltk import flatten

import pygame
import pygame_menu
from pygame.locals import *
from pygame_menu.examples import create_example_window
import string
import os

from pynput.keyboard import Key, Controller
from timeit import default_timer as timer

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


######################################################

alpha = beta = delta = theta = gamma = [-1,-1,-1,-1]
all_waves = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
all_samples = []

sample_nr = 0
expected_samples = 30                                           # there are 5 frequencies (alpa...gamma) and 4 sensors, if all 4 sensors are used
                                                                # this should be 5 x 4 = 20, the frequency is 10 Hz. 3 seconds of data with all
                                                                # 4 sensors = 3 * 5 * 4 * 10 = 600. 

confidence_threshold = 0.5                                      # default in Edge Impulse is 0.6
left = right = background = 0

blinks = 0                                                      # amount of blinks
blinked = False                                                 # did you blink?
bl2 = bl3 = False
jaw_clenches = 0
jaw_clenched = False
state = 0
alphabet = []
blink_time = []

start = timer()
secs = 3

IP = "0.0.0.0"                                                  # listening on all IP-addresses
PORT = 8080                                                     # on this port


####################################################

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
    global state
    global blinked ,bl2

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
                    state = 1
                elif outputSeq == "leftSequence":
                    state = -1
                elif outputSeq == "selectSequence":
                    blinked = True
                elif outputSeq == "outSequence":
                    bl2 = True
                else:
                    state = 0
                    # blinked = False
                inputSeqArr = []
                return
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
####################################################
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

def decodeMorse(morseCode):
    try:
        return MORSE_CODE_DICT[morseCode]
    except:
        return None


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
    firstSequence = 1
    ##########################
    # try:
    # The following loop acquires data, computes band powers, and calculates neurofeedback metrics based on those band powers
    while True:

        """ 3.1 ACQUIRE DATA """
        # Obtain EEG data from the LSL stream
        eeg_data, timestamp = inlet.pull_chunk(
            timeout=1, max_samples=int(SHIFT_LENGTH * fs))

        # Only keep the channel we're interested in
        # ch_data = np.array(eeg_data)[:, INDEX_CHANNEL]

    

        rData,lData = filter_delta_theta(eeg_data,fs=fs,wind_len=int(SHIFT_LENGTH * fs))

        
        

        # BlinkHandler(rData,lData,lowerTH,upperTH,True)
        # if firstSequence == 1:
        #     firstSequence = 0
        #     # for i in range(3):
        #     readSeq()   
        # else:
        readFullinputedSeq(rData,lData,lowerTH,upperTH)
                   
def start_threads():
    thread = threading.Thread(target=startEEG)
    thread.daemon = True
    thread.start()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Clears the screen ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def clear_screen():
	screen = pygame.display.set_mode(size)			                    # clearing screen
	pygame.display.update()												# update screen
   	

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Shows a random image ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def show_image():
    global screen, blinked, state, alphabet

    scr_width  = size[0]                                # surface width
    scr_height = size[1]                                # surface height
    MAXHEALTH = 9                                       # 0..9 = 10 bars for the "health bars"
    GREEN = (48, 141, 70)
    WHITE = (200,200,200)
    back_color = (55,55,55)
    HB_X = (scr_width / 2) - 185                        # start position for Health Bars
    HB_HEIGHT = 11                                      # height of health bars


    font = pygame.font.SysFont(None, 60)                # default font

    def clear_area():
        pygame.draw.rect(screen, back_color, (  HB_X, scr_height / 2 + 50, 100 * MAXHEALTH, HB_HEIGHT))

    def drawHealthMeterLeft(currentHealth):
        clear_area()
        for i in range(currentHealth): # draw green health bars
            pygame.draw.rect(screen, GREEN,   (HB_X + (10 * MAXHEALTH) - (i * 10), scr_height / 2 + 50, 20, HB_HEIGHT))
        for i in range(MAXHEALTH): # draw the white outlines
            pygame.draw.rect(screen, WHITE, (HB_X + (10 * MAXHEALTH) - (i * 10), scr_height / 2 + 50, 20, HB_HEIGHT), 1)

    def drawHealthMeterBackground(currentHealth):
        cH = currentHealth
        for i in range(cH): # draw green health bars
            pygame.draw.rect(screen, GREEN, ((scr_width/2) - (5*cH) + (i*10)-10, scr_height / 2 + 50, 20, HB_HEIGHT))
        for i in range(MAXHEALTH): # draw the white outlines
            pygame.draw.rect(screen, WHITE, (HB_X+120 + (10 * MAXHEALTH) - i * 10, scr_height / 2 + 50, 20, HB_HEIGHT), 1)

    def drawHealthMeterRight(currentHealth):
        for i in range(currentHealth): # draw green health bars
            pygame.draw.rect(screen, GREEN, (HB_X+160 + (10 * MAXHEALTH) + i * 10, scr_height / 2 + 50, 20, HB_HEIGHT))
        for i in range(MAXHEALTH): # draw the white outlines
            pygame.draw.rect(screen, WHITE, (HB_X+160 + (10 * MAXHEALTH) + i * 10, scr_height / 2 + 50, 20, HB_HEIGHT), 1)


    def write(txt, x,y, color, size):
        font = pygame.font.SysFont(None, size)
        img = font.render(txt, True, color)
        screen.blit(img, (x, y))

    def write_alphabet(list):
        pygame.draw.rect(screen, back_color, (0, scr_height / 2 + 100, scr_width, 35))      # emptying the background
        i = 0
        for c in list:
            write(c[0], 50 + (i*40), scr_height/2 + 100, WHITE, 60)
            i+=1


    def text_editor():
        global alphabet, text, blinked, state, bl2

        # Drawing selector Rectangle (x, y, width, height, border thickness, corner radius)
        pygame.draw.rect(screen, GREEN, pygame.Rect((scr_width/2)-35, (scr_height/2) + 88, 
            40, 60),  4, 6)
        write_alphabet(alphabet)

        # Text "editor" frame
        pygame.draw.rect(screen, WHITE, pygame.Rect(20, (scr_height/2) + 180, scr_width-40, 170),  1, 6)

        text = ""                                           # put any default text here if you dare :-)
        img = font.render(text, True, WHITE)
        rect = img.get_rect()

        start = timer()                                     # this and below needed for not scrolling the alphabet too fast
        end = start
        blinked = False
        editing = True

        while editing == True:
            # Close window event
            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            editing = False

            drawHealthMeterLeft       (int(left * MAXHEALTH))
            drawHealthMeterBackground (int(background * MAXHEALTH))
            drawHealthMeterRight      (int(right * MAXHEALTH))

            wait = 1                                        # wait how many seconds
            end = timer()

            if (end - start) > wait:
                start = timer()
                if state == -1:
                    alphabet = np.roll(alphabet, 1,0)       # scrolling one direction...
                    write_alphabet(alphabet)
                elif state == 1:                            # ...or the other
                    alphabet = np.roll(alphabet, -1,0)
                    write_alphabet(alphabet)
                state = 0

            if blinked == True:
                state = 0                                   # stops the alphabet when blinking
                blinked = False
                text += alphabet[13][0]                     # choosing the selected character
                if text == 'EDGE':                          # EASTER EGG :-D
                    text += ' IMPULSE :-D'
                img = font.render(text, True, WHITE)
                rect.size=img.get_size()


            pygame.draw.rect(screen, back_color, (0, scr_height / 2 + 180, scr_width-40, 170))      # emptying the background
            pygame.draw.rect(screen, WHITE, pygame.Rect(20, (scr_height/2) + 180, scr_width-40, 170),  1, 6)
            rect = img.get_rect()
            rect.topleft = (40, 580)

            screen.blit(img, rect)
            pygame.display.update()

            if bl2 == True:                             # did you double blink?...
                pygame.draw.rect(screen, back_color, (0,    # then clear the editor area
                    (scr_height/2) + 88, scr_width, scr_height))
                pygame.display.update()
                editing = False                         # and close the editor


    screen = pygame.display.set_mode(size)			    # clearing screen
    pygame.display.update()								# update screen

    images=[]                                           # list used for images found...
    path = 'E:/Graduation_Project/MUSE2/examples codes/Muse-EEG-main/Images/'                                    # ...in this subfolder of the current folder
    
    for image in os.listdir(path):                      # populating the list...
        if image.startswith('0') and image.endswith('.png'):  # ...only files with name 0*.png
            images.append(image)

    img_w_def = 150                                     # default image width, changing this might lead to a cascade effect...

    screen.fill(back_color)                             # surface background color


    def writeLabels():                                  # labels under the health bars
        write("Left",       HB_X +  40, scr_height/2+65, WHITE, 24)
        write("Background", HB_X + 130, scr_height/2+65, WHITE, 24)
        write("Right",      HB_X + 280, scr_height/2+65, WHITE, 24)

    writeLabels()                                       # writing the above labels

    # Drawing selector Rectangle (x, y, width, height, border thickness, corner radius)
    pygame.draw.rect(screen, GREEN, pygame.Rect((scr_width/2)-(img_w_def/2)-15, (scr_height/2)-(img_w_def/2)-25, 
        img_w_def + 20, img_w_def/1.3),  5, 7)

    clock = pygame.time.Clock()                         # clock
    start = timer()
    end = start
    nr_images = len(images)                             # how many images found?
    bl2 = False

    running = True                                      # Prepare loop condition
    while running:                                      # Event loop
        
        if bl2 == True:
            bl2 = False
            running = False

        # Close window event
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

        if blinked == True:
            write("Chosen", 20, 20, WHITE, 60)          # indicates the image was chosen
            state = 0                                   # stops scrolling the images
            if images[3][0:3] == '020':                 # if the keyboard (or whatever) picture was chosen
                text_editor()                           # starts the text editor
            blinked = False
        else:
            write("Chosen", 20, 20, back_color, 60)     # writes over the chosen text


        end = timer()
        if (end - start) > 0.1:
            start = timer()

            images = np.roll(images, state*-1)                                  # yippii! rotating the image carousel
            state = 0
            for i in range(nr_images):
                image = pygame.image.load(path + images[i])	                    # concatenating the folder with image name

                img_width   = image.get_width()                                 # finding image width...
                img_height  = image.get_height()                                # ...and height for scaling purposes

                IMAGE_SIZE = (img_w_def, img_w_def * img_height / img_width)	# setting the size for the image
                image = pygame.transform.scale(image, IMAGE_SIZE)			    # scaling the image
                IMAGE_POSITION = ((i * (img_w_def + 20)) + 10, 290)				# placing the image

                pygame.draw.rect(screen, back_color, (IMAGE_POSITION[0] + 20,
                    IMAGE_POSITION[1]+112, scr_width, 24))

                write(images[i][4:-4],IMAGE_POSITION[0] + 20,                   # writing the rest of the file name...
                    IMAGE_POSITION[1]+112,WHITE,24)                             # ...i.e. image description

                screen.blit(image, IMAGE_POSITION)                              # show the image

                large_image = pygame.image.load(path + images[3])               # enlarging the center image which is #3

                img_width   = large_image.get_width()                           # finding image width...
                img_height  = large_image.get_height()                          # ...and height for scaling purposes

                IMAGE_SIZE = (img_w_def*2.5, img_w_def*img_height/img_width*2.5)# setting the size for the image
                large_image = pygame.transform.scale(large_image, IMAGE_SIZE)	# scaling the image
                IMAGE_POSITION = ((scr_width/2) - IMAGE_SIZE[0] / 2, 20)        # placing the image

                screen.blit(large_image, IMAGE_POSITION)                        # show the image
        

        drawHealthMeterLeft       (int(left * MAXHEALTH))
        drawHealthMeterBackground (int(background * MAXHEALTH))
        drawHealthMeterRight      (int(right * MAXHEALTH))

        # Part of event loop
        pygame.display.flip()

        #time.sleep(.8)
        clock.tick(120)


def init_menu():
    global keyboard, alphabet, surface, background_image

    keyboard = Controller()

    surface = create_example_window('Mind Reader', size)


    menu = pygame_menu.Menu(
        height=size[1],
        onclose=pygame_menu.events.EXIT,  # User press ESC button
        theme=pygame_menu.themes.THEME_BLUE,
        title='Mind Reader',
        width=size[0]
    )
    
    chars = list(string.ascii_uppercase)                    # populating an alphabet list
    chars.append(' ')                                       # adding space char

    def createList(r1, r2):
        return list(range(r1, r2+1))

    numbers = createList(65,90)                             # ASCII-codes for A..Z...
    numbers.append(32)                                      # ...and space char

    alphabet = list(zip(chars,numbers))                     # creating a list of chars and ASCII-codes

    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(surface)


def start_the_game() -> None:
    pygame.init()
    pygame.font.init()
    clear_screen()
    show_image()
if __name__ == "__main__":
    size = (1200, 768)	
    start_threads()
    # startEEG()
    init_menu()

        