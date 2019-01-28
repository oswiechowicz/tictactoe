# Ollie Swiechowicz
# CS-UY 1114
# Final project
# Due December 10th, 2018 at 11:55pm

import turtle
import time
import random

# This list represents the board. It's a list
# of nine strings, each of which is either
# "X", "O", "_", representing, respectively,
# a position occupied by an X, by an O, and
# an unoccupied position. The first three
# elements in the list represent the first row,
# and so on. Initially, all positions are
# unoccupied.
the_board = [ "_", "_", "_",
              "_", "_", "_",
              "_", "_", "_"]

#COORDINATES OF SQUARES (going across rows and down columns):
S0 = [0, 160]
S1 = [80, 160.0]
S2 = [160, 160]
S3 = [0, 80] #2nd row
S4 = [80, 80]
S5 = [160, 80]
S6 = [0, 0] #3rd row
S7 = [80, 0]
S8 = [160, 0]
board_coord = [S0, S1, S2, S3, S4, S5, S6, S7, S8]
#board_coord has list of coords, format list( list (int,int) )

#FUNCTIONS BEGIN
############################################################
def husk_board():
    #sig: None -> None
    #Draws empty tic tac toe board
    turtle.up()
    turtle.setheading(0)
    turtle.goto(-40,-40)
    turtle.down()
    turtle.forward(240)
    turtle.left(90)
    turtle.forward(240)
    turtle.left(90)
    turtle.forward(240)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(240)
    turtle.right(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(240)
    turtle.left(90)
    turtle.goto(-40,-40)
    turtle.left(180)
    turtle.forward(160)
    turtle.up()
    turtle.goto(40,-40)
    turtle.down()
    turtle.forward(240)
    turtle.right(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(240)

def draw_board(board):
    """
    sig: list(str) -> NoneType
    Given the current state of the game, draws
    the board on the screen, including the
    lines and the X and O pieces at the position
    indicated by the parameter.
    Hint: Write this function first!
    """
    turtle.clear()
    turtle.hideturtle()
    turtle.goto(0,0)
    husk_board()

    for i in range(9):
        if the_board[i] == "X":
            coord_set = board_coord[i] 
            x_coord = coord_set[0]
            y_coord = coord_set[1]
            turtle.penup()
            turtle.goto(x_coord, y_coord)
            turtle.pendown()
            drawX()
            turtle.penup()

        elif the_board[i] == "O":
            coord_set = board_coord[i] 
            x_coord = coord_set[0] 
            y_coord = coord_set[1] - 35
            turtle.penup()
            turtle.goto(x_coord, y_coord) 
            drawO()
            turtle.penup()


    turtle.update()

def drawX():
    """
    sig: None -> None
    draws an X on the board; called in draw_board function
    """
    turtle.pendown()
    turtle.setheading(180) #makes sure turtle points in the 180 direction (down)
    turtle.pencolor('red') 
    turtle.left(45)
    turtle.forward(40)
    turtle.left(180)
    turtle.forward(80)
    turtle.left(180)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(180)
    turtle.forward(80)
    turtle.penup()
    turtle.pencolor('black')
    
def drawO():
    """
    sig: None -> None
    Draws an o on the board; it is used in draw_board function
    """
    turtle.pendown()
    turtle.pencolor('blue')
    turtle.setheading(360)
    turtle.circle(35)
    turtle.penup()
    turtle.pencolor('black')

def message(outcome): #handles all situations
    #sig: str -> None
    if outcome == "win":
        turtle.tracer()
        turtle.color('blue')
        turtle.goto(-80, 200)
        turtle.write ('GAME OVER: You win!', font = ('Times New Roman', 30, 'bold'))
    elif outcome == "loss":
        turtle.tracer()
        turtle.color('red')
        turtle.goto(-80, 200)
        turtle.write ('GAME OVER: You lose.', font = ('Times New Roman', 30, 'bold'))
    else: #stalemate
        turtle.tracer()
        turtle.color('gray')
        turtle.goto(-80, 200)
        turtle.write ('GAME OVER: Stalemate.', font = ('Times New Roman', 30, 'bold'))

def do_user_move(board, x, y):
    """
    sig: list(str), int, int -> bool
    Given a list representing the state of the board
    and an x,y screen coordinate pair indicating where
    the user clicked, update the board
    with an O in the corresponding position. Your
    code will need to translate the screen coordinate
    (a pixel position where the user clicked) into the
    corresponding board position (a value between 0 and
    8 inclusive, identifying one of the 9 board positions).
    The function returns a bool indicated if
    the operation was successful: if the user
    clicks on a position that is already occupied
    or outside of the board area, the move is
    invalid, and the function should return False,
    otherise True.
    """
    #print("user clicked at "+str(x)+","+str(y))
    row = 0
    column = 0
    valid = True
  
    if ( x < 40 ): #gather x coordinate
        column = 0
    elif (x > 40) and (x < 120):
        column = 1
    elif (x > 120) and (x < 200):
        column = 2
    else:
        valid = False

    if ( y < 200 ) and (y > 120): #gather y coordinate
        row = 0
    elif (y < 120) and (y > 40):
        row = 1
    elif (y < 40) and (y > -40):
        row = 2
    else:
        valid = False
    
    #use row/col to find index
    indexformula = (3 * row) + column

    for i in range(0, len(the_board)):
            if the_board[indexformula] != "_":
                valid = False
            elif the_board[indexformula] == "_":
                valid = True
                the_board[indexformula] = "O"
                break

    return valid

def check_game_over(board): 
    """
    sig: list(str) -> bool
    Given the current state of the board, determine
    if the game is over, by checking for
    a three-in-a-row pattern in horizontal,
    vertical, or diagonal lines; and also if the
    game has reached a stalemate, achieved when
    the board is full and no further move is possible.
    If there is a winner or if there is a stalemate, display
    an appropriate message to the user and clear the board
    in preparation for the next round. If the game is over,
    return True, otherwise False.
    """
    winninglst = [ [0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7],  [2,5,8], [0,4,8], [2,4,6] ] #finish list of winning possibilities
    gameover = False
    win = False
    loss = False
    for aset in winninglst:
        if (the_board[aset[0]] == the_board[aset[1]] == the_board[aset[2]]) and (the_board[aset[0]] != "_"):
            gameover = True
            if the_board[aset[0]] == "X":
                loss = True
                message('loss')
            elif the_board[aset[0]] == "O":
                win = True
                message('win')
            break
        else:
            gameover = False
    

    takenspots = 0
    for i in range(9): #iterates board and checks for stalemate
        if (the_board[i] == "X") or (the_board[i] == "O"):
            takenspots += 1
    
    if (takenspots == 9) and (win == False) and (loss == False): #need bools for win/loss to prevent clash (if win and full board etc.)
        gameover = True
        message('stalemate')
        

    screen = turtle.Screen()
    if gameover == True:
        answer = screen.textinput("Game over!", "Do you want to play again? (Y/N)") #prompt
        
        if (answer == None) or (answer.lower().startswith('n')): #presses cancel or says No etc.
            print("Exiting game. Goodbye!")
            screen.clear()
            screen.bye()
        else: #starts new game
            print("Starting a new round!")
            screen.clear()
            reset_board(the_board)
            main()
    
    return gameover

def reset_board(board):
    #Sig: list(str) -> list(str)
    #Clears the_board once a new game has started
    for i in range(9):
        the_board[i] = "_"
    return the_board

def do_computer_move(board):
    """
    sig: list(str) -> NoneType
    Given a list representing the state of the board,
    select a position for the computer's move and
    update the board with an X in an appropriate
    position. The algorithm for selecting the
    computer's move shall be as follows: if it is
    possible for the computer to win in one move,
    it must do so. If the human player is able 
    to win in the next move, the computer must
    try to block it. Otherwise, the computer's
    next move may be any random, valid position
    (selected with the random.randint function).
    """
    
    madeMove = False
    close_to_win = [ [0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7],  [2,5,8], [0,4,8], [2,4,6] ]
    
    #WIP; combine attack and block AI

    letters = ["X", "O"]
    #attack and block AI: find 2 X's to finish / find 2 O's to block
    for aletter in letters:
        for aset in close_to_win:
            if the_board[aset[0]] == the_board[aset[1]] == aletter: #if first two spots are X occupied
                if the_board[aset[2]] == "_":
                    the_board[aset[2]] = "X"
                    madeMove = True
                    break
            if the_board[aset[1]] == the_board[aset[2]] == aletter: #if last two spots are X occupied
                if the_board[aset[0]] == "_":
                    the_board[aset[0]] = "X"
                    madeMove = True
                    break
            if the_board[aset[0]] == the_board[aset[2]] == aletter: #if first and last spots are X occupied
                if the_board[aset[1]] == "_":
                    the_board[ aset[1]] = "X"
                    madeMove = True
                    break        

    free_spots = []

    if not madeMove: #if first two didn't work, go with random X assignment (3rd priority)
        for i in range(0, len(the_board)):
            if (the_board[i] == "_"):
                free_spots.append(i)
        random_free_spot = random.choice(free_spots)
        the_board[random_free_spot] = "X"

def clickhandler(x, y):
    """
    sig: int, int -> NoneType
    This function is called by turtle in response
    to a user click. The parameters are the screen
    coordinates indicating where the click happened.
    The function will call other functions. You do not
    need to modify this function, but you do need
    to understand it.
    """
    if do_user_move(the_board,x,y):
        draw_board(the_board)
        if not check_game_over(the_board):
            do_computer_move(the_board)
            draw_board(the_board)
            check_game_over(the_board)

def main():
    """
    sig: () -> NoneType
    Runs the tic-tac-toe game. You shouldn't
    need to modify this function.
    """
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onscreenclick(clickhandler)
    draw_board(the_board)
    turtle.mainloop()

main()