with open('inputD4.txt','r') as f:
	lines = f.read().split()

''' Day 4 - part 1 '''

bingoNumbers = lines[0].split(',')
#boards = lines.split()


print(len(lines[0]))
stop = False
lastNumber = 0

global boardsDone
boardsDone = [False] * 100

def CheckWin(_boardNumber) :
	global stop

	global winningNumber
	winningNumber = ['','','','','']
	winningBoard = 0
	try : 
		winningBoard = _boardNumber
		for row in range(0,5) :
			for index in range(1,6) :
				if stop == False :
					if lines[index + (row * 5) + (_boardNumber * 25)][0] != 'a' :
						winningNumber = ['','','','','']
						break
					winningNumber[index-1] = lines[index + (row * 5) + (_boardNumber * 25)]
					if index == 5 :
						boardsDone[_boardNumber] = True
						print('horizontal bingo')
						break
	except : 
		print()
	
	
	if stop == False :
		winningNumber = ['','','','','']
		try : 
			winningBoard = _boardNumber

			for row in range(0,5) :
				tempX = row + _boardNumber * 25 + 1
				for index in range(1,6) :
					if stop == False :
						if lines[tempX][0] != 'a' :
							winningNumber = ['','','','','']
							break

						winningNumber[index-1] = lines[tempX]
						tempX+=5
						if index == 5 :
							boardsDone[_boardNumber] = True
							print('vertical bingo')
							break
		except : 
			print()

	winningBoardNumbers = 0

	total = 0
	for x in range(len(boardsDone)) :
		if boardsDone[x] == True :
			total+=1
	if total == totalBoards :
		stop = True

	if stop == True :
		print('winningBoard',winningBoard)
		print('lines',lines[winningBoard*25 +1])
		for nnn in range(25) :
		
			tnum = lines[winningBoard * 25 + 1 + nnn]
			#print(tnum)
			if tnum[0] != 'a' :
				winningBoardNumbers += int(tnum)
				print(lines[winningBoard * 25 + 1 + nnn])

		print('lastNumber',lastNumber)
		print('winningBoardNumbers',winningBoardNumbers)
		print(int(winningBoardNumbers) * int(lastNumber))

for bnum in range(len(bingoNumbers)) :
	totalBoards = int(len(lines)-1) / 25
	test=13
#try : 
	for board in range(int(totalBoards)) : 
		if boardsDone[board] == True :
			continue
		if stop == True : 
			break
		for row in range(0,5) :
			if stop == True : 
				break
			for index in range(1,6) :
				#print(index + (row * 5) + (board * 25))
				boardPos = index + (row * 5) + (board * 25)
				lastNumber = bingoNumbers[bnum]
				if lines[boardPos] == bingoNumbers[bnum] :
					lines[boardPos] = 'a' + lines[boardPos]
		CheckWin(board)
		print()
#except : 
	print('no more boards')
