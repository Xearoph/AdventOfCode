with open('inputD2.txt','r') as f:
	lines = f.read().split()

''' Day 2 - part 1 '''

value1 = 0
value2 = 0

for x in range(len(lines)) :

	if lines[x] == 'forward' :
		value1 += int(lines[x+1])
	elif lines[x] == 'up' :
		value2 -= int(lines[x+1])
	elif lines[x] == 'down' :
		value2 += int(lines[x+1])

print('day 2 - part 1', value1*value2)

''' Day 2 - part 2 '''
depth = 0
aim = 0
horizontal = 0

for x in range(len(lines)) :
	if x % 2 == 0 :
		if lines[x] == 'forward' :
			horizontal += int(lines[x+1])
			depth += int(lines[x+1]) * aim
		elif lines[x] == 'down' :
			aim += int(lines[x+1])
		elif lines[x] == 'up' :
			aim -= int(lines[x+1])

print('day 2 - part 2', horizontal*depth)

