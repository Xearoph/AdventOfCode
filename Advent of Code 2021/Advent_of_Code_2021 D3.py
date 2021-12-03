import copy
with open('inputD3.txt','r') as f:
	lines = lines2 = f.read().split()

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
print('D3P1',gammaConverterd *epsilonConverted)

''' Day 3 - part 1 '''

countCommon1 = 0;
countCommon0 = 0;
gamma = '';
epsilon = '';

def func(_lines,_invert) :

	for y in range(len(_lines[0])) :
		countCommon0 = 0
		countCommon1 = 0
		for x in range(len(_lines)) :
			if _lines[x][y] == '1' :
				countCommon1 += 1
			else :
				countCommon0 += 1

		p = 0
		charCheck = ''
		loopCount = len(_lines)

		if countCommon0 > countCommon1 :
			charCheck = '0'
		else : 
			charCheck = '1'
		while p < loopCount :
			if len(_lines) == 1 :
				break
			if _invert is True:
				if _lines[p][y] != charCheck :
					_lines.pop(p)
					p-=1
					loopCount-=1
				p+=1
			else :
				if _lines[p][y] == charCheck :
					_lines.pop(p)
					p-=1
					loopCount-=1
				p+=1

	print(_lines[0],' decimal value: ',int(_lines[0],2))
	return int(_lines[0],2)

value1 = func(copy.copy(lines),False)

value2 = func(copy.copy(lines),True)

print(value1*value2)

