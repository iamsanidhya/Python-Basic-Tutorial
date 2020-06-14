#----------Global Variable------------

#game board
board = ["-", "-", "-", 
        "-", "-", "-",
        "-", "-", "-",]
#game_is_still_going
game_is_still_going = True
#Who won? or tie?
winner = None

# whose turn is it?
current_player = "X"



def play_game():
	display_board()
	#game is still going
	while game_is_still_going:

		#handle a single turn of an arbitrary player
		handle_turn(current_player)

		#check if the game is over
		check_if_game_over()

		#flip to the other player
		flip_player()
		#The game has ended
	if winner == "X" or winner == "O":
		print(winner + " won.")
	elif winner == None:
		print("Tie.")



def display_board():
	print("\n")
	print(board[0] + " | " + board[1] + " | " + board[2])
	print(board[3] + " | " + board[4] + " | " + board[5])  
	print(board[6] + " | " + board[7] + " | " + board[8])
	print("\n")



def handle_turn(player):

  # Get position from player
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  # Whatever the user inputs, make sure it is a valid input, and the spot is open
  valid = False
  while not valid:

    # Make sure the input is valid
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
 
    # Get correct index in our board list
    position = int(position) - 1

    # Then also make sure the spot is available on the board
    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")

  # Put the game piece on the board
  board[position] = player
  display_board()
def check_if_game_over():
	check_if_win()
	check_if_tie()


def check_if_win():

	global winner
	row_winner = check_rows()
	column_winner = check_columns()
	diagonal_winner = check_diagonals()
	if row_winner:
		winner = row_winner
	elif column_winner:
		winner = column_winner
	elif diagonal_winner:
		winner = diagonal_winner
	else:
		winner = None
		

def check_rows():
	global game_is_still_going
	row_1 = board[0] == board[1] == board[2] != "-"
	row_2 = board[3] == board[4] == board[5] != "-"
	row_3 = board[6] == board[7] == board[8] != "-"
	if row_1 or row_2 or row_3:
		game_is_still_going = False
	if row_1:
	   return board[0]
	elif row_2:
	   return board[3]
	elif row_3:
	   return board[6]
	else:
		return None

def check_columns():
	global game_is_still_going
	column_1 = board[0] == board[3] == board[6] != "-"
	column_2 = board[1] == board[4] == board[7] != "-"
	column_3 = board[2] == board[5] == board[8] != "-"
	if column_1 or column_2 or column_3:
		game_is_still_going = False
	if column_1:
	   return board[0]
	elif column_2:
	   return board[1]
	elif column_3:
	   return board[2]
	else:
		return None
 
def check_diagonals():
	global game_is_still_going
	diagonal_1 = board[0] == board[4] == board[8] != "-"
	diagonal_2 = board[6] == board[4] == board[2] != "-"
	if diagonal_1 or diagonal_2:
		game_is_still_going = False
	if diagonal_1:
	   return board[0]
	elif diagonal_2:
	   return board[6]
	else:
		return None

def check_if_tie():
	global game_is_still_going
	if "-" not in board:
		game_is_still_going = False
		return True
	else:
	    return False	

def flip_player():
	global current_player
	if current_player == "X":
		current_player = "O"
	elif current_player == "O":
	     current_player = "X"	
	return	

play_game()