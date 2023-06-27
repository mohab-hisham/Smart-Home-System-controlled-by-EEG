import paho.mqtt.client as mqtt



serverAddress = "raspberrypi.local"
clientName = "PiBot"
mqttClient = mqtt.Client(clientName)

# Flag to indicate subscribe confirmation hasn't been printed yet.
didPrintSubscribeMessage = False

def connectionStatus(client, userdata, flags, rc):
    global serverIsConnected
    global didPrintSubscribeMessage
    if not didPrintSubscribeMessage:
        didPrintSubscribeMessage = True
        print("subscribing")
        mqttClient.subscribe("/feeds/light1")
        mqttClient.subscribe("/feeds/light2")
        mqttClient.subscribe("/feeds/light3")
        mqttClient.subscribe("/feeds/light4")
        mqttClient.subscribe("/calibrate/startCalibrating")
        mqttClient.subscribe("/selectController")
        mqttClient.subscribe("/calibrate/minTH")
        mqttClient.subscribe("/calibrate/maxTH")
        print("subscribed")
        serverIsConnected = True
        

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
            mqttClient.publish("/calibrate/process","calibrating")
        else:
            print("out of calibration")
            mqttClient.publish("/calibrate/process","Done calibrating")
    elif calibratingFlag==1 and message.topic == "/calibrate/minTH":
        lowerTH = float(recivedmess)
    elif calibratingFlag==1 and message.topic == "/calibrate/maxTH":
        upperTH = float(recivedmess)
    elif message.topic == "/selectController":   
        homeOrCar = int(recivedmess)
        if homeOrCar == 1:
            mqttClient.publish("/nowControlling","Home")
        else:
            mqttClient.publish("/nowControlling","Car")

def connectToServer():
    
    mqttClient.on_connect = connectionStatus
    mqttClient.on_message = On_message
    print('Press Ctrl-C in the console to break the while loop.')
    print("server address is:", serverAddress)
    mqttClient.connect(serverAddress)
    
    mqttClient.loop_forever()