import random
import time

timePassed = 0.0


def emulate():
    voltage = random.uniform(-5, 5)
    global timePassed
    timePassed = timePassed + 0.1
    time.sleep(0.1)
    return [timePassed, voltage]
