#!/usr/bin/env python3
import EmulateGPIO as GPIO
from IPython.display import clear_output
import time
import requests
import os
_=os.system("clear")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

MotionsensorPin = 21
FanPin   = 23

GPIO.setup(MotionsensorPin, GPIO.OUT)
GPIO.setup(FanPin, GPIO.OUT)
print()
while True:

    lit = input("Emulator is ready for the job..! < m > = Motion sensor or < f > = Fan <q> to quit: ")

    lit1 = lit.lower()


    if lit1 == "m":
        print("Motion sensor ==> Activated")
        r = requests.post('https://maker.ifttt.com/trigger/iot1/with/key/besK7vjGRYHkNqTTztlEnz', params={"value1":"none","value2":"none","value3":"none"})
        GPIO.output(MotionsensorPin, False)
        GPIO.output(FanPin,   True)
        print()

    elif  lit1 == "f":
        print("Fan has been turned ON")
        r = requests.post('https://maker.ifttt.com/trigger/iot2/with/key/besK7vjGRYHkNqTTztlEnz', params={"value1":"none","value2":"none","value3":"none"})
        GPIO.output(MotionsensorPin, True)
        GPIO.output(FanPin,   False)
        print()

    elif  lit1 == "q":
        print("Emulator has been stoped... t- 3 seconds to exit")
        GPIO.output(MotionsensorPin, False) 
        GPIO.output(FanPin,   False)
        exit()

    else:
        print("Please enter m for Motion sensor, f for FAN, or q to quit.")
