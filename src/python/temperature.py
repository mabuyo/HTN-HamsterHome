import Adafruit_DHT

class Temperature(object):
	def __init__(self):
		self.sensor = Adafruit_DHT.DHT22
		self.pin = 20
		self.humidity = 0
		self.temperature = 0

	def getSensorReading(self):
		# Try to grab a sensor reading.  Use the read_retry method which will retry up
		# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
		self.humidity, self.temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)

		# Note that sometimes you won't get a reading and
		# the results will be null (because Linux can't
		# guarantee the timing of calls to read the sensor).  
		# If this happens try again!
		# if self.humidity is not None and self.temperature is not None:
		#         print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(self.temperature, self.humidity)
		# else:
		#         print 'Failed to get reading. Try again!'

	def getTemperature(self):
		return self.temperature

	def getHumidity(self):
		return self.humidity