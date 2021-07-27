#!/usr/bin/env python3
# Code Cell 1.
# Import the dweepy module that is a collection of functions that make it
# easier to communicate with dweet.io
#import dweepy

# Import the GPIO modules to control the GPIO pins of the Raspberry Pi
# Uncomment the following only when testing on a physcial Rasberry Pi
# Comment the following when testing on a Raspbian VM
#import RPi.GPIO as GPIO

# Import the Mock GPIO modules to control the Mock GPIO pins of the Raspberry Pi
# Uncomment the following when testing on a Raspbian VM
# Comment the following when testing on a physcial Rasberry Pi
import EmulateGPIO as GPIO

# Import to clear cell output with code
from IPython.display import clear_output

# Import the time module to control the timing of your application (e.g. add delay, etc.)
import time
import requests

import os

_=os.system("clear")

# Code Cell 2.
#Setup hardware
# Set the desired pin numbering scheme:
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Create variables for the GPIO PINs the LEDs are connected to
# ============================================
# the PIN of the green LED
MotionsensorPin = 21   #Add values: add the pin number for the green LED
# the PIN of the red LED
FanPin   = 23   #Add values: add the pin number for the red LED
#=============================================

# Setup the direction of the GPIO pins - either INput or OUTput
# The PINs that connect LEDs must be set to OUTput mode:
GPIO.setup(MotionsensorPin, GPIO.OUT)
GPIO.setup(FanPin, GPIO.OUT)
print()

#Code Cell 4.
while True:
    # Asks the user to select the LED. Put the response into a variable.
    lit = input("Emulator is ready for the job..! < m > = Motion sensor or < f > = Fan <q> to quit: ")

    # convert the input to lowercase and put it in another variable.
    lit1 = lit.lower()

    #Set the LED state based on the user input
    if lit1 == "m": #If the user chose the red LED
        print("Motion sensor ==> Activated")

        # Your IFTTT URL with event name, key and json parameters (values)
        r = requests.post('https://maker.ifttt.com/trigger/iot1/with/key/besK7vjGRYHkNqTTztlEnz', params={"value1":"none","value2":"none","value3":"none"})

        GPIO.output(MotionsensorPin, False) # False = set 0V on the pin
        GPIO.output(FanPin,   True)  # True = set 3.3V on the pin
        print()

    elif  lit1 == "f": #If the user chose the green LED
        print("Fan has been turned ON")

        # Your IFTTT URL with event name, key and json parameters (values)
        r = requests.post('https://maker.ifttt.com/trigger/iot2/with/key/besK7vjGRYHkNqTTztlEnz', params={"value1":"none","value2":"none","value3":"none"})

        GPIO.output(MotionsensorPin, True) # True = set 3.3V on the pin
        GPIO.output(FanPin,   False) #False = set 0V on the pin
        print()

    elif  lit1 == "q": #If the user chose to quit the program
        print("Emulator has been stoped... t- 3 seconds to exit")
        GPIO.output(MotionsensorPin, False) # True = set 3.3V on the pin
        GPIO.output(FanPin,   False) #False = set 0V on the pin
        exit()

    else:  #If the user entered something other than r, g, or q.
        print("Please enter m for Motion sensor, f for FAN, or q to quit.")
