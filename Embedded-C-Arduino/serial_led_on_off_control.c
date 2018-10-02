/*
------------------------------------------
		License Information
------------------------------------------
        GNU GENERAL PUBLIC LICENSE
        Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation, Inc. 
https://fsf.org/ Everyone is permitted to copy and 
distribute verbatim copies of this license document, 
but changing it is not allowed.

Note: For detailed license information, 
please read the LICENSE file in the repository[Repository Name: Projects-IoT-Python-Embedded-C]
*/

/*
Author        : Ganesh
script name   : serial_led_on_off_control.c
Functionality : Turn ON/OFF the LED using serial communication
Created on    : 23 SEP 2016
*/


#define ledPin 13
int state = 0;
void setup() {
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
  Serial.begin(9600);               // Default communication rate of the Bluetooth module
}
void loop() {
  if(Serial.available() > 0){       // Checks whether data is comming from the serial port
    state = Serial.read();          // Reads the data from the serial port
 }
 if (state == '0') {
  digitalWrite(ledPin, LOW);        // Turn LED OFF
  Serial.println("LED: OFF");       // Send back, to the phone, the String "LED: ON"
  state = 0;
 }
 else if (state == '1') {
  digitalWrite(ledPin, HIGH);
  Serial.println("LED: ON");;
  state = 0;
 } 
}
