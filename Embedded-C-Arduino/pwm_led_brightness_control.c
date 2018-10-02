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
script name   : pwm_led_brightness_control.c
Functionality : Controls the LED brightness using PWM
Description   : Fade
                This example shows how to fade an LED on pin 9
                using the analogWrite() function.
Created on    : 20 AUG 2016
*/

int led = 44;                                         // the pin that the LED is attached to
int brightness = 0;                                   // how bright the LED is
int fadeAmount = 5;                                   // how many points to fade the LED by

// the setup routine runs once when you press reset                                                   
void setup() {
  pinMode(led, OUTPUT);                               // declare pin 9 to be an output
}                                                     

// the loop routine runs over and over again forever                                                     
void loop() {
  analogWrite(led, brightness);                       // set the brightness of pin 9
  
  brightness = brightness + fadeAmount;               // change the brightness for next time through the loop
 
  
  if (brightness == 0 || brightness == 255) {
    fadeAmount = -fadeAmount ;
  }                                                   // reverse the direction of the fading at the ends of the fade
 
  delay(30);                                          // wait for 30 milliseconds to see the dimming effect
}
