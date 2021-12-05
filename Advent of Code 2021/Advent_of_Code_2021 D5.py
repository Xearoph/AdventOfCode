import numpy as np

with open('inputD5.txt','r') as f:
	lines = f.read().replace(" -> ",",")
	lines = lines.replace("\n",",")
	lines = lines.split(",")

vector2start = np.zeros((int(len(lines)/4),2), dtype=int)
vector2end = np.zeros((int(len(lines)/4),2), dtype=int)

board = np.chararray((10,10),unicode=True)
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

for x in range(int(len(lines)/4)) :

	if board[vector2start[x,0],vector2start[x,1]] == '0' :
		board[vector2start[x,0],vector2start[x,1]] = '1'
	else :
		board[vector2start[x,0],vector2start[x,1]] = '0'

	if board[vector2end[x,0],vector2end[x,1]] == '0' :
		board[vector2end[x,0],vector2end[x,1]] = '1'
	else :
		board[vector2end[x,0],vector2end[x,1]] = '0'

print(board)