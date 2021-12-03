with open('inputD3.txt','r') as f:
	lines = f.read().split()

''' Day 3 - part 1 '''

countCommon1 = 0;
countCommon0 = 0;
gamma = '';
epsilon = '';

for y in range(len(lines[0])) :
	countCommon0 = 0
	countCommon1 = 0
	for x in range(len(lines)) :
		if lines[x][y] == '1' :
			countCommon1 += 1
		else :
			countCommon0 += 1
	if countCommon0 > countCommon1 :
		gamma += '0'
	else :
		gamma += '1'

for x in range(len(gamma)) :
	if gamma[x] == '1' :
		epsilon += '0'
	else :
		epsilon += '1'

gammaConverterd = int(gamma,2)
epsilonConverted = int(epsilon,2)
print('gamma',gammaConverterd)
print('epsilon',epsilonConverted)
print(gammaConverterd *epsilonConverted)