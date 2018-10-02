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
script name   : security_breach.c
Functionality : Intruder Alert system using door sensor
Description   : Alerts the user with LED notification of intruder entry
Created on    : 20 AUG 2016
*/

#include<stdio.h>
#include<conio.h>

#define LED1() {printf("\nLED 1 is ON and Door 1 is breached\n");}
#define LED2() {printf("\nLED 2 is ON and Door 2 is breached\n");}

void main()
{
int D1=0, D2=0,Armed=0;      //D1,D2=0 means secured 
							//Armed 0 means not armed, if 1 Armed
						   //Buzzer =0  means deactivated, if 1 means activated

while (1)
	{
		printf("\n\n\t\tWelcome to Door security breach detection system\n");
		printf("\n1 for Armed\nPress any key to not armed\nEnter your choice: ");
		scanf("%d",&Armed);
		if(Armed == 1)
		{
		printf("\n\n\t\tArmed\n\n");
		printf("\nPress 0 to close Door \nPress any number to keep the door open\nEnter your choice for Door 1: ");
		scanf("%d",&D1);
		printf("\nPress 0 to close Door \nPress any number to keep the door open\nEnter your choice for Door 2: ");
		scanf("%d",&D2);
		printf("\n Door 1:%d",D1);
		printf("\n Door 2:%d",D2);
		if (D1==0 && D2==0)
		{
		printf("\nBoth Doors are closed, you are safe\n");
		}
		else if (D1!=0 && D2==0)
		{
		LED1();
		}
		else if(D1==0 && D2!=0)
		{
		LED2();
		}
		else
		{
		printf("\nBoth Doors are breached, you have to be cautious\n");
		}
		}
		else
		{
		printf("\n\nNot Armed\n\n");
		}
}	
	getch();
}