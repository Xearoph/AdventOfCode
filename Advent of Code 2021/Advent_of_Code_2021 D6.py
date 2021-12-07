with open('inputD6.txt','r') as f:
	lines = f.read().split(",")

lines = list(map(int, lines))
days = 32
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

