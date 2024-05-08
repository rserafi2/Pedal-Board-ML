outputfilepath = r"C:\Users\ryrid\Documents\PedalBoardML\scripts\modeloutputs.txt"

import random
import os

numpedals = 9
numvalues = 45

def randnuminterval(min, max, interval):
    if (interval < 0):
      return random.uniform(min,max)
    else:
      return round(random.uniform(min,max) * (1/interval)) / (1/interval)

enables = [0] * numpedals

for i in range(len(enables)):
    enables[i] = random.randint(0, 1)


mins = [0,	0,	0,	0,	1,	-60,	-120,	-120,	0,	-60,	0,	-20,	20,	20,	0,	-24,	0,	-24,	0,	-24,	-24,	0,	1,	-40,	0,	0,	-120,	-120,	-120,	-120,	0,	0,	-60,	0,	1,	1,	0.1,	0,	-100,	-100,	0,	-120,	-120,	-120,	0.001]
maxs = [1,	1,	1,	0.1,	300,	60,	0,	0,	2,	0,	9,	20,	2000,	1000,	100,	24,	22000,	24,	22000,	24,	24,	50,	10,	0,	2,	4000,	6,	6,	6,	6,	1,	100,	0,	1,	250,	8,	16,	1,	12,	12,	200,	6,	6,	6,	100]
intervals = [-1,	-1,	-1,	-1,	-1,	1,	1,	1,	1,	0.1,	1,	0.1,	10,	1,	0.1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	20,	1,	1,	1,	1,	1,	1,	1,	-1,	-1,	1,	-1,	-1,	1,	1,	1,	1,	1,	1,	0.1]

wah_mins = [0,	0,	0,	0]	
fuzz_mins = [1,	-60,	-120,	-120,	0]	
compressor_mins = [-60,	0,	-20,	20,	20,	0]
eq_mins = [-24,	0,	-24,	0,	-24,	-24]	
distortion_mins = [0,	1,	-40,	0]	
delay_mins = [0,	-120,	-120,	-120,	-120,	0]	
tremolo_mins = [0,	-60,	0]	
chorus_mins = [1,	1,	0.1,	0,	-100,	-100]
flanger_mins = [0,	-120,	-120,	-120,	0.001]

wah_maxs = [1,	1,	1,	0.1]	
fuzz_maxs = [300,	60,	0,	0,	2]	
compressor_maxs = [0,	9,	20,	2000,	1000,	100]	
eq_maxs = [24,	22000,	24,	22000,	24,	24]	
distortion_maxs = [50,	10,	0,	2]
delay_maxs = [4000,	6,	6,	6,	6,	1]	
tremolo_maxs = [100,	0,	1]
chorus_maxs = [250,	8,	16,	1,	12,	12]
flanger_maxs = [200,	6,	6,	6,	100]

wah_intervals = [-1,	-1,	-1,	-1]
fuzz_intervals = [-1,	1,	1,	1,	1]
compressor_intervals = [0.1,	1,	0.1,	10,	1,	0.1]
eq_intervals = [1,	1,	1,	1,	1,	1]
distortion_intervals = [1,	1,	1,	1]
delay_intervals = [20,	1,	1,	1,	1,	1]
tremolo_intervals = [1,	1,	-1]
chorus_intervals = [-1,	1,	-1,	-1,	1,	1]
flanger_intervals = [1,	1,	1,	1,	0.1]


wah = [0] * len(wah_mins)
fuzz = [0] * len(fuzz_mins)
compressor = [0] * len(compressor_mins)
eq = [0] * len(eq_mins)
distortion = [0] * len(distortion_mins)
delay = [0] * len(delay_mins)
tremolo = [0] * len(tremolo_mins)
chorus = [0] * len(chorus_mins)
flanger = [0] * len(flanger_mins)


for i in range(len(wah_mins)):
    if enables[0] == 1:
        wah[i] = randnuminterval(wah_mins[i], wah_maxs[i], wah_intervals[i])
    else:
        wah[i] = 0;

for i in range(len(fuzz_mins)):
    if enables[1] == 1:
        if i == 4:  #setting to stereo
            fuzz[i] = 2;
        else:
            fuzz[i] = randnuminterval(fuzz_mins[i], fuzz_maxs[i], fuzz_intervals[i])   
    else:
        fuzz[i] = 0;
  
for i in range(len(compressor_mins)):
    if enables[2] == 1:
        compressor[i] = randnuminterval(compressor_mins[i], compressor_maxs[i], compressor_intervals[i])
    else:
        compressor[i] = 0;
        
for i in range(len(eq_mins)):
    if enables[3] == 1:
        eq[i] = randnuminterval(eq_mins[i], eq_maxs[i], eq_intervals[i])
    else:
        eq[i] = 0;
    
for i in range(len(distortion_mins)):
    if enables[4] == 1:
        if i == 3:  #setting to stereo
            distortion[i] = 2;
        else:
            distortion[i] = randnuminterval(distortion_mins[i], distortion_maxs[i], distortion_intervals[i])
    else:
        distortion[i] = 0;
    
for i in range(len(delay_mins)):
    if enables[5] == 1:
        delay[i] = randnuminterval(delay_mins[i], delay_maxs[i], delay_intervals[i])
    else:
        delay[i] = 0;
    
for i in range(len(tremolo_mins)):
    if enables[6] == 1:
        tremolo[i] = randnuminterval(tremolo_mins[i], tremolo_maxs[i], tremolo_intervals[i])
    else:
        tremolo[i] = 0;
    
for i in range(len(chorus_mins)):
    if enables[7] == 1:
        chorus[i] = randnuminterval(chorus_mins[i], chorus_maxs[i], chorus_intervals[i])
    else:
        chorus[i] = 0;
    
for i in range(len(flanger_mins)):
    if enables[8] == 1:
        flanger[i] = randnuminterval(flanger_mins[i], flanger_maxs[i], flanger_intervals[i])
    else:
        flanger[i] = 0;

output = enables + wah + fuzz + compressor + eq + distortion + delay + tremolo + chorus + flanger

with open(outputfilepath, "w") as file:
    for idx, value in enumerate(output):
        if (idx < numpedals + numvalues - 1):
            file.write("%s\n" % value)
        else:
            file.write("%s" % value)
file.close()

os.system("python updateAllPedals.py")

