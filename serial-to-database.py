import mysql.connector
import serial
from datetime import datetime
from datetime import time

#inititating connection into database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="prototype"
)

#Check if connection to database successfully created
if db.is_connected():
  print("Successfully connected to the database")

#this line below is also to check connection by displaying database version
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print ("Database version : %s " % data)

ser = serial.Serial(port ='COM3',baudrate=9600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,timeout=10)

try:
    ser.isOpen()
    print("Serial port is open")
except:
    print("Error occured")



if(ser.isOpen()):
    try:
        #selama true bakal nunggu hasil baca data dari serial port
        line = ser.readline()
        line = line.decode('utf-8')
        line = line.strip('\r\n')
        saved = line # save input from serial (card uid) from line variable into saved variable
        print(line) #this line is to check if the input from serial is successfully converted into string format
    except Exception:
        print("error")
else:
    print("Cannot access serial port,kindly check if the port is available")


date = datetime.today().strftime('%Y-%m-%d-%H:%M') #get current date via date library and datetime.today function
name = "Rep"#this value will be updated into the database via sql query

sql = "UPDATE data SET name = %s,lastupdate=%s WHERE uid_card = %s " #SQL QUERY TO UPDATE DATA IN DATABASE TABLE
val = (name,date,saved)
cursor.execute(sql, val)
db.commit()
cursor.close()
