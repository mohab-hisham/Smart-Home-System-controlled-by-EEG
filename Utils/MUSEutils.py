import numpy as np  # Module that simplifies computations on matrices

from pylsl import StreamInlet, resolve_byprop  # Module to receive EEG data
# import utils  # Our own utility functions

import threading
import asyncio
from muselsl import stream, list_muses
import time
from types import SimpleNamespace
from Utils.MQTTutils import mqttClient

ns = SimpleNamespace()
streamRetryCounter = 0
muses = []

ns.continueFlag = 0
ns.testenter=0
ns.reconectFlag =0

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
            stream(ns , muses[0]['address'],ppg_enabled=False,acc_enabled=True,gyro_enabled=True)
            # Note: Streaming is synchronous, so code here will not execute until the stream has been closed
            print('Stream has ended')
            #raise RuntimeError('reconecting EEG stream.')
        except:
            streamRetryCounter += 1
            ns.reconectFlag = 0
            # mqttClient.publish("/muse/retrying",streamRetryCounter)
            print("something went wrong")
            if streamRetryCounter == 15:
                print("restarting")
                # mqttClient.publish("/server","Restarting")
                time.sleep(2)
                #os.system("sudo reboot")
            print("retrying")
            
        time.sleep(5)

def startMUSEconnection():
    ServerThread = threading.Thread(target=streamEEG)
    ServerThread.daemon = True
    ServerThread.start()
    while ns.continueFlag == 0:
        pass


def collectEEGsignal():
    EEGinlet = None
    accInlet = None
    gyroInlet = None
    fs = 0

    """ 1. CONNECT TO EEG STREAM """
    
    
        
    print('Looking for an EEG stream...')
    EEGstream = resolve_byprop('type', 'EEG', timeout=2)
    accStreams = resolve_byprop('type', 'ACC', timeout=2)#0:x, 1:y, 2:z
    # Name: Muse-D222 (00:55:da:b5:d2:22) Accelerometer - Nominal Rate: 52 - Channels (3): X,Y,Z	1685755057.94798	53.7735849056604
    gyroStreams = resolve_byprop('type', 'GYRO', timeout=2)#0:x, 1:y, 2:z
    # Name: Muse-D222 (00:55:da:b5:d2:22) Gyroscope - Nominal Rate: 52 - Channels (3): X,Y,Z	1685755371.95998	53.8384845463609
    if len(EEGstream) == 0:
        # continueFlag = 0
        raise RuntimeError('Can\'t find EEG stream.')




    # Set active EEG stream to inlet and apply time correction
    print("Start acquiring data")
    EEGinlet = StreamInlet(EEGstream[0], max_chunklen=12)
    accInlet = StreamInlet(accStreams[0], max_chunklen=1)
    gyroInlet = StreamInlet(gyroStreams[0], max_chunklen=1)
    # eeg_time_correction = EEGinlet.time_correction()

    # Get the stream info and description
    info = EEGinlet.info()
    # description = EEGinlet.desc()

    # Get the sampling frequency
    # This is an important value that represents how many EEG data points are
    # collected in a second. This influences our frequency band calculation.
    # for the Muse 2016, this should always be 256
    fs = int(info.nominal_srate())

    if EEGinlet != None and accInlet != None and gyroInlet != None and fs != 0:
        return EEGinlet,accInlet,gyroInlet, fs
    else:
        collectEEGsignal()

    
# # for some tests              
# if __name__ == '__main__':
#     startMUSEconnection()
#     while ns.continueFlag == 0:
#         pass
#     collectEEGsignal()