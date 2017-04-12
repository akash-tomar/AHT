import RPi.GPIO as GPIO
import time
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)
GPIO.setup(3, GPIO.OUT)

def getOutputFromSensor():
    while True:
        i = GPIO.input(11)
        if i == 0:
            print "no intruders",i
            GPIO.output(3,0)
            # return 0
            # time.sleep(0.1)
        elif i==1:
            print "intruder detected",i
            GPIO.output(3,1)
            # return 1
        # time.sleep(0.1)
getOutputFromSensor()
# class StartSensor:
# 	def start_sensor(self):
# 		return getOutputFromSensor()