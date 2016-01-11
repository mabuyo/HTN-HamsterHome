import wheel
import time

w = wheel.Wheel(5)
while True:
	w.readSensor()
	time.sleep(5)