with open('inputD3.txt','r') as f:
	lines = f.read().split()

''' Day 3 - part 1 '''

countCommon1 = 0;
countCommon0 = 0;

for x in range(len(lines[x])) :
	for y in range(len(lines)) :
		if lines[y][x] == '1' :
			countCommon1 += 1
		else :
			countCommon0 += 1

print('1',countCommon1)
print('0',countCommon0)
