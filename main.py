# Créé par croqu, le 26/03/2024 en Python 3.7

from operator import ge
from random import randint
# Representation of a matrix using lists :
# Matrix A (2 by 2) :
# [ 0 1 ]
# [ 2 3 ]
list1 = [0,1]
list2 = [2,3]


# List representing a matrix :

def sqmatrix(x):
    list3 = []
    sqm = []
    for i in range(x):
        list3.append(0)
    for i in range(x):
        sqm.append(list3)
    return sqm
#print(sqmatrix(5))
# Accessing to the number 1 :

# You will need to create these following functions to make the manipulation much easier
# To get the documentation of lists, run in python :
# help(list)

# Notes about what we learned previously and more : http://learn.wecodux.com/python/lists



# Create a function taking as parameters DIMX and DIMY, the dimension of the matrix
# We suppose that the parameters are greater that 1
# you need to return a list representing a matrix filled with 0
def createBoard(DIMX, DIMY):
    list4 = []
    matrix = []
    for i in range(DIMY):
        for i in range(DIMX):
            list4.append(0)
        matrix.append(list4)
        list4=[]
    return matrix

# Try to print your matrix in a pretty way that should looks like this :
""" 2x2 matrix :
  0 1
0 0 0
1 0 0
"""
def showBoardwco(board):
    rownb=len(board)
    ll=[" "]
    for v in range(len(board[0])):
        ll.append(v)
    print(*ll)
    for c in range(rownb):
        #for x in range(len(board[c])):
        #    print (board[c][x])
        print(c,*board[c])
#showBoardwco(createBoard(4, 6))
# Where the rows are the x coordinates and the columns are the y coordinates

# Define a function getBoardXY returning the value of a matrix depending on the x and y coordinates
# If x or y is out of the range of the matrix, return -1
def getBoardXY(board, x, y):
    if x>len(board[0]):
        val=-1
    elif y>len(board):
        val=-1
    else:
        val=board[y][x]
    return val

#print(getBoardXY((createBoard(4, 6)), 3, 5))
# Define a function setBoardXY, if x and y are correct value, return the modified matrix
# otherwise, return the same matrix
def setBoardXY(board, x, y, value):
    if getBoardXY(board, x, y) == -1:
        pass
    else:
        board[y][x] = value
    return board

#print(setBoardXY((createBoard(4, 6)), 3, 5, 1))

# Now we can work with numbers inside of a matrix, we can represent numbers with mines etc...
# The representation will be :
# 9 : a mine
# 0  : no bombs around
# 1 to 8 : numbers of mines around
# x : a character showing there is nothing discovered yet

# As for the hangman, we will work with two matrix :
# - The first matrix will represent the board with the mines (9) placed on the matrix and the number of mines around (0 to 8)
#   The user shouldn't be able to see this board, you can still print it to debug but in the final game,
#   The user need to guess the correct number of this board. This matrix is called the model (it is the logic part)
""" Example of a 3x2 matrix :
  0 1 2
0 9 1 0
1 1 1 0
"""

# - The second matrix will be what the user see and will interact with. He will then start with an empty matrix of x
#   (as he didn't entered any number)
""" Example of a 3x2 matrix :
  0 1 2
0 x x x
1 x x x
"""

### No tests on this one ###
# Create a function initialising bombs, place first some mines in a board
# you should end up with returned matrix like this (you can place mines manually or generate them randomly) :
"""
  0 1 2
0 9 0 0
1 0 0 0
"""
def init_Mines(board, minenb):
    for i in range(minenb):
        max=len(board[0]) -1
        may=len(board) -1
        x=randint(0,max)
        y=randint(0,may)
        setBoardXY(board, x, y, 9)

#calculate mine nb
def minenb(board, difficulty):
    X=len(board[0])
    Y=len(board)
    if difficulty == 1:
        nb= (12*(X*Y))/100
        nb= int(nb)
    if difficulty == 2:
        nb= (15*(X*Y))/100
        nb= int(nb)
    if difficulty == 3:
        nb= (20*(X*Y))/100
        nb= int(nb)
    else:
        pass
    return nb


# Create a function returning a matrix with the number of mines around a cell for each cells
def generate_Cell_Numbers(board):
    for i in range(len(board)):
        for u in range(len(board[i])):
            if board[i][u] == 9:
                if i !=0:
                    if board[i-1][u] != 9:
                        board[i-1][u]=board[i-1][u]+1

                if u !=0:
                    if board[i][u-1] != 9:
                        board[i][u-1]=board[i][u-1]+1

                if i != len(board) -1:
                    if board[i+1][u] != 9:
                        board[i+1][u]=board[i+1][u]+1

                if u != len(board[i]) -1:
                    if board[i][u+1] != 9:
                        board[i][u+1]=board[i][u+1]+1

                if i !=0 and u != len(board[i]) -1:
                    if board[i-1][u+1] != 9:
                        board[i-1][u+1]=board[i-1][u+1]+1

                if u !=0 and i != len(board) -1:
                    if board[i+1][u-1] != 9:
                        board[i+1][u-1]=board[i+1][u-1]+1

                if u!=0 and i!=0:
                    if board[i-1][u-1] != 9:
                        board[i-1][u-1]=board[i-1][u-1]+1

                if i != len(board) -1 and u != len(board[i]) -1:
                    if board[i+1][u+1] != 9:
                        board[i+1][u+1]=board[i+1][u+1]+1

### No test on this one ###
# Define the function init_Logic_Board using init_Mines and generate_Cell_Numbers to return the logic board of the game
def init_Logic_Board(DIMX, DIMY, diff):
    a=createBoard(DIMX, DIMY)
    val=minenb(a,diff)
    init_Mines(a,val)
    generate_Cell_Numbers(a)
    return a

# This function will generate a matrix of characters "x", this will be the Vue (what the user see in front)
def init_Vue_Board(DIMX, DIMY):
    list4 = []
    matrix = []
    for i in range(DIMY):
        for i in range(DIMX):
            list4.append("X")
        matrix.append(list4)
        list4=[]
    return matrix

## To know if a player won, you need to check if every "x" of the Vue matrix is at the
## same place with the mines in the logic board. If this is the case, return True otherwise, return False
## We suppose that the two matrix has the same dimension
def check_Won(board_Vue, board_Logic):
    md=0
    tm=0
    for i in range(len(board_Logic)):
        for u in range(len(board_Logic[i])):
            if board_Logic[i][u] == 9:
                if board_Vue[i][u] == "O":
                    md=md+1
                    tm=tm+1
                else:
                    tm=tm+1
    return tm-md


# From This point, you have every tools (functions) you need to create a minesweeper game.
# - Generate the logical and the vue board
# - Keep repeating these 4 steps until the player hit a mine or won the game :
# - Ask the user the coordinate x
# - Ask the user the coordinate y
# - Show his board updated (replace the x with the number of the logical board)
#   If the user discovered a mine, he lost the game and the game stops

# The goal to this game is to discover every digit (0 to 8) without finding the bombs. If you found
# a mine with the x and y coordinates, you lost
if __name__ == "__main__":
    dimx=int(input("quelle dimension en X? "))
    dimy=int(input("quelle dimension en Y? "))
    dif=int(input("quelle difficulté ? (1, 2 ou 3) "))

    LB=init_Logic_Board(dimx, dimy, dif)
    VB=init_Vue_Board(dimx, dimy)
    game = "début"
    if minenb(LB,dif) ==0:
        game= "end"
        print("not possible")
    while game != "end":
        showBoardwco(VB)
        coY=int(input("quelle co en X ? "))
        coX=int(input("quelle co en Y ? "))
        mine=str(input("est-ce une mine ?(y/n) "))
        if mine == "cheat":
            showBoardwco(LB)

        if mine == "end" :
            game = "end"

        if LB[coX][coY]==9 and mine=="n":
            print("PERDU")
            game = "end"

        if LB[coX][coY]==9 and mine=="y":
            print("mine découverte")
            VB[coX][coY] = "O"

        if LB[coX][coY]!=9 and mine=="y":
            print("LOUPé")

        if check_Won(VB,LB)==0 :
            print("GAGNé")
            game = "end"

        if VB[coX][coY] != "O":
            VB[coX][coY] = LB[coX][coY]


