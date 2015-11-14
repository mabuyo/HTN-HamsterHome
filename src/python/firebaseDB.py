from firebase import Firebase
import datetime

class FirebaseDB():
    def __init__(self):
        self.waterRef = Firebase('https://hamster-home.firebaseio.com/waterStatus')
        self.foodRefillRef = Firebase('https://hamster-home.firebaseio.com/refillFood')
        self.foodRef = Firebase('https://hamster-home.firebaseio.com/food')
        self.activityRef = Firebase('https://hamster-home.firebaseio.com/activity')

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
        Update only after setting.
        """
        if (activity == "water"):
            self.updateWater()
        elif (activity == "food"):
            pass
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
        