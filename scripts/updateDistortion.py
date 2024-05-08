outputfilepath = r"C:\Users\ryrid\Documents\PedalBoardML\scripts\modeloutputs.txt"
pedalfilepath = r"C:\Users\ryrid\AppData\Roaming\REAPER\Effects\guitar\distortion"

newsliders = [0,0,0,0]
outputoffset = 30

with open(outputfilepath, "r") as file:
    outputs = file.readlines()
file.close()

for idx, val in enumerate(newsliders):
    temp = outputs[idx+outputoffset].split('\n')
    newsliders[idx] = temp[0]

with open(pedalfilepath, "r") as file:
    data = file.readlines()
file.close()

slidercount = 0
for idx, line in enumerate(data):
    if "@init" in line:
        break
        
    if line.startswith("slider"):
        temp = line.replace(":",":?").replace("<","?<").split("?")
        temp[1] = str(newsliders[slidercount])
        data[idx] = "".join(temp)
        slidercount+=1
        
with open(pedalfilepath, "w") as file:
    file.writelines(data)
file.close()