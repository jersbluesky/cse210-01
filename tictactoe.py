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
# # # # IF: User has won the game (Call WINNER FUNCTION)
# # # # # THEN: end eq yes

# # # IF: The board results in a draw (Call DRAW FUNCTION)
# # # # THEN: end eq yes

# # # ELSE: No winner, no draw, correct input
# # # # THEN: Insert corresponding letter into array, replacing number
# # # #       Redraw Board (Call REDRAW FUNCTION)
# # # #       return end eq false
# # # 

# WINNER FUNCTION
# # If 

# Define a winning combination
# # Define which player won
# Define a board with no winner




def main():
    board = []
    display_rules()
    display_board()
    turn = 0
    end = False
    if (end == True):
        print("How about a nice game of chess?")
    else:
