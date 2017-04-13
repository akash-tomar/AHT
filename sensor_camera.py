from gpiozero import MotionSensor
from picamera import PiCamera

camera = PiCamera()
pir = MotionSensor(4)
camera.capture()
while True:
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()

#    pir.wait_for_motion()
#    camera.start_preview()
#    pir.wait_for_no_motion()
#    camera.stop_preview()
