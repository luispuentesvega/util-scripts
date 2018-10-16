a=1
b=2
c=1

board = ["*"] * 9
if a==b==c:
	print("They are alike")
else:
	print("They are different")
	
def has_won(board):
	print("Has won!")
	#horizontal
	return board[0]==board[1]==board[2] 
		or board[3]==board[4]==board[5]
		
has_won(board)