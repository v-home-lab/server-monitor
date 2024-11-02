#include "dht.h"
#define dht_apin A0 // Analog Pin sensor is connected to
 
dht DHT;
 
void setup(){
 
  Serial.begin(9600);
  delay(500);//Delay to let system boot
  Serial.println("Humidity & temperature Sensor starting...\n\n");
  delay(1000);//Wait before accessing Sensor
 
}//end "setup()"
 
void loop(){
  //Start of Program 
 
    DHT.read11(dht_apin);

    float temp_in_f = (DHT.temperature * 9.0 / 5.0) + 32;
    
    Serial.print("Current humidity = ");
    Serial.print(DHT.humidity);
    Serial.print("%  ");
    Serial.print("temperature = ");
    Serial.print(temp_in_f); 
    Serial.println(" F");
    
    delay(5000);//Wait 5 seconds before accessing sensor again.
 
}

