from firebase import Firebase
import serial
import io 
from threading import Thread
import datetime

diameterOfWheel = 0.12

waterRef = Firebase('https://hamster-home.firebaseio.com/water')
foodRefillRef = Firebase('https://hamster-home.firebaseio.com/refillFood/refillFood')
foodRef = Firebase('https://hamster-home.firebaseio.com/food')
activityRef = Firebase('https://hamster-home.firebaseio.com/activity')
wheelRef = Firebase('https://hamster-home.firebaseio.com/wheel')

s = serial.Serial('/dev/tty.usbmodem1451', 9600)

def handleSerialData():
	previousWaterState = "random";
	while True:
		incomingSerialData = s.readline()
		print incomingSerialData
		if incomingSerialData.startswith('/W'):
			waterLevel = incomingSerialData[2]
			#print waterLevel
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
				n = datetime.datetime.now()
				n = n.strftime("%c")
				activityRef.push({
					"date": n,
					"category": "water",
					"description": desc
				})
		elif incomingSerialData.startswith('/T'):
			revolutions = float(incomingSerialData[2:])
			print revolutions
			circumference = 3.14159*diameterOfWheel
			distance = circumference*revolutions
			print distance
			d = datetime.datetime.now()
			key = str(str(d.month)+'-'+str(d.day)+'-'+str(d.year))

			# if the hour already exists, then update it with old distance
			# wheelDateLog = wheelRef.child(key + '/day')
			# wheelHourLog = wheelRef.child(key + '/hours/' + str(d.hour))
			# if (wheelHourLog.get() == None): oldDistance = 0
			# else: oldDistance = wheelRef.child(key+'/hours/' + str(d.hour)).get()
			# print oldDistance
			# wheelDateLog.set({
			# 	"totalDailyDistance": 0
			# })
			
			thisday = wheelRef.child(key).get()
			oldDistance = thisday["totalDailyDistance"]
			wheelRef.child(key).set({
				"totalDailyDistance": oldDistance + distance
			})

def handleFireBaseData():
	while True:
		refillCommand = foodRefillRef.get();
		if (refillCommand == "f"): 
			#send f over to arduino 
			s.write('f')
			# reset database to n when done feeding
			foodRefillRef.set({"refillFood": "n"})


handleFireBaseDataThread = Thread(target=handleFireBaseData)
handleFireBaseDataThread.start()

handleSerialDataThread = Thread(target = handleSerialData)
handleSerialDataThread.start()