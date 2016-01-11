import Adafruit_ADS1x15 as ADC

class Wheel(object):
    def __init__(self, diameter):
        self.diameter = diameter
        self.channel = 1

        self.adc = ADC.ADS1x15(0x49)

    def readSensor(self):     
        reading = self.adc.readADCSingleEnded(self.channel)
        print "ADC Reading: " + str(reading/1000) + " V"

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