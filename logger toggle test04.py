import os
import time
import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
from itertools import count


GPIO.setmode(GPIO.BCM) # using broadcomm pin numbers

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

#button toggle
prevlog = 0



def my_callback(channel):
    global prevlog
    prevlog = not prevlog
    return prevlog

#/button toggle

GPIO.add_event_detect(23, GPIO.RISING, callback=my_callback, bouncetime=200 )



def datalog():
    file = open("/home/pi/filename", "a")
       
    #title of columns
    if os.stat("/home/pi/filename").st_size == 0:
        file.write("date, on\n")
    
    
    now = datetime.now()
    file.write(str(now)+"\n")
    file.flush()
    time.sleep(5)
    file.close()




#main program
while 1:
    OnButton = prevlog

    filename = ("data_%03i.dat" % i for i in count(1))
    

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
        next(filename)
        

# need to do other stuff here

GPIO.cleanup()
