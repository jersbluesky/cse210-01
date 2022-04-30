# Assignment 2: Prove: Developer - Solo Submission
# CSE210 - Brother Duane Richards
# Jeremy Johnson
# Tic Tac Toe

# This is a place to display the rules. They're easy, so have some sarcasm. :P
def display_rules():
    print("This is Tic Tac Toe. If you don't know the rules, too bad!")

# Feel's like a cheater's way to display the board, but we're hard-coding today. 
def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print('- + - + - ')
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print('- + - + - ')
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

# If the following spots on the array are the same, than the person wins. Very complicated game.
def winner(board):
    if (board[0] == board[1] == board[2] or board[0] == board[3] == board[6] or board[0] == board[4] == board[8] or
        board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or board[2] == board[4] == board[6] or
        board[3] == board[4] == board[5] or board[6] == board[7] == board[8]):
        winner = True
    else:
        winner = False
    return winner

# I always called a 'draw' a cat's game. I don't know why. This function
# tests if there are any values other than x or o, and if there are, it's
# not a cat's game. It takes the board as a parameter to the function. It
# returns a boolean for the 'turn' function later on.
def cats_game(board):
    test = 0
    for i in range(0,8):
        if ((board[i] != "x") & (board[i] != "o")):
            test +=1
    if(test > 0):
        cat = False
    else:
        cat = True
    return cat

# This is likely a bit more complex than it needs to be, but it works. It is embedded in the
# main function as a function that returns whether or not to end the game, but it keeps
# looping through and calling the other functions. 
def turn(turn_number, board):
    # This just determines who's turn it is, based on the remainder (modular variable) of the 
    # turn, which is increased and passed to the function from main.
    if ((turn_number == 0) | (turn_number % 2 == 0)):
        player = "x"
    else:
        player = "o"
    # This is a simple code to get the square number from the user.
    choice = int(input(f'Choose a square, {player}, between 1 and 9! '))
    # 
    print("")
    # If the user is putting in a value that is not in range, or has a value already
    # in it, then they get a sarcastic error and lose their turn.
    if ((choice > 9) | (choice < 1) | (board[choice - 1] == "x") | (board[choice - 1] == "o")):
        print("You loose your turn, Jack! In your defense, these rules are super hard.\n")
        end = False
        # The board is still displayed for convenience.
        display_board(board)
        return end
    # If we made it this far and the number chosen is legit, we put the player's
    # name (x or o) into the array (minus one, because it starts at zero).
    board[choice - 1] = player
    display_board(board)
    # We need to determine the winner, and figure out what to do if there is one.
    # If there is one, they are declared champion and we get out of the 'while' loop
    # called in the main function.
    is_win = winner(board)
    if (is_win == True):
        print(f'{player} is the champion. The other person is a loser.')
        end = True
        return end
    else:
        print("")
    # If it's a cat's game, then it's declared, and we leave the while loop.
    is_cat = cats_game(board)
    if is_cat == True:
        print(f'Cat\'s Game, whatever that means, right?')
        end = True
    else:
        print("")
        end = False
    return end

def main():
    # Oof. A hard-coded array. I'll do better next time. 
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    display_rules()
    display_board(board)
    # Because the loop below is a while loop, we're declaring the first turn number
    # and the end to be False. It's like a do-while loop. 
    turn_number = 0
    end = False
    while end == False:
        end = turn(turn_number, board)
        turn_number += 1
    # I'm sorry for my sarcasm. I can't always hold it back.
    else:
        chess = input("How about a nice game of chess? ")
        print(f'{chess} is your answer, eh? I\'m too tired. Go play TNW with Matthew Broderick.\n\nBye-a!')
        
if __name__ == "__main__":
    main()
    
