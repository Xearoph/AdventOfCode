with open('inputD6.txt','r') as f:
	lines = f.read().split(",")

lines = list(map(int, lines))

'''
days = 0
count = 0
for y in range(days) :
	for x in range(len(lines)) :
		if lines[x] == 0 :
			lines[x] = 6
			lines.append(8)
		else :
			lines[x] -= 1

global totalFish
totalFish = 0

for x in range(len(lines)) :
	totalFish += 1

print(totalFish)
'''

''' Day 6 P2 '''

fishes = {
	"0":0,
	"1":0,
	"2":0,
	"3":0,
	"4":0,
	"5":0,
	"6":0,
	"7":0,
	"8":0,
}

fishesTemp = {
	"0":0,
	"1":0,
	"2":0,
	"3":0,
	"4":0,
	"5":0,
	"6":0,
	"7":0,
	"8":0,
}
fishesTemplate = {
	"0":0,
	"1":0,
	"2":0,
	"3":0,
	"4":0,
	"5":0,
	"6":0,
	"7":0,
	"8":0,
}

days = 256
count = 0

print(lines)
for x in range(len(lines)) :
	fishes[str(lines[x])] += 1

for y in range(days) :
	for x in range(9) :
		if fishes[str(x)] > 0 and x == 0 :
			fishesTemp["6"] += int(fishes[str(x)])
			fishesTemp["8"] = int(fishes[str(x)])
			
		elif fishes[str(x)] > 0 :
			fishesTemp[str(x-1)] += fishes[str(x)]	
		fishes[str(x)]	= 0
	
	fishes = fishesTemp
	fishesTemp = {key: 0 for key in fishesTemp}

	print(fishesTemp)

totalFishes = 0
for x in range(9) :
	totalFishes += int(fishes[str(x)])
	print('fit',int(fishes[str(x)]))

print(fishes)
print('tf',totalFishes)
