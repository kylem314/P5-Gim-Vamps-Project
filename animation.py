import time
import os
from random import randrange
import sys


# adding a comment to test editing on INteliJ
def menuAni():
    # terminal print commands
    ANSI_CLEAR_SCREEN = u"\u001B[2J"
    ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
    RESET_COLOR = u"\u001B[0m\u001B[2D"

    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'

    colorBar = CGREEN  # color of the loading bar
    possibleColor = [CBLACK, CRED, CGREEN, CYELLOW, CBLUE, CVIOLET, CBEIGE, CWHITE]

    chess = [
        "                            ",
        "       _                    ",
        "   ___| |__   ___  ___ ___  ",
        "  / __| '_ \ / _ \/ __/ __| ",
        " | (__| | | |  __/\__ \__ \ ",
        "  \___|_| |_|\___||___/___/ "
    ]

    pawn = [
        "    _    ",
        "   (_)   ",
        "  (___)  ",
        "  _|_|_  ",
        " (_____) ",
        " /_____\ "
    ]

    def printTitle():
        for i in range(len(chess)):
            print(pawn[i] + chess[i] + pawn[i])

    length = 16
    loading = []  # this is the list which creates the loading animation

    def printLoading(postition):
        space = (postition - 1) * "   "
        print(*loading, end="")  # this prints the whole list of the loading bar and
        print(space + "|")  # this is the symbol for the final vertical bar, denotes fully loaded when reached

        loading.append(colorBar + "☺☻")  # appends another mark onto the loading bar

    for i in range(0, length):
        # c.cursor(0)
        print(RESET_COLOR, end="")  # to stop coloring after the ocean, without this line then everything is highlighted
        print(ANSI_HOME_CURSOR, end="")  # to clear the screen print in the same top left corner every time

        print(possibleColor[randrange(len(possibleColor))], end="")  # chooses random color for the title
        printTitle()  # printing title
        backwards = length - i  # to help with the placement of the vertical end line
        printLoading(backwards)  # prints the loading bar under the title

        time.sleep(.1)  # to diffrentiate the color changes

    #os.system('clear')
    print(CWHITE, end="")
    printTitle()  # printing title
    print(*loading, end="")  # prints the whole bar
    print("|")  # hard coding reached the end
    print(CWHITE)


def endAni():
    ANSI_CLEAR_SCREEN = u"\u001B[2J"
    ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
    RESET_COLOR = u"\u001B[0m\u001B[2D"

    # coloring the text

    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'

    CREDBG = '\33[41m'  # highlighting background
    CWHITEBG = '\33[47m'
    CBLACKBG = '\33[40m'

    possibleColor = [CBLACK, CRED, CGREEN, CYELLOW, CBLUE, CVIOLET, CBEIGE, CWHITE]

    pawn = [
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "    _    ",
        "   (_)   ",
        "  (___)  ",
        "  _|_|_  ",
        " (_____) ",
        " /_____\ "
    ]
    rook = [
        "          ",
        "          ",
        " _  _  _  ",
        "| || || | ",
        "|_______| ",
        "\__ ___ / ",
        " |___|_|  ",
        " |_|___|  ",
        " |___|_|  ",
        "(_______) ",
        "/_______\ "
    ]

    knight = [
        "           ",
        "           ",
        "   ^^__    ",
        "  /  - \_  ",
        "<|    __<  ",
        "<|    \    ",
        "<|     \   ",
        "<|______\  ",
        " _|____|_  ",
        "(________) ",
        "/________\ "

    ]

    bishop = [
        "          ",
        "   _O     ",
        "  / //\   ",
        " {     }  ",
        "  \___/   ",
        "  (___)   ",
        "   |_|    ",
        "  /   \   ",
        " (_____)  ",
        "(_______) ",
        "/_______\ "
    ]
    queen = [
        "   _()_    ",
        " _/____\_  ",
        " \      /  ",
        "  \____/   ",
        "  (____)   ",
        "   |  |    ",
        "   |__|    ",
        "  /    \   ",
        " (______)  ",
        "(________) ",
        "/________\ "
    ]

    king = [
        "   _::_    ",
        " _/____\_  ",
        " \      /  ",
        "  \____/   ",
        "  (____)   ",
        "   |  |    ",
        "   |__|    ",
        "  /    \   ",
        " (______)  ",
        "(________) ",
        "/________\ "
    ]

    attackPiece = [pawn, rook, knight, bishop, queen]

    length = 24
    spaceF = 0
    lengthOfRect = length + 24
    kingColor = CRED
    attackColor = CBEIGE

    q = randrange(len(attackPiece))

    def resetScene():
        print(RESET_COLOR, end="")
        print(ANSI_HOME_CURSOR, end="")

    def printScene(postition, backwards, attackColor, kingColor, attack):
        spaceF = postition * " "
        spaceB = backwards * " "
        for i in range(len(pawn)):
            print(spaceF + attackColor + attack[i] + spaceB + kingColor + king[i])

    def print1by1(text, color, delay=0.1):
        for c in text:
            sys.stdout.write(color + c)
            sys.stdout.flush()
            time.sleep(delay)
        print

    """
  def imageTest(q):
    for i in range(len(attackPiece[q])):
      print(attackPiece[q][i]+"|")
  """

    def move(y, x):
        print("\033[%d;%dH" % (y, x))

    def printMiddle(message, background):
        front = lengthOfRect - len(message)
        front = front / 2
        front = round(front)
        space = " " * front
        print("\n")
        print(background + space, end="")
        print1by1(message, CREDBG)
        move(11, 0)
        print(u"\u001B[0m")
        # print(background + ANSI_HOME_CURSOR + background)

    print(RESET_COLOR, end="")
    print(ANSI_HOME_CURSOR)
    for i in range(50):
        print("\n")

    for i in range(0, length):
        resetScene()
        print(CBLACK, end="")  # color the background
        backwards = length - i  # to help with the placement of the vertical end line
        printScene(i, backwards, attackColor, kingColor, attackPiece[q])
        time.sleep(.1)  # to diffrentiate the color changes

    resetScene()

    for i in range(len(king)):  # all all red
        print(CREDBG + " " * lengthOfRect)

    time.sleep(.1)  # to diffrentiate the color changes
    resetScene()
    message = "The King has been Captured!"
    printMiddle(message, CREDBG)
