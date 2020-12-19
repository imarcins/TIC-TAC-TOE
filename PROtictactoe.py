player = "X"
board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]

def print_board():
    print ("  A B C")
    print("1 " + board[0][0] + "|" + board[0][1] + "|"+   board[0][2])
    print("  -----  ")
    print("2 " + board[1][0] + "|" + board[1][1] + "|"+   board[1][2])
    print("  -----  ")
    print("3 " + board[2][0] + "|" + board[2][1] + "|"+   board[2][2])


def change_turns():
    global player
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"

# marking the players inputted coordinates onto the board 
def mark():
    #change_turns()
    is_input_correct = False
    while not is_input_correct:
        choice = tuple(input("Player " + player + " Please enter the coordinates 1. Column (a-c), 2. Row (1-3): "))

        if choice == ("a", "1"):
            if board[0][0] == ".":
                board[0][0] = player
                print("Your coordinates %s have been placed" %str(choice))
                is_input_correct = True
            else:
                print("This spot is taken!")
            
        elif choice == ("a", "2"):
            if board[1][0] == ".":
                board[1][0] = player
                print("Your coordinates %s have been placed" %str(choice))
                is_input_correct = True
            else:
                print("This spot is taken!")

        elif choice == ("a", "3"):
            if board[2][0] == ".":
                board[2][0] = player
                print("Your coordinates %s have been placed" %str(choice))
                is_input_correct = True
            else:
                print("This spot is taken!")


        elif choice == ("b", "1"):
            if board[0][1] == ".":
                board[0][1] = player
                print("Your coordinates %s have been placed" %str(choice))
                is_input_correct = True
            else:
                print("This spot is taken!")

        elif choice == ("b", "2"):
            if board[1][1] == ".":
                board[1][1] = player
                print("Your coordinates %s have been placed" %str(choice))
                is_input_correct = True
            else:
                print("This spot is taken!")

        elif choice == ("b", "3"):
            if board[2][1] == ".":
                board[2][1] = player
                print("Your coordinates %s have been placed" %str(choice))
                is_input_correct = True
            else:
                print("This spot is taken!")
        elif choice == ("c", "1"):
            if board[0][2] == ".":
                board[0][2] = player
                print("Your coordinates %s have been placed" %str(choice))
                is_input_correct = True
            else:
                print("This spot is taken!")

        elif choice == ("c", "2"):
            if board[1][2] == ".":
                board[1][2] = player
                print("Your coordinates %s have been placed" %str(choice))
                is_input_correct = True
            else:
                print("This spot is taken!")

        elif choice == ("c", "3"):
            if board[2][2] == ".":
                board[2][2] = player
                print("Your coordinates %s have been placed" %str(choice))
                is_input_correct = True
            else:
                print("This spot is taken!")
        else:
            print ("Out of bounds!")
  
    

def has_won():

    if board[0][0] == board[1][0] == board[2][0] != ".":
       print("Game over! " + board[1][0] + " wins")
       return True
       
    elif board[0][1] == board[1][1] == board[2][1] != ".":
        print("Game over! " + board[1][1] + " wins")
        return True

    elif board[0][2] == board[1][2] == board [2][2] != ".":
        print("Game over! " + board[1][2] + " wins")
        return True
        
    elif board[0][0] == board[1][1] == board[2][2] != ".":
        print("Game over! " + board[1][1] + " wins")
        return True
    elif board[0][2] == board[1][1] == board[2][0] != ".":
        print("Game over! " + board[1][1] + " wins")
        return True
    elif board[0][0] == board [0][1] == board [0][2] != ".":
        print("Game over! " + board[0][1] + " wins")
        return True

    elif board[1][0] == board [1][1] == board [1][2] != ".":
        print("Game over! " + board[1][1] + " wins")
        return True
    elif board[2][0] == board [2][1] == board [2][2] != ".":
        print("Game over! " + board[2][1] + "  wins")
        return True
    else:
        return False
    
    
        
def is_full():

    for row in board:
        for cell in row:
            if cell == ".":
                return False
   
    return True


def tictactoe_game():
    
    print("Welcome to Tic tac toe!")
    while not has_won() and not is_full():   
    
        print_board()
        mark()
        change_turns()
        
        if is_full():
            print("Tie Game!")


    else:
        print_board()
        print("Thank you for playing")
        
            

#asking the player if he wants to play again. If so clear the board. 
#even though player X or O won after 9 turns it still shows up as a tie game. 
            
    


        
tictactoe_game()


