import Adafruit_ADS1x15 as ADC

class Water(object):
    def __init__(self, status):
        self.status = status
        self.channel = 0

        self.adc = ADC.ADS1x15(0x49)
        self.MAX_VOLTAGE = 2700;
        self.MIN_VOLTAGE = 1300;

    def readStatus(self):
        """
        Reads from water level sensor and updates status.
        """
        waterLevel = self.getSensorLevels()
        print "WaterLevel: " + str(waterLevel)
        if (waterLevel == 0): waterDescription = "empty"
        elif (waterLevel == 1): waterDescription = "almost empty"
        elif (waterLevel == 2): waterDescription = "half full"
        elif (waterLevel == 3): waterDescription = "full"

        self.setStatus(waterDescription)
        print "Status: " + self.status + '\n'
        
    def getSensorLevels(self):
        voltage = self.readSensor()
        percentage = (self.MAX_VOLTAGE - voltage) / (self.MAX_VOLTAGE - self.MIN_VOLTAGE) * 100
        print "Percentage: " + str(percentage) + "%"
        if (percentage < 20): return 0
        elif (percentage >= 20 and percentage < 50): return 1
        elif (percentage >= 50 and percentage < 80): return 2
        else: return 3

    def readSensor(self):     
        reading = self.adc.readADCSingleEnded(self.channel)
        print "ADC Reading: " + str(reading/1000) + " V"
        return reading # returns mV
     
    def setStatus(self, stat):
        self.status = stat

    def getStatus(self):
        return self.status
