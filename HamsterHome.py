
from firebase import Firebase
import serial
import io 
from threading import Thread

#diameterOfWheel = 

waterRef = Firebase('https://hamster-home.firebaseio.com/water')
foodRefillRef = Firebase('https://hamster-home.firebaseio.com/food/refillFood')
foodRef = Firebase('https://hamster-home.firebaseio.com/food')
activityRef = Firebase('https://hamster-home.firebaseio.com/activity')
s = serial.Serial('/dev/tty.usbmodem1411', 9600)

def handleSerialData():
	previousWaterState;
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
			# activity push
			if (waterDescription != previousWaterState): 
				previousWaterState = waterDescription
				desc = "Water levels are " + waterDescription
				activityRef.push({
					"date": new Date().toString(),
					"category": "water",
					"description": desc
				})



		elif incomingSerialData.startswith('/T'):
			revolutions = incomingSerialData[2:]
			print revolutions
			circumference = 3.14159*diameterOfWheel
			distance = circumference*revolutions
			#totalHourlyDistance = (distance pulled from database) + distance
			#total 

def handleFireBaseData():
	while True:
		refillCommand = foodRefillRef.get();
		if (refillCommand == "f"): 
			#send f over to arduino 
			print refillCommand
			# reset database to n when done feeding
			foodRef.set({"refillFood": "n"})


handleFireBaseDataThread = Thread(target=handleFireBaseData)
handleFireBaseDataThread.start()

# handleSerialDataThread = Thread(target = handleSerialData)
# handleSerialDataThread.start()