import os
import time
import Rpi.GPIO as GPIO

class LED:
 

 def lit(self,prob):
  i=0
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(7,GPIO.OUT)
  GPIO.setwarnings(False)
  while(i>0):
   if prob>0.5:
    GPIO.output(7,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(7,GPIO.LOW)
    GPIO.output(7,GPIO.LOW)
    time.sleep(1)
    i-=1
   else:
    GPIO.output(7,GPIO.LOW)
    time.sleep(1)
    i-=1
  GPIO.output(7,GPIO.LOW) 
  GPIO.cleanup()
