from Adafruit_AMG88xx import Adafruit_AMG88xx
from time import sleep

sensor = Adafruit_AMG88xx()
sleep(0.1)
pixels = sensor.readPixels()

print pixels