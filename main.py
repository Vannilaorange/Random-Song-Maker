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
# Generate a .csd file
csd_content = f"""
<CsoundSynthesizer>
<CsOptions>
; Select audio/midi flags here according to platform
-odac ;;;RT audio out
</CsOptions>
<CsInstruments>
instr 1
    a1 oscil 0.5, 440, 1
    out a1
endin
</CsInstruments>
<CsScore>
f 1 0 1024 10 1
i 1 0 {measures2} 
</CsScore>
</CsoundSynthesizer>
"""

with open("output.csd", "w") as file:
    file.write(csd_content)
