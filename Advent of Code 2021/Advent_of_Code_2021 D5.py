import numpy as np

with open('inputD5.txt','r') as f:
	lines = f.read().replace(" -> ",",")
	lines = lines.replace("\n",",")
	lines = lines.split(",")

boardSize = 5000
vector2start = np.zeros((boardSize,2), dtype=int)
vector2end = np.zeros((boardSize,2), dtype=int)

board = np.chararray((boardSize,boardSize),unicode=True)
board[:] = '.'

i = 0
j = 2

for x in range(int(len(lines)/4)) :
	for y in range(2) :
		vector2start[x,y] = lines[i]
		i+=1
		vector2end[x,y] = lines[j]
		j+=1
		
	i+=2
	j+=2


markFields = []

for x in range(len(vector2start)) :
	firstX = vector2start[x][0]
	firstY = vector2start[x][1]

	lastX = vector2end[x][0]
	lastY = vector2end[x][1]
	
	# als de eerste x waarde lager is dan de tweede en de y waardes zijn gelijk
	if firstX < lastX and firstY == lastY :
		lineCounter = lastX - firstX
		for x in range(lineCounter+1) :
			markFields.append([firstX+x,lastY])

	# als de eerste x waarde groter is dan de tweede en de y waardes zijn gelijk
	if firstX > lastX and firstY == lastY :
		lineCounter = firstX - lastX 
		for x in range(lineCounter+1) :
			markFields.append([firstX-x,lastY])

	# als de eerste x waarde kleiner is dan de tweede en de x waardes zijn gelijk
	if firstX == lastX and firstY > lastY :
		lineCounter = firstY - lastY
		for x in range(lineCounter+1) :
			markFields.append([firstX,lastY+x])
	
	# als de eerste x waarde kleiner is dan de tweede en de x waardes zijn gelijk
	if firstX == lastX and firstY < lastY :
		lineCounter =  lastY - firstY
		for x in range(lineCounter+1) :
			markFields.append([firstX,lastY-x])
	
	# als de eerste x waarde kleiner is dan de tweede en de x waardes zijn gelijk
	if firstX < lastX and firstY < lastY :
		lineCounter = lastY - firstY
		for x in range(lineCounter+1) :
			markFields.append([firstX+x,lastY-x])
	
	# als de eerste x waarde kleiner is dan de tweede en de x waardes zijn gelijk
	if firstX > lastX and firstY > lastY :
		lineCounter = firstY - lastY
		for x in range(lineCounter+1) :
			markFields.append([firstX-x,firstY-x])
	
	# als de eerste x waarde kleiner is dan de tweede en de x waardes zijn gelijk
	if firstX > lastX and firstY < lastY :
		lineCounter = lastY - lastX
		for x in range(lineCounter+1) :
			markFields.append([firstX-x,lastY-x])
	
	# als de eerste x waarde kleiner is dan de tweede en de x waardes zijn gelijk
	if firstX < lastX and firstY > lastY :
		lineCounter = firstX - lastY
		for x in range(lineCounter+1) :
			markFields.append([firstX+x,firstY-x])

	


twoos = 0
for x in range(int(len(markFields))) :
		spot = board[markFields[x][1],markFields[x][0]]
		if spot == '.' :
			board[markFields[x][1],markFields[x][0]] = '1'
		elif spot == '1' :
			board[markFields[x][1],markFields[x][0]] = '2'
			twoos+=1
		elif spot == '2' :
			board[markFields[x][1],markFields[x][0]] = '3'
		elif spot == '3' :
			board[markFields[x][1],markFields[x][0]] = '4'
		elif spot == '4' :
			board[markFields[x][1],markFields[x][0]] = '5'
print(board)
print(twoos)
