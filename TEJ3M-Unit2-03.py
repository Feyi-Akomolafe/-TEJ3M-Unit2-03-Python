# Copyright(c) 2023 Feyi Akomolafe All rights reserved.
# Created by : Feyi Akomolafe
# Created on : February 2023
# TEJ3M-Unit2-03.py File.

import time
import board
import digitalio

led13 = digitalio.DigitalInOut(board.GP13)
led13.direction = digitalio.Direction.OUTPUT

while True:
    led13.value = True
    time.sleep(1)
    led13.value = False
    time.sleep(1)
