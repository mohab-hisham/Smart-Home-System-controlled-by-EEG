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
Adafruit_MQTT_Subscribe *light1_sub = NULL;
Adafruit_MQTT_Subscribe *light2_sub = NULL;
Adafruit_MQTT_Subscribe *light3_sub = NULL;
Adafruit_MQTT_Subscribe *light4_sub = NULL;
Adafruit_MQTT_Subscribe *wifi_name = NULL;
Adafruit_MQTT_Subscribe *wifi_password = NULL;

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

    if (light1_sub)
  {
    delete light1_sub;
    light1_sub = NULL;
    Serial.println("Deleting old light1 object");
  }

      if (light2_sub)
  {
    delete light2_sub;
    light2_sub = NULL;
    Serial.println("Deleting old light2 object");
  }

    if (light3_sub)
  {
    delete light3_sub;
    light3_sub = NULL;
    Serial.println("Deleting old light3 object");
  }

      if (light4_sub)
  {
    delete light4_sub;
    light4_sub = NULL;
    Serial.println("Deleting old light4 object");
  }
  
  if (wifi_name)
  {
    delete wifi_name;
    wifi_name = NULL;
    Serial.println("Deleting old wifi_name object");
  }
  if (wifi_password)
  {
    delete wifi_password;
    wifi_password = NULL;
    Serial.println("Deleting old wifi_password object");
  }  
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
    serverIp = MDNS.queryHost("raspberrypi"); 
  }
 
  Serial.println("Host address resolved:");
  Serial.println(serverIp.toString());
  strcpy(custom_AIO_SERVER, serverIp.toString().c_str());

  deleteOldInstances();

  mqtt = new Adafruit_MQTT_Client(&client, custom_AIO_SERVER, AIO_SERVERPORT, AIO_USERNAME, AIO_KEY);


    
/****************************** Feeds ***************************************/

  // Notice MQTT paths for AIO follow the form: <username>/feeds/<feedname>
  
  light1_sub = new Adafruit_MQTT_Subscribe(mqtt, AIO_USERNAME "/feeds/light1");
  
  light2_sub = new Adafruit_MQTT_Subscribe(mqtt, AIO_USERNAME "/feeds/light2");

  light3_sub = new Adafruit_MQTT_Subscribe(mqtt, AIO_USERNAME "/feeds/light3");
  
  light4_sub = new Adafruit_MQTT_Subscribe(mqtt, AIO_USERNAME "/feeds/light4");
  
  wifi_name = new Adafruit_MQTT_Subscribe(mqtt, AIO_USERNAME "/wifi/name");
  
  wifi_password = new Adafruit_MQTT_Subscribe(mqtt, AIO_USERNAME "/wifi/password");

  mqtt->subscribe(wifi_name);
  mqtt->subscribe(wifi_password);
  mqtt->subscribe(light1_sub);
  mqtt->subscribe(light2_sub);
  mqtt->subscribe(light3_sub);
  mqtt->subscribe(light4_sub);
}
//Servo myservo;
void setup() {
  Serial.begin(115200);

  delay(10);
  pinMode(Relay1, OUTPUT);
  pinMode(Relay2, OUTPUT);
  pinMode(Relay3, OUTPUT);
  pinMode(Relay4, OUTPUT);
  digitalWrite(Relay1, HIGH);
  digitalWrite(Relay2, HIGH);
  digitalWrite(Relay3, HIGH);
  digitalWrite(Relay4, HIGH);

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
  mqtt->subscribe(wifi_name);
  mqtt->subscribe(wifi_password);
  mqtt->subscribe(light1_sub);
  mqtt->subscribe(light2_sub);
  mqtt->subscribe(light3_sub);
  mqtt->subscribe(light4_sub);
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
    if (subscription == wifi_name) {
      Serial.print(F("Got: "));
      Serial.println((char *)wifi_name->lastread);
      WIFI_NAME = (char *)wifi_name->lastread;
      Serial.println(WIFI_NAME);
      
    }

    if (subscription == wifi_password) {
      Serial.print(F("Got: "));
      Serial.println((char *)wifi_password->lastread);
      WIFI_PASSWORD = (char *)wifi_password->lastread;
      Serial.println(WIFI_PASSWORD);

    }
    if (subscription == light1_sub) {
      Serial.print(F("Got: Light1 "));
      Serial.println((char *)light1_sub->lastread);
      int Light1_State = atoi((char *)light1_sub->lastread);
      if(Light1_State == 0){
        digitalWrite(Relay1, HIGH);
      }
      else{
        digitalWrite(Relay1, LOW);
      }
    }

    if (subscription == light2_sub) {
      Serial.print(F("Got: Light2 "));
      Serial.println((char *)light2_sub->lastread);
      int Light2_State = atoi((char *)light2_sub->lastread);
      if(Light2_State == 0){
        digitalWrite(Relay2, HIGH);
      }
      else{
        digitalWrite(Relay2, LOW);
      }
    }

    if (subscription == light3_sub) {
      Serial.print(F("Got: Light3 "));
      Serial.println((char *)light3_sub->lastread);
      int Light3_State = atoi((char *)light3_sub->lastread);
      if(Light3_State == 0){
        digitalWrite(Relay3, HIGH);
      }
      else{
        digitalWrite(Relay3, LOW);
      }
      
    }

    if (subscription == light4_sub) {
      Serial.print(F("Got: Light4 "));
      Serial.println((char *)light4_sub->lastread);
      int Light4_State = atoi((char *)light4_sub->lastread);
      if(Light4_State == 0){
        digitalWrite(Relay4, HIGH);
      }
      else{
        digitalWrite(Relay4, LOW);
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
