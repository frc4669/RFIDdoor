import RPi.GPIO as GPIO

import time



controlPort = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(controlPort,GPIO.OUT)

cycleFreq = 50

pwm = GPIO.PWM(controlPort,cycleFreq)

# Duty cycle constants

left = 1.5

right = 2.5

middle = (right - left) / 2 + left

cycleMS = 1000 / cycleFreq



def startpwm(pos):

    dcp = (pos * 100) / cycleMS

    pwm.start(dcp)

    time.sleep(.5)

#    pwm.stop()


def move(pos):

    startpwm(right)

    dcp = (pos * 100) / cycleMS

    pwm.ChangeDutyCycle(dcp)

    time.sleep(.5)

def openDoor():

        move(left)

        time.sleep(5)

        move(right)

        pwm.stop()



#main program loop

startpwm(right)

while True:

        file = open("idlist", "r")

        readid = raw_input("scan id card")

       while True:

                line = file.readline()

                if line.strip() == readid:

                        openDoor()

                        break

                elif line == "":

                        print ("id does not match")

                        print (readid)

                        break

        file.close()




