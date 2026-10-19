# Animate String using Python

# sys = In this case, we use it to directly write output to the console (sys.stdout.write()).
# time = It allows us to pause the pragram using time.sleep() - this is what makes the typing effect possible.

import sys
import time

text = "Welcome to Python Magic"

for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.2)
