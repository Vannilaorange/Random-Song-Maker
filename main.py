# THIS ENTIRE FILE DECIDES THE AMOUNT OF BEATS THEN CALCULATES THE AMOUNT OF MEASURES.
import random
import math
# Select a random amount of beats.
beats = random.randrange(200, 400)
print(beats)
# Figure out the corresponding amount of measures.
(measures1) = beats / 4
print (measures1)
# This SHOULD round measures1 up to the nearest whole number.
measures2 = math.ceil(measures1)
print (measures2)
# The python part is done now, it shouldn't require any more editing.
