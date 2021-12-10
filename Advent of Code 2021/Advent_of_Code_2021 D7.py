with open('inputD7.txt','r') as f:
	lines = f.read().split(",")

lines = list(map(int, lines))
fuelCost = 9999999999999999999999
fuelTemp = 0
count = 0
print(max(lines))
for x in range(max(lines)) :
	print(x)
	count = 0
	for y in range(len(lines)) :
		fuelOnce = 0
		if x != lines[y]:
			if x > lines[y]:
				fuelDist = x - lines[y]
				for z in range(fuelDist +1) :
					fuelTemp += z
					fuelOnce += z
					count += z
				#print('from ', lines[y],' to ',x, ' costs' , fuelOnce, ' progress ', fuelTemp)

			else :				
				fuelDist = lines[y] - x
				for z in range(fuelDist +1) :
					fuelTemp += z
					fuelOnce += z
					count += z
				#print('from ', lines[y] ,' to ',x, ' costs' , fuelOnce , ' progress ', fuelTemp)

	#print('with a total of ', count)
		

	if fuelTemp < fuelCost : 
		fuelCost = fuelTemp

	fuelTemp = 0

print(fuelCost)
