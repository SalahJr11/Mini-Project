from gpiozero import DistanceSensor # ultrasonic sensor library
from time import sleep

sensor = DistanceSensor(echo=23, trigger=24)  # define of ultrasonic pins


while True:
    distance1 = sensor.distance * 100  # Convert to centimeters
    if distance1 < 10:  #The code for ultrasonic sensor 
        #The code for camera
    else:
        #The other condition of camera
    print(distance1) ##prints the distance measured 
    sleep(0.5)