"""
Find all possible moves in a Double-X Game.

Game rules: Two players begin with an empty set of dashes, like "-----". Players alternate adding adjacent double X's, "XX", to the board until there are no more legal moves. The last player to place double X's wins.

Example game sequences:

-------			-------
-XX----			-----XX
-XXXX--			XX---XX	
-XXXXXX			XX-XXXX

"""

def start(length):
	allStates, nextMoves = {}, {}
	allStates[0] = [genBoard(length)]
	
	for i in range(1, (length+1)/2):
		allStates[i] = []
		for board in allStates[i-1]:
			legalMoves = nextStates(board)
			allStates[i].extend(legalMoves)
			if board not in nextMoves:
				nextMoves[board] = legalMoves
				
	print 'allStates: ', allStates
	print 'nextMoves: ', nextMoves
	return allStates, nextMoves
	
def genBoard(length):
	newBoard = ''
	for i in range(length):
		newBoard = newBoard + '-'
	return newBoard

def nextStates(board):
    states = []
    for i in range(len(board)-2):
        if validMove(board, i):
            states.append(commitMove(board, i))
    return states

def validMove(board, index):
	if board[index] == '-' and board[index+1] == '-':
		return True
	else:
		return False

def commitMove(board, index):
	return board[:index] + 'XX' + board[index+2:]

start(7)

# validMove and commitMove are simple enough that they do not need to be abstracted but I wanted to demonstrate my ability to abstract operations in a complex program.