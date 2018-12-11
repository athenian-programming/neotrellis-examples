import time
import random
import adafruit_trellism4

trellis = adafruit_trellism4.TrellisM4Express()

PAUSE = 0.01

while True:
    for x in range(8):
        for y in range(4):
            trellis.pixels[x, y] = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
            time.sleep(PAUSE)
