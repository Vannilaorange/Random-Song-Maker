  import random
# Select a random amount of beats.
  beats = random.randrange(200, 400)
print(beats)
# Figure out the corresponding amount of measures.
  (measures1) = beats / 4
# This SHOULD round measures1 up to the nearest whole number
  math.ceil(measures1)
