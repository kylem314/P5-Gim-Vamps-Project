#this is the file that you will be editing to edit the display on the buttons
#from movepiece import len2, len3, len4, len5, len6, len7
from piecedefinitions import *
"""from zwhitepersp import *
from zblackpersp import *"""
from checkfunctions import *
from protectionfunctions import *
#from movepiece import movepiece

board = { #intial configuration of the board
    "a8": "BR1n", "b8": "BN1", "c8": "BB1", "d8": "BQ1", "e8": "BK1n", "f8": "BB2", "g8": "BN2", "h8": "BR2n",
    "a7": "bp1", "b7": "bp2", "c7": "bp3", "d7": "bp4", "e7": "bp5", "f7": "bp6", "g7": "bp7", "h7": "bp8",
    "a6": "  ", "b6": "  ", "c6": "  ", "d6": "  ", "e6": "  ", "f6": "  ", "g6": "  ", "h6": "  ",
    "a5": "  ", "b5": "  ", "c5": "  ", "d5": "  ", "e5": "  ", "f5": "  ", "g5": "  ", "h5": "  ",
    "a4": "  ", "b4": "  ", "c4": "  ", "d4": "  ", "e4": "  ", "f4": "  ", "g4": "  ", "h4": "  ",
    "a3": "  ", "b3": "  ", "c3": "  ", "d3": "  ", "e3": "  ", "f3": "  ", "g3": "  ", "h3": "  ",
    "a2": "wp1", "b2": "wp2", "c2": "wp3", "d2": "wp4", "e2": "wp5", "f2": "wp6", "g2": "wp7", "h2": "wp8",
    "a1": "WR1n", "b1": "WN1", "c1": "WB1", "d1": "WQ1", "e1": "WK1n", "f1": "WB2", "g1": "WN2", "h1": "WR2n"}

og_board = { #to set the board equal to when the create the board is pressed
    "a8": "BR1n", "b8": "BN1", "c8": "BB1", "d8": "BQ1", "e8": "BK1n", "f8": "BB2", "g8": "BN2", "h8": "BR2n",
    "a7": "bp1", "b7": "bp2", "c7": "bp3", "d7": "bp4", "e7": "bp5", "f7": "bp6", "g7": "bp7", "h7": "bp8",
    "a6": "  ", "b6": "  ", "c6": "  ", "d6": "  ", "e6": "  ", "f6": "  ", "g6": "  ", "h6": "  ",
    "a5": "  ", "b5": "  ", "c5": "  ", "d5": "  ", "e5": "  ", "f5": "  ", "g5": "  ", "h5": "  ",
    "a4": "  ", "b4": "  ", "c4": "  ", "d4": "  ", "e4": "  ", "f4": "  ", "g4": "  ", "h4": "  ",
    "a3": "  ", "b3": "  ", "c3": "  ", "d3": "  ", "e3": "  ", "f3": "  ", "g3": "  ", "h3": "  ",
    "a2": "wp1", "b2": "wp2", "c2": "wp3", "d2": "wp4", "e2": "wp5", "f2": "wp6", "g2": "wp7", "h2": "wp8",
    "a1": "WR1n", "b1": "WN1", "c1": "WB1", "d1": "WQ1", "e1": "WK1n", "f1": "WB2", "g1": "WN2", "h1": "WR2n"}

keysBoard, valuesBoard = zip(*board.items()) # isolates the board keys and board values

""" from chessmain.py from chessOO neeeded to define the """
whitemove = "W"
whitecolor = "red"
blackcolor = "lighter blue"

"""storeboard = {
    "a8": [], "b8": [], "c8": [], "d8": [], "e8": [], "f8": [], "g8": [], "h8": [],
    "a7": [], "b7": [], "c7": [], "d7": [], "e7": [], "f7": [], "g7": [], "h7": [],
    "a6": [], "b6": [], "c6": [], "d6": [], "e6": [], "f6": [], "g6": [], "h6": [],
    "a5": [], "b5": [], "c5": [], "d5": [], "e5": [], "f5": [], "g5": [], "h5": [],
    "a4": [], "b4": [], "c4": [], "d4": [], "e4": [], "f4": [], "g4": [], "h4": [],
    "a3": [], "b3": [], "c3": [], "d3": [], "e3": [], "f3": [], "g3": [], "h3": [],
    "a2": [], "b2": [], "c2": [], "d2": [], "e2": [], "f2": [], "g2": [], "h2": [],
    "a1": [], "b1": [], "c1": [], "d1": [], "e1": [], "f1": [], "g1": [], "h1": []}"""

storeboard = {
    "a8": [], "b8": [], "c8": [], "d8": [], "e8": [], "f8": [], "g8": [], "h8": [],
    "a7": [], "b7": [], "c7": [], "d7": [], "e7": [], "f7": [], "g7": [], "h7": [],
    "a6": ["bp1"], "b6": ["bp2"], "c6": ["bp3", "BN1"], "d6": ["bp4"], "e6": ["bp5"], "f6": ["bp6", "BN2"],
    "g6": ["bp7"], "h6": ["bp8"],
    "a5": ["bp1"], "b5": ["bp2"], "c5": ["bp3"], "d5": ["bp4"], "e5": ["bp5"], "f5": ["bp6"], "g5": ["bp7"],
    "h5": ["bp8"],
    "a4": ["wp1"], "b4": ["wp2"], "c4": ["wp3"], "d4": ["wp4"], "e4": ["wp5"], "f4": ["wp6"], "g4": ["wp7"],
    "h4": ["wp8"],
    "a3": ["wp1"], "b3": ["wp2"], "c3": ["wp3", "WN1"], "d3": ["wp4"], "e3": ["wp5"], "f3": ["wp6", "WN2"],
    "g3": ["wp7"], "h3": ["wp8"],
    "a2": [], "b2": [], "c2": [], "d2": [], "e2": [], "f2": [], "g2": [], "h2": [],
    "a1": [], "b1": [], "c1": [], "d1": [], "e1": [], "f1": [], "g1": [], "h1": []}

ogstoreboard = {
    "a8": [], "b8": [], "c8": [], "d8": [], "e8": [], "f8": [], "g8": [], "h8": [],
    "a7": [], "b7": [], "c7": [], "d7": [], "e7": [], "f7": [], "g7": [], "h7": [],
    "a6": [], "b6": [], "c6": [], "d6": [], "e6": [], "f6": [], "g6": [], "h6": [],
    "a5": [], "b5": [], "c5": [], "d5": [], "e5": [], "f5": [], "g5": [], "h5": [],
    "a4": [], "b4": [], "c4": [], "d4": [], "e4": [], "f4": [], "g4": [], "h4": [],
    "a3": [], "b3": [], "c3": [], "d3": [], "e3": [], "f3": [], "g3": [], "h3": [],
    "a2": [], "b2": [], "c2": [], "d2": [], "e2": [], "f2": [], "g2": [], "h2": [],
    "a1": [], "b1": [], "c1": [], "d1": [], "e1": [], "f1": [], "g1": [], "h1": []}
""" ------------------------------------------------ """

# the row dictonaries that the board is split out too
board1 = {} #rank 1 (row 1) (closest to white)
board2 = {}
board3 = {}
board4 = {}
board5 = {}
board6 = {}
board7 = {}
board8 = {} #rank 8 (row 8) (farthest from white)

listBoard = ["", board1, board2, board3, board4, board5, board6, board7, board8] # inluded "" to artificialy overcome the 0 index
dictionarything = {"BR": "♜", "BN": "♞", "BB": "♝", "BQ": "♛", "BK": "♚", "bp": "♟︎️︎", "WR": "♖", "WN": "♘", "WB": "♗", "WQ": "♕", "WK": "♔", "wp": "♙"}

# spliting the dictonary into 8 dictonaries, if the second value within the cell "a8" is 8 then update the row of the board with that value
for square,piece in board.items():
    if piece != "  ":
        # if the values is not empty then replace the cell value with the unicode of the value
        listBoard[int(square[1])].update({square:dictionarything[piece[0:2]]})
    else:
        """if the values of the dictonary are empty, we replace it with a string emptySpace, 
        this allows for us in the jinja template replace the value emptySpace with &nbsp;&nbsp;&nbsp;&nbsp; 
        or whitespace only interpreted by html"""
        listBoard[int(square[1])].update({square:"emptySpace"})

# placing all of the ranks (rows) allows the jinja template to show each dictonary as the row of the tbale
allBoard = [board8, board7, board6, board5, board4, board3, board2, board1]

def split_board(board):
    print(type(board))
    for square,piece in board.items():
        if piece != "  ":
            # if the values is not empty then replace the cell value with the unicode of the value
            listBoard[int(square[1])].update({square:dictionarything[piece[0:2]]})
        else:
            """if the values of the dictonary are empty, we replace it with a string emptySpace, 
            this allows for us in the jinja template replace the value emptySpace with &nbsp;&nbsp;&nbsp;&nbsp; 
            or whitespace only interpreted by html"""
            listBoard[int(square[1])].update({square:"emptySpace"})
    allBoard = [board8, board7, board6, board5, board4, board3, board2, board1]
    return allBoard

#keeping track of the moves
movelist = []

# initializing N
N = 2
res = movelist[-N:]

def sample(currentMove,res):
    b = currentMove%2
    if b != 0:
        #this means the only the first value of the move has been selected
        message = "cannot sample the values yet"
        return message
    else: #this means that two cells have been slected
        usermove = ' '.join(res)#this is the string that is passed into movePiece
        message = "last two moves were"+ " " + usermove
        #print(str(res))
        len5(usermove, board, storeboard, whitemove, whitecolor, blackcolor)
        return message
    #if the move was invalid message = "last two moves were invalid"+ " " + usermove

#from move piece code
def len5(usermove, board, storeboard, whitemove, whitecolor, blackcolor):
    if usermove[2] == ' ':
        piece = board[usermove[0:2]]#the value in the board dictonary will represent the piece
        startpos = usermove[0:2]#the
        print(usermove)
        #print(usermove[3:5])
        if piece in storeboard[usermove[3:5]]:
            board[startpos] = '  '
            board[usermove[3:5]] = piece
            #print(board)
            if whitemove == "W":
                #blackpersp(whitecolor, blackcolor, board) #print the board in black perspective
                whitemove = "B"
            else:
                whitemove = "W"
                #whitepersp(whitecolor, blackcolor, board) #print the board in black perspective
            storeboard = storeboardset(board, whitemove, 1)
        else:
            message = "Please enter a valid move."
            print("you have arrived")
            #print(board)#split_board(board)
            """for board in split_board(board):
                print(board)"""


def storeboardset(board, whitemove, setting):
    storeboard = {
        "a8": [], "b8": [], "c8": [], "d8": [], "e8": [], "f8": [], "g8": [], "h8": [],
        "a7": [], "b7": [], "c7": [], "d7": [], "e7": [], "f7": [], "g7": [], "h7": [],
        "a6": [], "b6": [], "c6": [], "d6": [], "e6": [], "f6": [], "g6": [], "h6": [],
        "a5": [], "b5": [], "c5": [], "d5": [], "e5": [], "f5": [], "g5": [], "h5": [],
        "a4": [], "b4": [], "c4": [], "d4": [], "e4": [], "f4": [], "g4": [], "h4": [],
        "a3": [], "b3": [], "c3": [], "d3": [], "e3": [], "f3": [], "g3": [], "h3": [],
        "a2": [], "b2": [], "c2": [], "d2": [], "e2": [], "f2": [], "g2": [], "h2": [],
        "a1": [], "b1": [], "c1": [], "d1": [], "e1": [], "f1": [], "g1": [], "h1": []}
    piecefunc = {"wp": wpawn, "bp": bpawn, "WN": wknight, "BN": bknight, "WR": wrook, "BR": brook, "WB": wbishop,
                 "BB": bbishop, "WQ": wqueen, "BQ": bqueen, "WK": wking, "BK": bking}
    stalemate = True
    for i in board:
        piece = board[i][0:2]
        if piece != '  ':
            storeboard1 = dict(storeboard)
            storeboard = dict(piecefunc[piece](dict(board), dict(storeboard), board[i], i[0], int(i[1])))
            if storeboard != storeboard1 and piece[0].upper() == whitemove:
                stalemate = False
            if board[i][0:3] == whitemove + "K1":
                kingpos = i
                print("Kingpos = " + kingpos)

    checkmate = False
    if setting != 2:
        if len(storeboard[kingpos]) > 0:
            storeboard = check(board, storeboard, kingpos, whitemove)
            # if storeboard:
                # checkmate is true
            #     pass
        return storeboard
    else:
        return kingpos, storeboard


def check(board, storeboard, kingpos, whitemove):
    # note that because it is calculating the upcoming move, whitemove is the side that will be in check
    king = board[kingpos]
    piecedict = aidictionarything(storeboard)
    storeboard1 = {
        "a8": [], "b8": [], "c8": [], "d8": [], "e8": [], "f8": [], "g8": [], "h8": [],
        "a7": [], "b7": [], "c7": [], "d7": [], "e7": [], "f7": [], "g7": [], "h7": [],
        "a6": [], "b6": [], "c6": [], "d6": [], "e6": [], "f6": [], "g6": [], "h6": [],
        "a5": [], "b5": [], "c5": [], "d5": [], "e5": [], "f5": [], "g5": [], "h5": [],
        "a4": [], "b4": [], "c4": [], "d4": [], "e4": [], "f4": [], "g4": [], "h4": [],
        "a3": [], "b3": [], "c3": [], "d3": [], "e3": [], "f3": [], "g3": [], "h3": [],
        "a2": [], "b2": [], "c2": [], "d2": [], "e2": [], "f2": [], "g2": [], "h2": [],
        "a1": [], "b1": [], "c1": [], "d1": [], "e1": [], "f1": [], "g1": [], "h1": []}
    check = True
    checkmate = True
    board1 = dict(board)
    for piece in piecedict.keys():
        if piece[0].upper() == whitemove:
            for space in board.keys():
                if board[space][0:3] == piece:
                    piecepos = space
                    break
            for move in piecedict[piece]:
                board1 = dict(board)
                board1[piecepos] = '  '
                board1[move] = board[piecepos]
                kingpos2, storeboard2 = storeboardset(board1, whitemove, 2)
                if len(storeboard2[kingpos2]) == 0:
                    storeboard1[move].append(piece)
                    checkmate = False
    # if checkmate:
    #     return True
    # else:
    return storeboard1


def aidictionarything(storeboard):
    dictionary = {
        "bp1": [], "bp2": [], "bp3": [], "bp4": [], "bp5": [], "bp6": [], "bp7": [], "bp8": [],
        "BR1": [], "BN1": [], "BB1": [], "BQ1": [], "BK1": [], "BB2": [], "BN2": [], "BR2": [],
        "WR1": [], "WN1": [], "WB1": [], "WQ1": [], "WK1": [], "WB2": [], "WN2": [], "WR2": [],
        "wp1": [], "wp2": [], "wp3": [], "wp4": [], "wp5": [], "wp6": [], "wp7": [], "wp8": []}
    for i in storeboard:
        for k in storeboard[i]:
            dictionary[k[0:3]].append(i)
    return #dictionary


# this gets a dict with key = protected, term = list of protectors
def protdictfunc(board, storeboard, whitemove):
    protdict = {
        "bp1": [], "bp2": [], "bp3": [], "bp4": [], "bp5": [], "bp6": [], "bp7": [], "bp8": [],
        "BR1": [], "BN1": [], "BB1": [], "BQ1": [], "BK1": [], "BB2": [], "BN2": [], "BR2": [],
        "WR1": [], "WN1": [], "WB1": [], "WQ1": [], "WK1": [], "WB2": [], "WN2": [], "WR2": [],
        "wp1": [], "wp2": [], "wp3": [], "wp4": [], "wp5": [], "wp6": [], "wp7": [], "wp8": []}
    protfunc = {"wp": wpawnprot, "bp": bpawnprot, "WN": knightprot, "BN": knightprot, "WR": wrookprot, "BR": brookprot,
                "WB": wbishopprot, "BB": bbishopprot, "WQ": wqueenprot, "BQ": bqueenprot}

    for i in board:
        piece = board[i][0:2]
        if piece != '  ' and piece[1] != 'K':
            protdict = protfunc[piece](board, protdict, board[i][0:3], i[0], int(i[1]))
        elif piece[1] == 'K':
            protdict = kingprot(board, protdict, board[i][0:3], i[0], int(i[1]), storeboard)
    return protdict

# this takes the routes that are selected by the buttons an appends them to moveList
def movesdata(toAppend):
    movelist.append(toAppend)
    sets = [movelist[x:x+2] for x in range(0, len(movelist), 2)]
    return sets

def actualMove(currentMove):
    actMove = round(currentMove/2)
    return actMove

def previousMove(acutalMove):
    if acutalMove%2 != 0:
        print("previously: white's move")
    else:
        print("previously: black's move") #this is the player that is wi

def getMove():
    return actualMove(len(movelist))

def didMove():
    if len(movelist)>0 and len(movelist)%2 ==0:
        return True
    return False

def getUserMove1():
    if len(movelist)==0:
        return ""
    if len(movelist)%2 ==0:
        return movelist[len(movelist)-2]
    return movelist[len(movelist)-1]

def getUserMove2():
    if len(movelist)==0:
        return ""
    if len(movelist)%2 ==0:
        return movelist[len(movelist)-1]
    return ""

def getColor():
    turn=round(len(movelist)/2)
    if turn%2==0:
        return "B"
    return "W"

def newGame():
    movelist.clear()
