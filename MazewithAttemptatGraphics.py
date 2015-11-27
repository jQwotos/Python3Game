__author__ = 'Jason Le'
__email__ = 'le.kent.jason@gmail.com'
import glob, os
from random import randint
import graphics

window = graphics.GraphWin('by Jason Le', 500, 500)
wall = 'x'

def PickMaze():
    os.chdir('MazeFiles')
    mazes = glob.glob('*.txt')
    for file in mazes:
        print(file, end=' | ')
    mazesWanted = randint(0, len(mazes) - 1)
    try:
        print('Selected Maze:', mazes[mazesWanted])
        f = open(mazes[mazesWanted])
        return f
    except:
        print('Darn nabit! The file went rogue!')

def RegMaze(f, blocksize):
    global window
    currentY = 0
    currentX = 0
    blocks = []
    for line in f:
        blocks.append([])
        for character in line:
            if character != '\n':
                blocks[currentY].append(character)
                currentX += 1
        currentY += 1
        currentX = 0
    window.setCoords(-10, len(blocks) + 10, len(blocks[0]) + 10, -10)
    return blocks

def InitdrawGraphics(blocks, playerX, playerY, wall):
    for line in range(len(blocks)):
        for character in range(len(blocks[line])):
            if blocks[line][character] == wall:
                    block = graphics.Rectangle(graphics.Point(character, line), graphics.Point(character -1, line - 1))
                    block.setFill('blue')
                    block.setOutline('blue')
                    block.draw(window)

def playerDraw(playerX, playerY):
    print('Drawing Player')
    Pblock = graphics.Rectangle(graphics.Point(playerX, playerY), graphics.Point(playerX -1, playerY - 1))
    Pblock.setFill('red')
    Pblock.setOutline('red')
    Pblock.draw(window)

def Main():
    blocksize = 2
    blocks = RegMaze(PickMaze(), blocksize)
    playerX = setX(blocks)
    playerY = 0
    InitdrawGraphics(blocks, playerX, playerY, wall)
    return (blocks, playerX, playerY, blocksize)

def movement(blocks, playerX, playerY, wall, blocksize):
    while True:
        playerDraw(playerX, playerY)
        move = input('Enter w a s d to move')
        try:
            if move == 'w' and blocks[playerY - 1][playerX] != wall:
                playerY -= 1
            elif move == 's' and blocks[playerY + 1][playerX] != wall:
                playerY += 1
            elif move == 'a' and blocks[playerY][playerX - 1] != wall:
                playerX -= 1
            elif move == 'd' and blocks[playerY][playerX + 1] != wall:
                playerX += 1
            else:
                print('BLOCKED')
            if len(blocks) - 1 == playerY:
                print('You win!')
                exit()
        except IndexError:
            print('BLOCKED')
        print(playerX, playerY)

def setX(blocks):
    for character in (range(len(blocks[0]))):
        if blocks[0][character] != wall:
            playerX = character
            return playerX

blocks, playerX,  playerY, blocksize = Main()
movement(blocks, playerX, playerY, wall, blocksize)