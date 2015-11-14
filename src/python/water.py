class Water(object):
	def __init__(self, status):
        self.status = status

    def readStatus(self):
    	"""
    	Reads from water level sensor and updates status.
    	"""
    	waterLevel = readFromSensor()
    	if (waterLevel == "0"): waterDescription = "empty"
		elif (waterLevel == "1"): waterDescription = "almost empty"
		elif (waterLevel == "2"): waterDescription = "half full"
		elif (waterLevel == "3"): waterDescription = "full"

		self.setStatus(waterDescription)
    	pass

    def setStatus(self, stat):
    	self.status = stat

    def getStatus(self):
    	return self.status