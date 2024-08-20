from picamera import PiCamera
import RPi.GPIO as GPIO
from time import sleep
camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
sleep(2)  # Give time for the camera to warm up




############# codition #####################
    print("Object detected within 10 cm, taking a picture...")
    camera.capture('/home/pi/Desktop/object_detected.jpg')
    sleep(5)  # Wait before taking another picture
    camera.stop_preview()

