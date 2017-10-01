from Adafruit_AMG88xx import Adafruit_AMG88xx
from time import sleep
import math

# http://www.brython.info/

sensor = Adafruit_AMG88xx()

def getPixels():
	pixels = [0.0 for x in range(64)]

	for i in range(5):
		reading = sensor.readPixels()
		for j in range(len(reading)):
			if pixels[j] == 0.0:
				pixels[j] = reading[j]

	return pixels;

def getTemp():
	return sensor.readThermistor()

def getExpectedSkinTemp(ambientTemp):
	if ambientTemp >= 40:
		return 40.0
	else:
		return 20.10186 + 0.6096458 * ambientTemp - 0.004770726 * (ambientTemp ** 2)

def findPotentialChildren(pixels, childTemp):
	col = 0
	row = 0
	hotSpots = []
	children = []

	for col in range(8):
		for row in range(8):
			i = 8 * row + col

			if abs(pixels[i] - childTemp) <= 1:
				hotSpots.append(i);

	for x in range(len(hotSpots)):
		i = hotSpots[x]

		if i - 1 in hotSpots or i + 1 in hotSpots or i - 8 in hotSpots or i + 8 in hotSpots or i - 7 in hotSpots or i - 9 in hotSpots or i + 7 in hotSpots or i + 9 in hotSpots:
			children.append(i)

	return children

def confirmPotentialChildren(potentialChildren):
	return potentialChildren

def checkChild():
	pixels = getPixels()
	temp = getTemp()
	childTemp = getExpectedSkinTemp(temp)

	potentialChildren = findPotentialChildren(pixels, childTemp)
	children = confirmPotentialChildren(potentialChildren)

	return len(children) > 0

def tocol(num):
	norm = (num - 15.0) / 28.0
	val = math.ceil(norm * 255.0)
	antival = 255.0 - val

	val = str(hex(val))[-2:]
	antival = str(hex(antival))[-2:]

	if val[0] == "x":
		val = "0" + val[1]

	if antival[0] == "x":
		antival = "0" + antival[1]

	return "#" + val + "00" + antival

def getWebOutput():
	col = getPixels()

	inner = ""
	for i in range(8):
		row = "<div>"

		for j in range(8):
			row = row + "<div class=\"square\" style=\"background:" + tocol(col[8 * j + i]) + "\"></div>"

		row += "</div>"
		inner += row

	return inner