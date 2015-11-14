import camera
import water
import wheel
import food
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
			database.setFoodRefill("no")

def waterLevels():
	"""
	Constantly checks water levels of hamster cage and updates database.
	Four possible values: {Full, Half Full, Almost Empty, Empty}
	"""
	while True:
		current_status = water.getStatus()	# sensor
		old_status = database.getWaterStatus()	# stored in database

		if (current_status != old_status):	# Something has changed!
			# update database
			database.setWaterStatus(current_status)
			database.updateActivities("water")


def main():
	print("Hello World! This is Hamster Home.\n")

	# connect to database
	database = firebaseDB.Firebase()

	# initialize components
	food = food.FoodMotor()
	water = water.Water()
	wheel = wheel.Wheel()
	camera = camera.Camera()


	# initialize threads
	foodRefillThread = Thread(target=foodRefill)
	foodRefillThread.start()

	waterLevelsThread = Thread(target=waterLevels)
	waterLevelsThread.start()

if __name__ == "__main__":
    main()