import sys
import time
import RPi.GPIO as GPIO

"""
Controlling stepper motor credits below:
#--------------------------------------
#    Stepper Motor Test
#
# A simple script to control
# a stepper motor.
#
# Author : Matt Hawkins
# Date   : 28/09/2015
# Modified by Michelle Mabuyo, November 15, 2015
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------
"""

class FoodMotor(object):
    def __init__(self):
        # Use BCM GPIO references
        # instead of physical pin numbers
        GPIO.setmode(GPIO.BCM)

        # Define GPIO signals to use
        # Physical pins 11,15,16,18
        # GPIO17,GPIO22,GPIO23,GPIO24
        self.StepPins = [23,22,17,27]

        # Set all pins as output
        for pin in self.StepPins:
          print "Setup pins"
          GPIO.setup(pin,GPIO.OUT)
          GPIO.output(pin, False)

        # Define advanced sequence
        # as shown in manufacturers datasheet
        self.Seq = [[1,0,1,0],
               [0,1,1,0],
               [0,1,0,1],
               [1,0,0,1]]
               
        self.StepCount = len(self.Seq)
        self.StepDir = 1 # Set to 1 or 2 for clockwise
                    # Set to -1 or -2 for anti-clockwise

        # Read wait time from command line
        self.WaitTime = 10/float(1000)

        # Initialise variables
        self.StepCounter = 0

    def refill(self):
        """
        Activates auger system to refill food.
        TODO: Figure out number of revolutions it takes for food to drop.
        Right now it only turns for ~3 seconds and stops.
        """
        print("Refilling food!")
        timeout = time.time() + 3
        self.__init__()
        try: 
            while True:
                print self.StepCounter
                print self.Seq[self.StepCounter]

                for pin in range(0, 4):
                    xpin = self.StepPins[pin]
                    if self.Seq[self.StepCounter][pin]!=0:
                        print " Enable GPIO %i" %(xpin)
                        GPIO.output(xpin, True)
                    else:
                        GPIO.output(xpin, False)

                self.StepCounter += self.StepDir

                # If we reach the end of the sequence
                # start again
                if (self.StepCounter>=self.StepCount):
                    self.StepCounter = 0
                if (self.StepCounter<0):
                    self.StepCounter = self.StepCount+self.StepDir

                # Wait before moving on
                time.sleep(self.WaitTime)

                if time.time() > timeout:
                    break
        except KeyboardInterrupt:
            print("KeyboardInterrupt\n")
        except:
            print("Other error.\n")
        finally:
            self.StepCounter = 0
            GPIO.cleanup()