import Adafruit_ADS1x15 as ADC
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class Wheel(object):
    def __init__(self, diameter):
        self.diameter = diameter
        self.channel = 1

        self.adc = ADC.ADS1x15(0x49)
        self.LED = 26
        GPIO.setup(self.LED, GPIO.OUT)
        GPIO.output(self.LED, GPIO.HIGH)

        self.sensor = self.readSensor
        self.median = 3.3045


    def readSensor(self):     
        if(GPIO.input(self.LED) == GPIO.HIGH):
            print "LED on"
        reading = self.adc.readADCSingleEnded(self.channel)
        print "ADC Reading: " + str(reading/1000) + " V"
        return reading/1000
        
    def calculate(self, sensorVal, state=0, quarterTurns=0, changeState=0):
        """
        TODO: calculate full turns.
        """
        if sensorVal < self.median:
            newBinaryWheelValue = 0
        else:
            newBinaryWheelValue = 1
        
        if newBinaryWheelValue != state:  #changed states
            changeState += 1
        else if newBinaryWheelValue == state:
            changeState = 0
          
        if changeState >= 2:
            quarterTurns += 1
            state = newBinaryWheelValue
            changeState = 0

        if quarterTurns == 4:
            fullTurns += 1
            quarterTurns = 0

    def calculateDistance():
        # revolutions = float(incomingSerialData[2:])
        revolutions = 1
        circumference = 3.14159*diameterOfWheel
        distance = circumference*revolutions
        
### OLD STUFF
# d = datetime.datetime.now()
# key = str(str(d.month)+'-'+str(d.day)+'-'+str(d.year))
# thisday = wheelRef.child(key).get()
# oldDistance = thisday["totalDailyDistance"]
# wheelRef.child(key).set({
#     "totalDailyDistance": oldDistance + distance
# })