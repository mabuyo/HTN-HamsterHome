from firebase import Firebase
import datetime

class FirebaseDB():
    def __init__(self):
        self.waterRef = Firebase('https://hamster-home.firebaseio.com/waterStatus')
        self.foodRefillRef = Firebase('https://hamster-home.firebaseio.com/refillFood')
        self.foodRef = Firebase('https://hamster-home.firebaseio.com/food')
        self.activityRef = Firebase('https://hamster-home.firebaseio.com/activity')
        self.tempRef = Firebase('https://hamster-home.firebaseio.com/temperature')

    def getFoodRefill(self):
        return self.foodRefillRef.get()

    def setFoodRefill(self, state):
        self.foodRefillRef.set(state)

    def setWaterStatus(self, state):
        self.waterRef.set(state)

    def getWaterStatus(self):
        return self.waterRef.get()
    
    def updateActivities(self, activity):
        """
        Water: Needs to be set to proper value in database before activity is updated.
        """
        if (activity == "water"):
            self.updateWater()
        elif (activity == "food"):
            self.updateFood()
        elif (activity == "wheel"):
            pass
        else: print("Error!")

    def updateWater(self):
        description = "Water levels are " + self.getWaterStatus()
        n = datetime.datetime.now()
        n = n.strftime("%c")
        self.activityRef.push({
            "date": n,
            "category": "water",
            "description": description
        })

    def updateFood(self):
        # TODO: This only deals with situation where food is refilled. Possible extension could be "food running low", according to calories burned or time passed.
        description = "Food refilled."
        n = datetime.datetime.now()
        n = n.strftime("%c")
        self.activityRef.push({
            "date": n,
            "category": "food",
            "description": description
        })






        