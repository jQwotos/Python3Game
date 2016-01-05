# </> with <3 by Jason, Patrick, Ricky and Justin
import pygame as pi
from threading import Thread

pi.init()

# Get display info
displayInfo = pi.display.Info()
# Display width
dp_width = displayInfo.current_w
# Display height
dp_height = displayInfo.current_h

# Set display
screen = pi.display.set_mode((dp_width, dp_height))
pi.display.set_caption('Marsio')

moveAmount = 5

# Player info
player = {
    'image': pi.image.load("img/projectile01.png"),
    'positionOnScreen': pi.Rect((dp_width // 3, dp_height // 3), (dp_width // 10, dp_width // 10))
    'movement': {'w': {'move': False,
                       'direction': [0, -1 * moveAmount]},
                 's': {'move': False,
                       'direction': [0, moveAmount]},
                 'a': {'move': False,
                       'direction': [-1 * moveAmount, 0]},
                 'd': {'move': False,
                       'direction': [moveAmount, 0]}}
}

def Globals():
    global player

def controls(contaminated):
    while True:
        for i in player['movement']:
            if player['movement'][i]['move'] == True:
                player['playerOnScreen'] = player['playerOnScreen'].move(player['movement'][i]['direction'][0], player['movement'][i]['direction'][1])

# Multithreaded quitting
def Quitter():
    while True:
        for event in pi.event.get():
            if event.type == pi.QUIT:
                Main.stop()
                pi.quit()
                exit()
            if event.type == pi.KEYDOWN:
                if chr(event.key).lower() in player['movement']:
                    player['movement'][chr(event.key).lower()]['move'] = True
            if event.type == pi.KEYUP:
                    player['movement'][chr(event.key).lower()]['move'] = True
# Main program that draws
def Main():
    while True:
        screen.fill((255, 255, 255))
        screen.blit(player.get("image"), player.get("positionOnScreen"))
        pi.display.flip()

Globals()

# Initialize and start functions
mainThread = Thread(target=Main)
exitThread = Thread(target=Quitter)

mainThread.start()
exitThread.start()