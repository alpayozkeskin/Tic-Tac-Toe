import math

def initialize():
	tour = 3
	scoreP, scoreAi = 0, 0
	size = int(raw_input("Please enter the size of the board: "))
	for i in range(tour):
		print "Tour ",
		print i + 1
		board = []
		gameEnded = False
		for i in range(size):
			subBoard = [' '] * size
			board.append(subBoard)
		printBoard(board)
		counter = 0
		while not gameEnded :
			print "It's your turn"
			board = makeMovePlayer(board)
			counter += 1
			if counter == len(board) * len(board[0]):
				print "Tied!"
				break
			score, hScoreP, vScoreP, dScoreP = countScore(board, 'X')
			if score <= - math.pow(10, size) :
				scoreP += 1
				print "The player wins this round"
				break
			print "It's Ai's turn"
			score, hScoreAi, vScoreAi, dScoreAi = countScore(board, 'O')
			x, y = aiMove(board, hScoreAi, vScoreAi, dScoreAi,hScoreP, vScoreP, dScoreP)
			board = makeMoveAi(board, x, y)
			counter += 1
			score, hScoreAi, vScoreAi, dScoreAi = countScore(board, 'O')
			if score >= math.pow(10, size) :
				scoreAi += 1
				print "The Ai wins this round"
				break
			
			
def printBoard(board):
	rows = len(board)
	cols = len(board[0])
	for row in range(rows):
		for col in range(cols):
			print board[row][col],
			if(col != cols - 1):
				print " | ",
			else:
				print ""

def makeMovePlayer(board):
	x = int(raw_input("Please enter the row of X: "))
	y = int(raw_input("Please enter the column of X: "))
	board[x][y] = 'X'
	printBoard(board)
	return board

def makeMoveAi(board, x, y):
	board[x][y] = 'O'
	printBoard(board)
	return board

def countScore(board, player):
	horizontalC, verticalC = 0, 0
	diagonalC, rDiagonalC = 0, 0
	hScore, vScore, dScore = [], [], []
	totalScore = 0
	rows = len(board)
	cols = len(board[0])
	for row in range(rows):
		for col in range(cols):
			if board[row][col] == player:
				horizontalC += 1
				if row == col :
					diagonalC += 1
				if row + col == rows - 1:
					rDiagonalC += 1
			if board[col][row] == player:
				verticalC += 1
		hScore.append(math.pow(10, horizontalC))
		vScore.append(math.pow(10, verticalC))
		if player == 'X':
			totalScore -= hScore[row] + vScore[row]
		else :
			totalScore += hScore[row] + vScore[row]
		horizontalC, verticalC = 0, 0
	dScore.append(math.pow(10, diagonalC))
	dScore.append(math.pow(10, rDiagonalC))
	if player == 'X':
		totalScore -= dScore[0] + dScore[1]
	else :
		totalScore += dScore[0] + dScore[1]
	return totalScore, hScore, vScore, dScore 

def aiMove(board, hScoreAi, vScoreAi, dScoreAi,hScoreP, vScoreP, dScoreP):
	hScore = merge(hScoreP, hScoreAi)
	vScore = merge(vScoreP, vScoreAi)
	dScore = merge(dScoreP, dScoreAi)
	playerScoreList = hScoreP + vScoreP + dScoreP
	aiScoreList = hScoreAi + vScoreAi +dScoreAi
	scoreList = hScore + vScore + dScore
	highest, indexh, lowest, indexl, indexCounter = float("-inf"), 0, float("inf"), 0, 0
	for i, score in reversed(list(enumerate(scoreList))) :
		if score > highest :
			highest = score
			indexh = i
		if score < lowest :
			lowest = score
			indexl = i
	if lowest <= - math.pow(10, len(board) - 1) +1:
		x, y = chooseTile(board, indexl, len(scoreList))
		if x != -1:
			return x, y
	else :
		if(aiScoreList[indexh] == 1.0):
			x, y = chooseTile(board, indexh, len(scoreList))
			if x != -1:
				return x, y
	while len(aiScoreList) > 0:
		highest = 0
		for i, score in reversed(list(enumerate(aiScoreList))) :
			if score > highest :
				highest = score
				indexh = i
		if playerScoreList[indexh] == 1.0:
	 		x, y = chooseTile(board, indexh, len(playerScoreList))
			if x != -1:
				return x, y
		aiScoreList.pop(indexh)

	rows = len(board)
	cols = len(board[0])
	for row in range(rows):
		for col in range(cols):
			if board[row][col] == ' ':
				return row, col
def merge(player, ai):
	return [ x - y for x, y in zip(player, ai)]

def chooseTile(board, index, length):
	if index == length - 2 :
		for i in range(len(board)):
			if board[i][i] == ' ':
				return i, i
	elif index == length - 1 :
		for i in range(len(board)):
			if board[len(board) - 1 - i][i] == ' ':
				return len(board) - 1 - i, i
	elif index < len(board) :
		for i in range(len(board)):
			if board[index][i] == ' ':
				return index, i
	elif index < len(board) * 2  :
		for i in range(len(board)):
			if board[i][index - len(board)] == ' ':
				return i, index - len(board)
	return -1, -1

initialize()