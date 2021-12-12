import re
with open('inputD8.txt','r') as f:
	lines = f.read()
	lines = re.split(pattern = r"[\|\n]",string=lines)
	lines = list(map(str,lines))
	lines = list(filter(None, lines))

tenDigits = []
tenDict = {
	'0': '000000',
	'1': '00',
	'2': '00000',
	'3': '00000',
	'4': '0000',
	'5': '00000',
	'6': '000000',
	'7': '000',
	'8': '0000000',
	'9': '000000'
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

def AddToNine(_number) :
	for x in range(len(_number)) :
		contains = False
		for y in range(len(tenDict["9"])) :
			if _number[x] == tenDict["9"][y] :
				contains = True
		if contains == False :
			
			for y in range(len(tenDict["9"])) :
				if not tenDict["9"][y] == 0:
					tenDict["9"] = tenDict["9"][1:]
					tenDict["9"] += _number[x]
					break
				elif tenDict["9"][y] != _number[x] :
					tenDict["9"] += _number[x]
					break

count = 0

for x in range(len(tenDigits)) :
	if len(tenDigits[x]) == 2 :
		tenDict["1"] = tenDigits[x]
	elif len(tenDigits[x]) == 3 :
		tenDict["7"] = tenDigits[x]
		AddToNine(tenDigits[x])
	elif len(tenDigits[x]) == 7 :
		tenDict["8"] = tenDigits[x]
	elif len(tenDigits[x]) == 4 :
		tenDict["4"] = tenDigits[x]
		AddToNine(tenDigits[x])

# 4+7 = bijna 9

print(tenDict)
print(tenDict["9"])

