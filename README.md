# Python-Serial-To-Database

Have you ever do some IoT research or project with Arduino and wanted to store the data you get into the database ? 
There are several ways to do this such as adding an Ethernet Shield to connect directly into the database,but this will be very tricky and if your project is a prototype will be time consuming.

So i decided to do some experiments by handling serial input from arduino and handle it with python to connect it directly into the database

To use this code you need to create your own database first,give it a simple name.

Add 3 columns : name,lastupdate and uid_card

The project to test with this code is an Arduino connected with MFRC-522 RFID Reader. 

Before using it with this code you also need to make the arduino takes only the UID Card upon the read of the RFID CARD.
(I will add the code soon to help you get along easier)

This code works literally like this : 

- Card scanned , arduino takes the UID 
- Arduino send the UID taken from the card via Serial input into the PC via USB Port
- Python handle the serial input with serial module/library
- Python do query into MySQL table and updated UID received from serial along with another additional values 



