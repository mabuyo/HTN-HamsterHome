import water
import time

w = water.Water("full")
while True:
	w.readStatus()
	time.sleep(5)
