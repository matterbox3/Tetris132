# Techtris
# Date: 10-29-17

import random, time, pygame, sys, RPi.GPIO as GPIO
from pygame.locals import *
from gpiozero import Button
from time import sleep

#setting GPIO pin values
middle = 25
right = 22
left = 27

#Initializing GPIO Ports
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(middle, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(right, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(left, GPIO.IN, pull_up_down = GPIO.PUD_UP)

left = Button(left)
right = Button(right)
middle = Button(middle)

#Setting Variables
FPS = 25
WINDOWWIDTH = 720
WINDOWHEIGHT = 430
BOXSIZE = 21
BOARDWIDTH = 30
BOARDHEIGHT = 20
BLANK = '.'

MOVESIDEWAYSFREQ = 1.0
MOVEDOWNFREQ = 2.0

XMARGIN = int((WINDOWWIDTH - BOARDWIDTH * BOXSIZE) / 2)
TOPMARGIN = WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE) - 5



#Colors        R    G    B
WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
BLACK       = (  0,   0,   0)
RED         = (155,   0,   0)
LIGHTRED    = (175,  20,  20)
BLUE        = (  0,   0, 155)
LIGHTBLUE   = ( 20,  20, 175)

#Setting Colors
BORDERCOLOR = RED
BGCOLOR = WHITE
TEXTCOLOR = RED
TEXTSHADOWCOLOR = BLUE
COLORS      = (     BLUE,      RED)
LIGHTCOLORS = (LIGHTBLUE,  LIGHTRED)
assert len(COLORS) == len(LIGHTCOLORS) # each color must have light color

TEMPLATEWIDTH = 5
TEMPLATEHEIGHT = 5

#All Techtris Pieces
J_SHAPE_TEMPLATE = [['..O..',
                     '..O..',
                     '..OO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '.....',
                     '..OOO',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '.O...',
                     '.OO..',
                     '..O..',
                     '..O..'],
                    ['.....',
                     '..OO.',
                     'OOO..',
                     '.....',
                     '.....']]

j_SHAPE_TEMPLATE = [['..O..',
                     '..O..',
                     '.OO..',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..OOO',
                     '.....',
                     '.....'],
                    ['.....',
                     '...O.',
                     '..OO.',
                     '..O..',
                     '..O..'],
                    ['.....',
                     '.....',
                     'OOO..',
                     '..OO.',
                     '.....']]

L_SHAPE_TEMPLATE = [['..O..',
                     '..O..',
                     '..O..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOOO',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..O..',
                     '..O..',
                     '..O..'],
                    ['.....',
                     '...O.',
                     'OOOO.',
                     '.....',
                     '.....']]

l_SHAPE_TEMPLATE = [['..O..',
                     '..O..',
                     '..O..',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '.O...',
                     '.OOOO',
                     '.....',
                     '.....'],
                    ['.....',
                     '..OO.',
                     '..O..',
                     '..O..',
                     '..O..'],
                    ['.....',
                     '.....',
                     'OOOO.',
                     '...O.',
                     '.....']]



F_SHAPE_TEMPLATE = [['..O..',
                     '..O..',
                     '.OO..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OOOO',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '..O..',
                     '..O..'],
                    ['.....',
                     '.....',
                     'OOOO.',
                     '..O..',
                     '.....']]

f_SHAPE_TEMPLATE = [['..O..',
                     '..O..',
                     '..OO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOOO',
                     '..O..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '..O..',
                     '..O..'],
                    ['.....',
                     '..O..',
                     'OOOO.',
                     '.....',
                     '.....']]

D_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OOO.',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '.OO..',
                     '.O...',
                     '.....']]

d_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '..OO.',
                     '.OOO.',
                     '.....'],
                    ['.....',
                     '.O...',
                     '.OO..',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '.OOO.',
                     '.OO..',
                     '.....',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '.OO..',
                     '..O..',
                     '.....']]

K_SHAPE_TEMPLATE = [['.....',
                     '..O..',
                     '.OO..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OOO.',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..OO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '...O.',
                     '.OOO.',
                     '..O..',
                     '.....']]

k_SHAPE_TEMPLATE = [['.....',
                     '..OO.',
                     '.OO..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OOO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '.O...',
                     '.OOO.',
                     '..O..',
                     '.....']]

I_SHAPE_TEMPLATE = [['..O..',
                     '..O..',
                     '..O..',
                     '..O..',
                     '..O..'],
                    ['.....',
                     '.....',
                     'OOOOO',
                     '.....',
                     '.....']]

C_SHAPE_TEMPLATE = [['.....',
                     '.OOO.',
                     '.O...',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OOO.',
                     '...O.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '...O.',
                     '...O.',
                     '.OOO.',
                     '.....'],
                    ['.....',
                     '.O...',
                     '.O...',
                     '.OOO.',
                     '.....']]

T_SHAPE_TEMPLATE = [['.....',
                     '.OOO.',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '...O.',
                     '.OOO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '.OOO.',
                     '.....'],
                    ['.....',
                     '.O...',
                     '.OOO',
                     '.O...',
                     '.....']]

W_SHAPE_TEMPLATE = [['.....',
                     '...O.',
                     '..OO.',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '.O...',
                     '.OO..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '..OO.',
                     '.OO..',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..OO.',
                     '...O.',
                     '.....']]

t_SHAPE_TEMPLATE = [['.....',
                     '..O..',
                     '.OOO.',
                     '..O..',
                     '.....']]

U_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OOO.',
                     '.O.O.',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..O..',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '.O.O.',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '.O...',
                     '.OO..',
                     '.....']]

S_SHAPE_TEMPLATE = [['.....',
                     '.O...',
                     '.OOO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..OO.',
                     '..O..',
                     '.OO..',
                     '.....']]

Z_SHAPE_TEMPLATE = [['.....',
                     '...O.',
                     '.OOO.',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..O..',
                     '..OO.',
                     '.....']]
                   

PIECES = {'J': J_SHAPE_TEMPLATE,
          'j': j_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'l': l_SHAPE_TEMPLATE,
          'F': F_SHAPE_TEMPLATE,
          'f': f_SHAPE_TEMPLATE,
          'D': D_SHAPE_TEMPLATE,
          'd': d_SHAPE_TEMPLATE,
          'K': K_SHAPE_TEMPLATE,
          'k': k_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'C': C_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE,
          'W': W_SHAPE_TEMPLATE,
          't': t_SHAPE_TEMPLATE,
          'U': U_SHAPE_TEMPLATE,
          'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,}

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BIGFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    BIGFONT = pygame.font.Font('freesansbold.ttf', 100)
    pygame.display.set_caption('Techtris')

    showTextScreen('Techtris')
    while True: #Starts music and runs game
        pygame.mixer.music.load('fightsong.mp3')
        pygame.mixer.music.play(-1, 0.0)
        runGame()
        pygame.mixer.music.stop()
        showTextScreen('Game Over')


def runGame():
    # setup variables for game
    board = getBlankBoard()
    lastMoveDownTime = time.time()
    lastMoveSidewaysTime = time.time()
    lastFallTime = time.time()
    movingDown = False
    movingLeft = False
    movingRight = False
    score = 0
    level, fallFreq = calculateLevelAndFallFreq(score)

    fallingPiece = getNewPiece()
    nextPiece = getNewPiece()

    while True: #Game loop
        if fallingPiece == None:
            # No falling piece in play, starts new piece
            fallingPiece = nextPiece
            nextPiece = getNewPiece()
            lastFallTime = time.time() # reset lastFallTime

            if not isValidPosition(board, fallingPiece):
                return #Game over

        checkForQuit()
        for event in pygame.event.get():
            if event.type == KEYUP:
                if (event.key == K_p):
                    #Pausing the game
                    showTextScreen('Paused') #Pause until key is pressed
                    lastFallTime = time.time()
                    lastMoveDownTime = time.time()
                    lastMoveSidewaysTime = time.time()
                elif (event.key == K_LEFT or event.key == K_a or left.is_pressed):
                    movingLeft = False
                elif (event.key == K_RIGHT or event.key == K_d):
                    movingRight = False
                elif (event.key == K_DOWN or event.key == K_s):
                    movingDown = False

            elif event.type == KEYDOWN:
                #Moves piece left and right
                if (event.key == K_LEFT or event.key == K_a or left.is_pressed) and isValidPosition(board, fallingPiece, adjX=1):
                    fallingPiece['x'] += 1
                    movingLeft = False
                    movingRight = True
                    lastMoveSidewaysTime = time.time()

                elif (event.key == K_RIGHT or event.key == K_d) and isValidPosition(board, fallingPiece, adjX=-1):
                    fallingPiece['x'] -= 1
                    movingRight = False
                    movingLeft = True
                    lastMoveSidewaysTime = time.time()

                #Rotates piece
                elif (event.key == K_UP or event.key == K_w):
                    fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(PIECES[fallingPiece['shape']])
                    if not isValidPosition(board, fallingPiece):
                        fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(PIECES[fallingPiece['shape']])
                elif (event.key == K_q): # rotate the other direction
                    fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(PIECES[fallingPiece['shape']])
                    if not isValidPosition(board, fallingPiece):
                        fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(PIECES[fallingPiece['shape']])

                #Increases fall speed
                elif (event.key == K_DOWN or event.key == K_s):
                    movingDown = True
                    if isValidPosition(board, fallingPiece, adjY=1):
                        fallingPiece['y'] += 1
                    lastMoveDownTime = time.time()

                #Auto drop
                elif event.key == K_SPACE:
                    movingDown = False
                    movingLeft = False
                    movingRight = False
                    for i in range(1, BOARDHEIGHT):
                        if not isValidPosition(board, fallingPiece, adjY=i):
                            break
                    fallingPiece['y'] += i - 1

        if (left.is_pressed) and (isValidPosition(board, fallingPiece, adjX=1)):
            fallingPiece['x'] += 1

        if (right.is_pressed) and (isValidPosition(board, fallingPiece, adjX=-1)):
            fallingPiece['x'] -= 1

        if (middle.is_pressed):
            fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(PIECES[fallingPiece['shape']])
            sleep(0.1)
            if not isValidPosition(board, fallingPiece):
                fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(PIECES[fallingPiece['shape']])
                sleep(0.1)
    
    
        

    #Moves piece
        if (movingLeft or movingRight) and time.time() - lastMoveSidewaysTime > MOVESIDEWAYSFREQ:
            if movingLeft and isValidPosition(board, fallingPiece, adjX=-1):
                fallingPiece['x'] -= 1
            elif movingRight and isValidPosition(board, fallingPiece, adjX=1):
                fallingPiece['x'] += 1
            lastMoveSidewaysTime = time.time()

        if movingDown and time.time() - lastMoveDownTime > MOVEDOWNFREQ and isValidPosition(board, fallingPiece, adjY=1):
            fallingPiece['y'] += 1
            lastMoveDownTime = time.time()

        #Piece falls
        if time.time() - lastFallTime > fallFreq:
            #See if the piece has landed
            if not isValidPosition(board, fallingPiece, adjY=1):
                #Salling piece has landed, set it on the board
                addToBoard(board, fallingPiece)
                score += removeCompleteLines(board)
                level, fallFreq = calculateLevelAndFallFreq(score)
                fallingPiece = None
            else:
                #Piece did not land, just move the piece down
                fallingPiece['y'] += 1
                lastFallTime = time.time()

        #Screen display
        DISPLAYSURF.fill(BGCOLOR)
        drawBoard(board)
        drawStatus(score, level)
        drawNextPiece(nextPiece)
        if fallingPiece != None:
            drawPiece(fallingPiece)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def makeTextObjs(text, font, color):
    surf = font.render(text, True, color)
    return surf, surf.get_rect()


def terminate():
    pygame.quit()
    sys.exit()


def checkForKeyPress():
    #Checks if key is pressed
    checkForQuit()

    for event in pygame.event.get([KEYDOWN, KEYUP]):
        if event.type == KEYDOWN:
            continue
        return event.key
    return None


def showTextScreen(text):
    #Initial text until key is pressed
    titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTSHADOWCOLOR)
    titleRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))
    DISPLAYSURF.blit(titleSurf, titleRect)

    #Draw the text
    titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTCOLOR)
    titleRect.center = (int(WINDOWWIDTH / 2) - 3, int(WINDOWHEIGHT / 2) - 3)
    DISPLAYSURF.blit(titleSurf, titleRect)

    #Draw "Press a key to play."
    pressKeySurf, pressKeyRect = makeTextObjs('Press a key to play.', BASICFONT, TEXTCOLOR)
    pressKeyRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) + 100)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

    while checkForKeyPress() == None:
        pygame.display.update()
        FPSCLOCK.tick()


def checkForQuit():
  #Terminates game if any quit event is pressed
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate() 
        pygame.event.post(event)


def calculateLevelAndFallFreq(score):
    #Increases level
    level = int(score / 10) + 1
    fallFreq = 0.27 - (level * 0.02)
    return level, fallFreq

def getNewPiece():
    #Returns a new piece
    shape = random.choice(list(PIECES.keys()))
    newPiece = {'shape': shape,
                'rotation': random.randint(0, len(PIECES[shape]) - 1),
                'x': int(BOARDWIDTH / 2) - int(TEMPLATEWIDTH / 2),
                'y': -2, # start it above the board (i.e. less than 0)
                'color': random.randint(0, len(COLORS)-1)}
    return newPiece


def addToBoard(board, piece):
    #Fill's into board
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            if PIECES[piece['shape']][piece['rotation']][y][x] != BLANK:
                board[x + piece['x']][y + piece['y']] = piece['color']


def getBlankBoard():
    #Creates new blank board
    board = []
    for i in range(BOARDWIDTH):
        board.append([BLANK] * BOARDHEIGHT)
    return board


def isOnBoard(x, y):
    return x >= 0 and x < BOARDWIDTH and y < BOARDHEIGHT


def isValidPosition(board, piece, adjX=0, adjY=0):
    #True if piece is on board and not colliding
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            isAboveBoard = y + piece['y'] + adjY < 0
            if isAboveBoard or PIECES[piece['shape']][piece['rotation']][y][x] == BLANK:
                continue
            if not isOnBoard(x + piece['x'] + adjX, y + piece['y'] + adjY):
                return False
            if board[x + piece['x'] + adjX][y + piece['y'] + adjY] != BLANK:
                return False
    return True

def isCompleteLine(board, y):
    #True if full line
    for x in range(BOARDWIDTH):
        if board[x][y] == BLANK:
            return False
    return True


def removeCompleteLines(board):
    #Removes completed lines
    numLinesRemoved = 0
    y = BOARDHEIGHT - 1
    while y >= 0:
        if isCompleteLine(board, y):
            #Removes line and pull boxes down
            for pullUpY in range(y, 0, -1):
                for x in range(BOARDWIDTH):
                    board[x][pullUpY] = board[x][pullUpY-1]
            #Sets top line to blank
            for x in range(BOARDWIDTH):
                board[x][0] = BLANK
            numLinesRemoved += 1
        else:
            y -= 1 #Check's next row up
    return numLinesRemoved


def convertToPixelCoords(boxx, boxy):
    return (XMARGIN + (boxx * BOXSIZE)), (TOPMARGIN + (boxy * BOXSIZE))


def drawBox(boxx, boxy, color, pixelx=None, pixely=None):
    #Draw single Techtris piece box
    if color == BLANK:
        return
    if pixelx == None and pixely == None:
        pixelx, pixely = convertToPixelCoords(boxx, boxy)
    pygame.draw.rect(DISPLAYSURF, COLORS[color], (pixelx + 1, pixely + 1, BOXSIZE - 1, BOXSIZE - 1))
    pygame.draw.rect(DISPLAYSURF, LIGHTCOLORS[color], (pixelx + 1, pixely + 1, BOXSIZE - 4, BOXSIZE - 4))


def drawBoard(board):
    #Draws outside border
    pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (XMARGIN - 3, TOPMARGIN - 7, (BOARDWIDTH * BOXSIZE) + 8, (BOARDHEIGHT * BOXSIZE) + 8), 5)

    #Fills in background
    pygame.draw.rect(DISPLAYSURF, BGCOLOR, (XMARGIN, TOPMARGIN, BOXSIZE * BOARDWIDTH, BOXSIZE * BOARDHEIGHT))
    #Draws individual boxes
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            drawBox(x, y, board[x][y])


def drawStatus(score, level):
    #Score
    scoreSurf = BASICFONT.render('Score: %s' % score, True, TEXTCOLOR)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 150, 20)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

    #Level
    levelSurf = BASICFONT.render('Level: %s' % level, True, TEXTCOLOR)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (WINDOWWIDTH - 150, 50)
    DISPLAYSURF.blit(levelSurf, levelRect)


def drawPiece(piece, pixelx=None, pixely=None):
  #Draws pieces by individual boxes
    shapeToDraw = PIECES[piece['shape']][piece['rotation']]
    if pixelx == None and pixely == None:
        pixelx, pixely = convertToPixelCoords(piece['x'], piece['y'])
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            if shapeToDraw[y][x] != BLANK:
                drawBox(None, None, piece['color'], pixelx + (x * BOXSIZE), pixely + (y * BOXSIZE))


def drawNextPiece(piece):
    nextSurf = BASICFONT.render('Next:', True, TEXTCOLOR)
    nextRect = nextSurf.get_rect()
    nextRect.topleft = (WINDOWWIDTH - 120, 80)
    DISPLAYSURF.blit(nextSurf, nextRect)
    drawPiece(piece, pixelx=WINDOWWIDTH-120, pixely=100)


if __name__ == '__main__':
    main()

