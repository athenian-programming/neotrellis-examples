import math
import time
import random
import busio
import adafruit_adxl34x
import board
import adafruit_trellism4

# https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/master/NeoTrellisM4_Dice/code.py

trellis = adafruit_trellism4.TrellisM4Express()

i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)

previous_reading = [None, None, None]
bound = 4.0


def randomize():
    print("Reset colors")
    for x in range(8):
        for y in range(4):
            c = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
            trellis.pixels[x, y] = c


def shaken():
    """Detect when the Trellis is shaken.
    See http://www.profoundlogic.com/docs/display/PUI/Accelerometer+Test+for+Shaking
    TL;DR one or more axis experiences a significant (set by bound) change very quickly
    Returns whether a shake was detected.
    """
    global previous_reading
    result = False
    x, y, z = accelerometer.acceleration
    if previous_reading[0] is not None:
        result = (math.fabs(previous_reading[0] - x) > bound and
                  math.fabs(previous_reading[1] - y) > bound and
                  math.fabs(previous_reading[2] - z) > bound)
    previous_reading = (x, y, z)
    return result


randomize()

while True:
    if shaken():
        randomize()

    time.sleep(.1)
