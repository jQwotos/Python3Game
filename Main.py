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

moveAmount = 1

# Player info
player = {
    'image': pi.image.load("img/projectile01.png"),
    'positionOnScreen': pi.Rect((dp_width // 3, dp_height // 3), (dp_width // 10, dp_width // 10)),
    'movement': {'w': {'move': False,
                       'direction': [0, -1 * moveAmount]}}
}

def Globals():
    global player

def jump():
    player['positionOnScreen'] = player['positionOnScreen'].move(player['movement']['w']['direction'][0], player['movement']['w']['direction'][1])

# Multithreaded quitting
def controlScheme():
    for event in pi.event.get():
        if event.type == pi.QUIT:
            pi.quit()
            exit()
        if event.type == pi.KEYDOWN:
            if chr(event.key).lower() == 'w':
                jump()
# Main program that draws
def Main():
    while True:
        controlScheme()
        screen.fill((255, 255, 255))
        screen.blit(player.get("image"), player.get("positionOnScreen"))
        pi.display.flip()

Globals()
Main()