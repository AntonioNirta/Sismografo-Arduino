//Code written by Antonio Nirta (www.intrageo.it)

#include <SD.h> //Load SD card library
#include<SPI.h> //Load SPI Library
#include "Wire.h"    // imports the wire library for talking over I2C 

const int MPU = 0x68;   //Default address of I2C for MPU 6050
const int8_t ACCEL_CONFIG = 0x1C; // configurazione dell’accelerometro
const int8_t PWR_MGMT_1   = 0x6B; // risparmio energia 1 indirizzo del registro
const int8_t ACCEL_XOUT_H = 0x3B; // misure accelerometriche

// settaggio del fondo scala accelerometro
const int8_t AFS_SEL_2G   = 0x00;
const int8_t AFS_SEL_4G   = 0x08;
const int8_t AFS_SEL_8G   = 0x10;
const int8_t AFS_SEL_16G  = 0x18;
float to_g_force;

int16_t AcX, AcY, AcZ;

unsigned long time;


int CS_PIN = 4;                   //SD reader/writer PIN
int buzzerPin = 8;               //Buzzer PIN

void setup(){
  Serial.begin(9600); //turn on serial monitor
  Wire.begin();                   // Wire library initialization
  Wire.beginTransmission(MPU);    // Begin transmission to MPU
  Wire.write(0x6B);               // PWR_MGMT_1 register
  Wire.write(0);                  // MPU-6050 to start mode
  Wire.endTransmission(true);
  
  pinMode(buzzerPin, OUTPUT);

  // svegliare l’unità mpu-6050
  Wire.beginTransmission(MPU);
  Wire.write(PWR_MGMT_1);
  Wire.write(0);
  Wire.endTransmission();

  // selezionare il fondo scala dell’accelerometro
  int8_t afs_sel = AFS_SEL_2G;

 // impostazioni dell’accelerometro a fondo scala
   Wire.beginTransmission(MPU);
   Wire.write(ACCEL_CONFIG);
   Wire.write(afs_sel);
   Wire.endTransmission();


  if (SD.exists("example.txt")) {
      SD.remove("example.txt");
  }


 
//Scrivo l'header del file LOG.csv

File file = SD.open("LOG.csv", FILE_WRITE);    
if (file)
  {
    String header = "AcX, AcY, AcZ, Time"; //These will be the headers for your excel file, CHANGE "" to whatevr headers you would like to use
    file.println(header);
    file.close();
    Serial.println(header);
  }
  
}

void loop() {   
  Wire.beginTransmission(MPU);      // Start transfer
  Wire.write(0x3B);                 // register 0x3B (ACCEL_XOUT_H), records data in queue
  Wire.endTransmission(false);      // Maintain connection
  Wire.requestFrom(MPU, 14, true);  // Request data to MPU
  


  //Reads byte by byte
 
  AcX = Wire.read() << 8 | Wire.read(); // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)
  AcY = Wire.read() << 8 | Wire.read(); // 0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
  AcZ = Wire.read() << 8 | Wire.read(); // 0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)

  //Prints values on Serial
  Serial.print(AcX);
  Serial.print(","); 
  Serial.print(AcY);
  Serial.print(","); 
  Serial.println(AcZ);
  delay(20);

  if (AcX > 0) { beep(50); beep(50); }     //sound from AcX
  if (AcY > 250) { beep(50); beep(50); }        //sound from AcY
  if (AcZ > 19000) { beep(50); beep(50); }    //sound from AcZ


//Time
time = millis();

//Scrivo le accelerazioni nel file LOG.csv
File file = SD.open("LOG.csv", FILE_WRITE);
String parametri = String(AcX) + "," + String(AcY) + "," + String(AcZ) + "," + String(time);
    
}

//Instructions for beep buzzer
void beep(unsigned char delayms){
  digitalWrite(buzzerPin,HIGH);
  delay(delayms); // wait for a delayms ms
  digitalWrite(buzzerPin,LOW);
  delay(delayms); // wait for a delayms ms
}




 
