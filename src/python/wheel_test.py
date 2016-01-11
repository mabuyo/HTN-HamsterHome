import wheel
import time

w = wheel.Wheel(5)
while True:
	sensorVal = w.readSensor()
	w.calculate(sensorVal)
	time.sleep(5)