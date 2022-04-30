# Assignment 2: Prove: Developer - Solo Submission
# CSE210 - Brother Duane Richards
# Jeremy Johnson

# Tic Tac Toe

# DISPLAY_RULES FUNCTION
# # Print rules: "This is Tic Tac Toe. If you don't know the rules, too bad!"

# DISPLAY_BOARD FUNCTION
# # Loop through the array with lines, dashes, and pluses
# # Starting array:
# # # 1 | 2 | 3 
# # # - + - + -
# # # 4 | 5 | 6
# # # - + - + -
# # # 7 | 8 | 9

# INPUT FUNCTION
# # set variable --> choice
# # Get input: Choose a square, X(1-9)!
# # return choice

# REDRAW FUNCTION (player, choice)
# # choice eq player (within board array)
# # Call DISPLAY_BOARD FUNCTION




# MAIN FUNCTION:
# # 1. Create the Array
# # 2. Display the rules (Call DISPLAY_RULES FUNCTION)
# # 3. Display the board for the first time (Call DISPLAY_BOARD FUNCTION)
# # 4. Set turn variable to 0 and end variable to false
# # 5. IF end eq true
# # # # display "How about a nice game of chess?", end game after input.
# # #  ELSE
# # 6. Start the turns loop (Call TURNS FUNCTION(bool end))
# # # # turn plus-eq 1

# TURNS FUNCTION (turn)
# # 1. Determine player 
# # # IF Turn eq 0 or turn mod 2 eq 0
# # # # THEN player eq X
# # # ELSE
# # # # player eq 0

# # 2. Get user input (Call INPUT FUNCTION(player)) (choice eq user input(player))
# # 3. Determine next steps based on input:::

# # # IF: input IS NOT a number between 1 and 9
# # # # THEN: Display message - "You messed up, and lose a turn."; Go to next player
# # # ELSE:
# # # # IF: User has won the game (Call WINNER FUNCTION(board))
# # # # # THEN: end eq yes

# # # IF: The board results in a draw (Call DRAW FUNCTION(board))
# # # # THEN: end eq yes

# # # ELSE: No winner, no draw, correct input
# # # # THEN: Insert corresponding letter into array, replacing number
# # # #       Call DISPLAY_BOARD FUNCTION(board)
# # # #       return end eq false
# # # 

# WINNER FUNCTION
# # If 


def display_rules():
    print("This is Tic Tac Toe. If you don't know the rules, too bad!")

def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print('- + - + - ')
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print('- + - + - ')
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def winner(board):
    winner = False
    if (board[0] == board[1] == board[2] or board[0] == board[3] == board[6] or board[0] == board[4] == board[8] or
        board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or board[2] == board[4] == board[6] or
        board[3] == board[4] == board[5] or board[6] == board[7] == board[8]):
        winner = True
    else:
        winner = False
    return winner

def cats_game(board):
    test = 0
    cat = False
    for i in range(0,8):
        if ((board[i] != "x") | (board[i] != "o")):
            test +=1
    if(test > 0):
        cat = True
    else:
        cat = False
    return cat

def turn(turn_number, board):
    end = False
    player = "x"
    if (turn_number <=10):
        if ((turn_number == 0) | (turn_number % 2 == 0)):
            player = "x"
            print(player)
        else:
            print(player)
        end = False
    else:
        end = True
    return end

def main():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    display_rules()
    display_board(board)
    turn_number = 0
    end = False
    while end == 0:
        end = turn(turn_number,board)
        turn_number += 1
    else:
        print("How about a nice game of chess?")
        
    
if __name__ == "__main__":
    main()
