#include <WiFi.h>
#include <ESPmDNS.h>
#include "Adafruit_MQTT.h"
#include "Adafruit_MQTT_Client.h"

/************************* Pin Definition *********************************/

//Relays for switching appliances
#define Relay1            19
#define Relay2            18
#define Relay3            5
#define Relay4            17
#define Relay5            33
#define Relay6            25
#define Relay7            26
#define Relay8            27

char custom_AIO_SERVER[20];

/************************* WiFi Access Point *********************************/

#define WLAN_SSID       "POCO X3 NFC"
#define WLAN_PASS       "234567891"

/************************* Adafruit.io Setup *********************************/

//#define AIO_SERVER      "192.168.4.2" //IP address of RPi
//#define AIO_SERVER2      "192.168.4.5" //IP address of RPi
//#define AIO_SERVER3      "192.168.53.172" //IP address of RPi
//#define AIO_SERVER      "192.168.1.6" //IP address of RPi
#define AIO_SERVERPORT  1883                   // use 8883 for SSL
#define AIO_USERNAME    ""
#define AIO_KEY         ""

/************ Global State (you don't need to change this!) ******************/
IPAddress serverIp;
// Create an ESP8266 WiFiClient class to connect to the MQTT server.
WiFiClient client;
// or... use WiFiFlientSecure for SSL
//WiFiClientSecure client;

Adafruit_MQTT_Client *mqtt = NULL;
Adafruit_MQTT_Subscribe *living_light_sub = NULL;
Adafruit_MQTT_Subscribe *room1_TV_sub = NULL;
Adafruit_MQTT_Subscribe *room2_light_sub = NULL;
Adafruit_MQTT_Subscribe *kitchen_light_sub = NULL;
Adafruit_MQTT_Subscribe *corridor_door1_sub = NULL;
Adafruit_MQTT_Subscribe *toilet_light_sub = NULL;
//Adafruit_MQTT_Subscribe *wifi_name = NULL;
//Adafruit_MQTT_Subscribe *wifi_password = NULL;

//// Setup the MQTT client class by passing in the WiFi client and MQTT server and login details.
//Adafruit_MQTT_Client mqtt(&client, AIO_SERVER, AIO_SERVERPORT, AIO_USERNAME, AIO_KEY);
//
///****************************** Feeds ***************************************/
//


char* WIFI_NAME = "";
char* WIFI_PASSWORD = "";
int connection_state = 0;

/************ Necessary declaration for DHT11 ******************/

void deleteOldInstances(void)
{
  // Delete previous instances
  if (mqtt)
  {
    delete mqtt;
    mqtt = NULL;
    Serial.println("Deleting old MQTT object");
  }

    if (living_light_sub)
  {
    delete living_light_sub;
    living_light_sub = NULL;
    Serial.println("Deleting old light1 object");
  }

      if (room1_TV_sub)
  {
    delete room1_TV_sub;
    room1_TV_sub = NULL;
    Serial.println("Deleting old light2 object");
  }

      if (room2_light_sub)
  {
    delete room2_light_sub;
    room2_light_sub = NULL;
    Serial.println("Deleting old room2_light_sub object");
  }

    if (kitchen_light_sub)
  {
    delete kitchen_light_sub;
    kitchen_light_sub = NULL;
    Serial.println("Deleting old light3 object");
  }

      if (corridor_door1_sub)
  {
    delete corridor_door1_sub;
    corridor_door1_sub = NULL;
    Serial.println("Deleting old corridor_door1_sub object");
  }

      if (toilet_light_sub)
  {
    delete toilet_light_sub;
    toilet_light_sub = NULL;
    Serial.println("Deleting old light4 object");
  }
  
//  if (wifi_name)
//  {
//    delete wifi_name;
//    wifi_name = NULL;
//    Serial.println("Deleting old wifi_name object");
//  }
//  if (wifi_password)
//  {
//    delete wifi_password;
//    wifi_password = NULL;
//    Serial.println("Deleting old wifi_password object");
//  }  
}

/*************************** Sketch Code ************************************/

// Bug workaround for Arduino 1.6.6, it seems to need a function declaration
// for some reason (only affects ESP8266, likely an arduino-builder bug).
void MQTT_connect();

void GetServerIP(){
  while(mdns_init()!= ESP_OK){
    delay(1000);
    Serial.println("Starting MDNS...");
  }
 
  Serial.println("MDNS started");
 
  delay(2000);
  serverIp= IPAddress(0,0,0,0);
  while (serverIp.toString() == "0.0.0.0") {
    Serial.println("Resolving host...");
    delay(250);
    serverIp = MDNS.queryHost("DESKTOP-KB0NG3A"); 
  }
 
  Serial.println("Host address resolved:");
  Serial.println(serverIp.toString());
  strcpy(custom_AIO_SERVER, serverIp.toString().c_str());

  deleteOldInstances();

  mqtt = new Adafruit_MQTT_Client(&client, custom_AIO_SERVER, AIO_SERVERPORT, AIO_USERNAME, AIO_KEY);


    
/****************************** Feeds ***************************************/

  // Notice MQTT paths for AIO follow the form: <username>/feeds/<feedname>
  
  living_light_sub = new Adafruit_MQTT_Subscribe(mqtt, AIO_USERNAME "/Living/Light");
  
  room1_TV_sub = new Adafruit_MQTT_Subscribe(mqtt, AIO_USERNAME "/Room 1/TV");

  room2_light_sub = new Adafruit_MQTT_Subscribe(mqtt, AIO_USERNAME "/Room 2/Light");

  kitchen_light_sub = new Adafruit_MQTT_Subscribe(mqtt, AIO_USERNAME "/Kitchen/Light");

  corridor_door1_sub = new Adafruit_MQTT_Subscribe(mqtt, AIO_USERNAME "/Corridor/Door 1");
  
  toilet_light_sub = new Adafruit_MQTT_Subscribe(mqtt, AIO_USERNAME "/Toilet/Light");
  
//  wifi_name = new Adafruit_MQTT_Subscribe(mqtt, AIO_USERNAME "/wifi/name");
//  
//  wifi_password = new Adafruit_MQTT_Subscribe(mqtt, AIO_USERNAME "/wifi/password");

//  mqtt->subscribe(wifi_name);
//  mqtt->subscribe(wifi_password);
  mqtt->subscribe(living_light_sub);
  mqtt->subscribe(room1_TV_sub);
  mqtt->subscribe(room2_light_sub);
  mqtt->subscribe(kitchen_light_sub);
  mqtt->subscribe(corridor_door1_sub);
  mqtt->subscribe(toilet_light_sub);
}
//Servo myservo;
void setup() {
  Serial.begin(115200);

  delay(10);
  pinMode(Relay1, OUTPUT);
  pinMode(Relay2, OUTPUT);
  pinMode(Relay3, OUTPUT);
  pinMode(Relay4, OUTPUT);
  pinMode(Relay5, OUTPUT);
  pinMode(Relay6, OUTPUT);
  pinMode(Relay7, OUTPUT);
  pinMode(Relay8, OUTPUT);
  digitalWrite(Relay1, HIGH);
  digitalWrite(Relay2, HIGH);
  digitalWrite(Relay3, HIGH);
  digitalWrite(Relay4, HIGH);
  digitalWrite(Relay5, LOW);
  digitalWrite(Relay6, LOW);
  digitalWrite(Relay7, LOW);
  digitalWrite(Relay8, LOW);

  Serial.println(F("Adafruit MQTT demo"));

  // Connect to WiFi access point.
  Serial.println(); Serial.println();
  Serial.print("Connecting to ");
  Serial.println(WLAN_SSID);

  WiFi.begin(WLAN_SSID, WLAN_PASS);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println();

  Serial.println("WiFi connected");
  Serial.println("IP address: "); Serial.println(WiFi.localIP());
  delay(1000);
  deleteOldInstances();
  GetServerIP();

  // Setup MQTT subscription for onoff feed.
//  mqtt->subscribe(wifi_name);
//  mqtt->subscribe(wifi_password);
  mqtt->subscribe(living_light_sub);
  mqtt->subscribe(room1_TV_sub);
  mqtt->subscribe(room2_light_sub);
  mqtt->subscribe(kitchen_light_sub);
  mqtt->subscribe(corridor_door1_sub);
  mqtt->subscribe(toilet_light_sub);
}

uint32_t x = 0;

void loop() {
  // Ensure the connection to the MQTT server is alive (this will make the first
  // connection and automatically reconnect when disconnected).  See the MQTT_connect
  // function definition further below.
  MQTT_connect();
  // this is our 'wait for incoming subscription packets' busy subloop
  // try to spend your time here

  Adafruit_MQTT_Subscribe *subscription;
  while ((subscription = mqtt->readSubscription(5000))) {
//    if (subscription == wifi_name) {
//      Serial.print(F("Got: "));
//      Serial.println((char *)wifi_name->lastread);
//      WIFI_NAME = (char *)wifi_name->lastread;
//      Serial.println(WIFI_NAME);
//      
//    }
//
//    if (subscription == wifi_password) {
//      Serial.print(F("Got: "));
//      Serial.println((char *)wifi_password->lastread);
//      WIFI_PASSWORD = (char *)wifi_password->lastread;
//      Serial.println(WIFI_PASSWORD);
//
//    }
    if (subscription == living_light_sub) {
      Serial.print(F("Got: Light1 "));
      Serial.println((char *)living_light_sub->lastread);
      int Light1_State = atoi((char *)living_light_sub->lastread);
      if(Light1_State == 0){
        digitalWrite(Relay1, HIGH);
      }
      else{
        digitalWrite(Relay1, LOW);
      }
    }

    if (subscription == room1_TV_sub) {
      Serial.print(F("Got: Light2 "));
      Serial.println((char *)room1_TV_sub->lastread);
      int Light2_State = atoi((char *)room1_TV_sub->lastread);
      if(Light2_State == 0){
        digitalWrite(Relay5, LOW);
      }
      else{
        digitalWrite(Relay5, HIGH);
      }
    }

    if (subscription == room2_light_sub) {
      Serial.print(F("Got: room2_light_sub "));
      Serial.println((char *)room2_light_sub->lastread);
      int Light1_State = atoi((char *)room2_light_sub->lastread);
      if(Light1_State == 0){
//        digitalWrite(Relay1, HIGH);
//          Serial.println("room2_light_sub 0");
          digitalWrite(Relay4, HIGH);
      }
      else{
        digitalWrite(Relay4, LOW);
//          Serial.println("room2_light_sub 1");
//        digitalWrite(Relay1, LOW);
      }
    }

    if (subscription == kitchen_light_sub) {
      Serial.print(F("Got: Light3 "));
      Serial.println((char *)kitchen_light_sub->lastread);
      int Light3_State = atoi((char *)kitchen_light_sub->lastread);
      if(Light3_State == 0){
        digitalWrite(Relay6, LOW);
      }
      else{
        digitalWrite(Relay6, HIGH);
      }
      
    }

    if (subscription == corridor_door1_sub) {
      Serial.print(F("Got: corridor_door1_sub "));
      Serial.println((char *)corridor_door1_sub->lastread);
      int Light1_State = atoi((char *)corridor_door1_sub->lastread);
      if(Light1_State == 0){
//        Serial.println("corridor_door1_sub 0");
        digitalWrite(Relay7, LOW);

      }
      else{
//        Serial.println("corridor_door1_sub 1");
        digitalWrite(Relay7, HIGH);
      }
    }

    if (subscription == toilet_light_sub) {
      Serial.print(F("Got: Light4 "));
      Serial.println((char *)toilet_light_sub->lastread);
      int Light4_State = atoi((char *)toilet_light_sub->lastread);
      if(Light4_State == 0){
        digitalWrite(Relay8, LOW);
      }
      else{
        digitalWrite(Relay8, HIGH);
      }
    }

  }

  // ping the server to keep the mqtt connection alive
  // NOT required if you are publishing once every KEEPALIVE seconds
//  
//    if(! mqtt.ping()) {
//    mqtt.disconnect();
//    }
  
//  delay(500);
}

// Function to connect and reconnect as necessary to the MQTT server.
// Should be called in the loop function and it will take care if connecting.
void MQTT_connect() {
  int8_t ret;

  // Stop if already connected.
  if (mqtt->connected()) {
    return;
  }

  Serial.print("Connecting to MQTT... ");

  uint8_t retries = 10;
  while ((ret = mqtt->connect()) != 0) { // connect will return 0 for connected
    Serial.println(mqtt->connectErrorString(ret));
    Serial.println("Retrying MQTT connection in 5 seconds...");
    mqtt->disconnect();
    delay(5000);  // wait 5 seconds
    retries--;
    if (retries == 0) {
      // basically die and wait for WDT to reset me
      Serial.println("reached maximum number of retries check that your system is running right then retart !!");
      while(1);
    }
  }
  Serial.println("MQTT Connected!");
}
