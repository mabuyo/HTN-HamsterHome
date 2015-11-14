import camera as cameraComponent
import water as waterComponent
import wheel as wheelComponent
import food as foodComponent
import firebaseDB
import serial 
import io 
from threading import Thread
import datetime


def foodRefill():
    """
    Constantly checks database to see if food needs refilling.
    If 'yes': needs refilling.
    Reset to 'no' after filling.
    """
    while True:
        needsRefill = database.getFoodRefill();
        if (needsRefill == "yes"): 
            # TODO: delegate to food.py for
            food.refill()

            # reset database to no when done feeding
            database.updateActivities("food")
            database.setFoodRefill("no")

def waterLevels():
    """
    Constantly checks water levels of hamster cage and updates database.
    Four possible values: {Full, Half Full, Almost Empty, Empty}
    """
    while True:
        current_status = water.getStatus()  # sensor
        old_status = database.getWaterStatus()  # stored in database

        if (current_status != old_status):  # Something has changed!
            # update database
            database.setWaterStatus(current_status)
            database.updateActivities("water")


def main():
    print("Hello World! This is Hamster Home.\n")

    # initialize threads
    foodRefillThread = Thread(target=foodRefill)
    #foodRefillThread.start()

    waterLevelsThread = Thread(target=waterLevels)
    waterLevelsThread.start()

########### GLOBAL VARIABLES #############
##########################################

# connect to database
database = firebaseDB.FirebaseDB()

# initialize components
food = foodComponent.FoodMotor()
water = waterComponent.Water("full")
wheel = wheelComponent.Wheel(12)
camera = cameraComponent.Camera()

##########################################
######## END GLOBAL VARIABLES ############

if __name__ == "__main__":
    main()