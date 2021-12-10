import re
with open('inputD8.txt','r') as f:
	lines = f.read()
	lines = re.split(pattern = r"[\|\n]",string=lines)
	lines = list(map(str,lines))
	lines = list(filter(None, lines))

tenDigits = []
tenDict = {
	'0': '',
	'1': '',
	'2': '',
	'3': '',
	'4': '',
	'5': '',
	'6': '',
	'7': '',
	'8': '',
	'9': ''
} 
fourDigits = []

for x in range(len(lines)) :
	if x % 2 == 0 :
		temp = lines[x].split()
		for y in range(len(temp)) :
			tenDigits.append(temp[y])
	else :
		temp = lines[x].split()
		for y in range(len(temp)) :
				fourDigits.append(temp[y])


count = 0

for x in range(len(tenDigits)) :
	if len(tenDigits[x]) == 2 :
		tenDict["1"] = tenDigits[x]
	elif len(tenDigits[x]) == 3 :
		tenDict["7"] = tenDigits[x]
	elif len(tenDigits[x]) == 7 :
		tenDict["8"] = tenDigits[x]
	elif len(tenDigits[x]) == 4 :
		tenDict["4"] = tenDigits[x]


# 4+7 = bijna 9

print(tenDict)

