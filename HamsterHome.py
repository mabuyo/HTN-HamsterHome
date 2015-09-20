
from firebase import Firebase
import serial
import io 
from threading import Thread

waterRef = Firebase('https://hamster-home.firebaseio.com/water')
s = serial.Serial('/dev/tty.usbmodem1421', 9600)

def handleSerialData():
	while True:
		incomingSerialData = s.readline()
		print incomingSerialData
		if incomingSerialData.startswith('/W'):
			waterLevel = incomingSerialData[2]
			print waterLevel
			if (waterLevel == "0"): waterDescription = "empty"
			elif (waterLevel == "1"): waterDescription = "almost empty"
			elif (waterLevel == "2"): waterDescription = "half full"
			elif (waterLevel == "3"): waterDescription = "full"
			print waterDescription
			waterRef.set({"stats": waterDescription})


		elif incomingSerialData.startswith('/T'):
			spins = incomingSerialData[2:]
			print spins



handleSerialDataThread = Thread(target = handleSerialData)
handleSerialDataThread.start()