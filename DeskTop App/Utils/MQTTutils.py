import paho.mqtt.client as mqtt
import threading
from types import SimpleNamespace
# from MUSEutils import MUSEns
# from EEGutils import EEGns
MQTTns = SimpleNamespace()

serverAddress = "raspberrypi.local"
clientName = "PiBot"
MQTTns.mqttClient = mqtt.Client(clientName)

# Flag to indicate subscribe confirmation hasn't been printed yet.
MQTTns.didPrintSubscribeMessage = False

def connectionStatus(client, userdata, flags, rc):
    
    global didPrintSubscribeMessage
    if not didPrintSubscribeMessage:
        MQTTns.didPrintSubscribeMessage = True
        print("subscribing")
        MQTTns.mqttClient.subscribe("/feeds/light1")
        MQTTns.mqttClient.subscribe("/feeds/light2")
        MQTTns.mqttClient.subscribe("/feeds/light3")
        MQTTns.mqttClient.subscribe("/feeds/light4")
        MQTTns.mqttClient.subscribe("/calibrate/startCalibrating")
        MQTTns.mqttClient.subscribe("/selectController")
        MQTTns.mqttClient.subscribe("/calibrate/minTH")
        MQTTns.mqttClient.subscribe("/calibrate/maxTH")
        print("subscribed")
        
        

def On_message(client, userdata, message):
    global calibratingFlag
    global relay1State
    global relay2State
    global relay3State
    global relay4State
    global homeOrCar
    global upperTH
    global lowerTH
    print("message received", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    recivedmess = str(message.payload.decode("utf-8"))
    if message.topic == "/feeds/light1":
        relay1State = int(recivedmess)
    elif message.topic == "/feeds/light2":
        relay2State = int(recivedmess)
    elif message.topic == "/feeds/light3":
        relay3State = int(recivedmess)
    elif message.topic == "/feeds/light4":
        relay4State = int(recivedmess)
    elif message.topic == "/calibrate/startCalibrating":   
        calibratingFlag = int(recivedmess)
        if calibratingFlag == 1:
            print("in calibration mode")
            MQTTns.mqttClient.publish("/calibrate/process","calibrating")
        else:
            print("out of calibration")
            MQTTns.mqttClient.publish("/calibrate/process","Done calibrating")
    elif calibratingFlag==1 and message.topic == "/calibrate/minTH":
        lowerTH = float(recivedmess)
    elif calibratingFlag==1 and message.topic == "/calibrate/maxTH":
        upperTH = float(recivedmess)
    elif message.topic == "/selectController":   
        homeOrCar = int(recivedmess)
        if homeOrCar == 1:
            MQTTns.mqttClient.publish("/nowControlling","Home")
        else:
            MQTTns.mqttClient.publish("/nowControlling","Car")

def connectToServer():
    
    MQTTns.mqttClient.on_connect = connectionStatus
    MQTTns.mqttClient.on_message = On_message
    print('Press Ctrl-C in the console to break the while loop.')
    print("server address is:", serverAddress)
    MQTTns.mqttClient.connect(serverAddress)
    
    MQTTns.mqttClient.loop_forever()

def startMQTTserver():
    ServerThread = threading.Thread(target=connectToServer)
    ServerThread.daemon = True
    ServerThread.start()
    MQTTns.mqttClient.publish("/server/connection","connecting....")
    while not MQTTns.didPrintSubscribeMessage:
        continue
    MQTTns.mqttClient.publish("/server/connection","connected")
    