from firebase import Firebase
class FirebaseDB(object):
	def __init__(self):
        self.waterRef = Firebase('https://hamster-home.firebaseio.com/water')
		self.foodRefillRef = Firebase('https://hamster-home.firebaseio.com/refillFood/refillFood')
		self.foodRef = Firebase('https://hamster-home.firebaseio.com/food')
		self.activityRef = Firebase('https://hamster-home.firebaseio.com/activity')

	def getFoodRefill(self):
		return foodRefillRef.get()

	def setFoodRefill(self, state):
		foodRefillRef.set({"refillFood": '"' + state + '"'})

	def setWaterStatus(self, state):
		waterRef.set({"stats": '"' + state + '"'})

	def getWaterStatus(self):
		return waterRef.get()
	
	def updateActivities(self, activity):
		"""
		Update only after setting.
		"""
		if (activity == "water"):
			updateWater()
		elif (activity == "food"):
			pass
		elif (activity == "wheel"):
			pass
		else: print("Error!")

	def updateWater(self):
		desc = "Water levels are " + self.getWaterStatus()
		n = datetime.datetime.now()
		n = n.strftime("%c")
		activityRef.push({
			"date": n,
			"category": "water",
			"description": desc
		})
		