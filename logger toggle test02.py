import os
import time
import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime


GPIO.setmode(GPIO.BCM) # using broadcomm pin numbers

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

#button toggle
prevlog = 0
#/button toggle


def my_callback(channel):
    global prevlog
    prevlog = not prevlog
    return prevlog

GPIO.add_event_detect(23, GPIO.RISING, callback=my_callback, bouncetime=200 )



def datalog
file = open("/home/pi/data_log.csv", "a")
i=0
if os.stat("/home/pi/data_log.csv").st_size == 0:
    file.write("on\n")
while True:
        i=i+1
        now = datetime.now()
        file.write(str(now)+"\n")
        file.flush()
        time.sleep(5)
        file.close()




while 1:
    OnButton = prevlog

	#logger on
    if (OnButton == True):
        GPIO.output(24, True)
        GPIO.output(25, False)
        print('On')
        datalog()

      

	#logger off
    if (OnButton == False):
        GPIO.output(24, False)
        GPIO.output(25, True)
        

# need to do other stuff here

GPIO.cleanup()
