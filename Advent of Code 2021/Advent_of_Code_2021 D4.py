with open('inputD4.txt','r') as f:
	lines = f.read().split()

''' Day 4 - part 1 '''

bingoNumbers = lines[0].split(',')
#boards = lines.split()


print(len(lines[0]))
stop = False
lastNumber = 0

def CheckWin() :
	global stop

	global winningNumber
	winningNumber = ['','','','','']
	winningBoard = 0
	try : 
		for boardt in range(10000) : 
			if stop == True :
				break
			winningBoard = boardt
			for row in range(0,5) :
				for index in range(1,6) :
					if stop == False :
						if lines[index + (row * 5) + (boardt * 25)][0] != 'a' :
							winningNumber = ['','','','','']
							break
						winningNumber[index-1] = lines[index + (row * 5) + (boardt * 25)]
						if index == 5 :
							print('horizontal bingo')
							stop = True
							break
	except : 
		print()
	
	
	if stop == False :
		winningNumber = ['','','','','']
		try : 
			for boardd in range(10000) : 
				if stop == True :
					break
				winningBoard = boardd

				for row in range(0,5) :
					tempX = row + boardd * 25 + 1
					for index in range(1,6) :
						if stop == False :
							if lines[tempX][0] != 'a' :
								winningNumber = ['','','','','']
								break

							winningNumber[index-1] = lines[tempX]
							tempX+=5
							if index == 5 :
								print('vertical bingo')
								stop = True
								break
		except : 
			print()

	winningBoardNumbers = 0



	if stop == True :
		print('winningNumber',winningNumber)
		print('winningBoard',winningBoard)
		print('lines',lines[winningBoard*25 +1])
		for nnn in range(25) :
		
			tnum = lines[winningBoard * 25 + 1 + nnn]
			#print(tnum)
			if tnum[0] != 'a' :
				winningBoardNumbers += int(tnum)
				print(lines[winningBoard * 25 + 1 + nnn])

		print('lastNumber',winningBoardNumbers)
		print(int(winningBoardNumbers) * int(lastNumber))


for bnum in range(len(bingoNumbers)) :
	totalBoards = int(len(lines)-1) / 25
	
	test=13
	try : 
		for board in range(30000) : 
			
			if stop == True : 
				break
			print('------- board ',board)
			for row in range(0,5) :
				if stop == True : 
					break
				for index in range(1,6) :
					#print(index + (row * 5) + (board * 25))
					boardPos = index + (row * 5) + (board * 25)
					lastNumber = bingoNumbers[bnum]
					if lines[boardPos] == bingoNumbers[bnum] :
						lines[boardPos] = 'a' + lines[boardPos]
					print(lines[boardPos],' ', end='')
				print('')
			print('-------')
			print('no more boards')
			print(totalBoards)
			if board != 0 :
				test = int(board+1) % int(totalBoards)
			else :
				test = 10123
			if test == 0 :
				CheckWin()
				print()
	except : 
		print('no more boards')

