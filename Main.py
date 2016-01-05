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

# Player info
player = {
    'image': pi.image.load("img/projectile01.png"),
    'positionOffScreen': pi.Rect(()),
    'positionOnScreen': pi.Rect((dp_width // 3, dp_height // 3), (dp_width // 10, dp_width // 10))
}

moveAmount = 5

def Globals():
    global player
    global moveAmount

def controls(contaminated):
    key = chr(contaminated).lower()
    if key == 'w':
        player['positionOnScreen'].move(0, moveAmount)
    elif key == 's':
        player['positionOnScreen'].move(0, -1 * moveAmount)
    elif key == 'a':
        player['positionOnScreen'].move(-1 * moveAmount, 0)
    elif key == 'd':
        player['positionOnScreen'].move(0, moveAmount)

# Multithreaded quitting
def Quitter():
    while True:
        for event in pi.event.get():
            if event.type == pi.QUIT:
                Main.stop()
                pi.quit()
                exit()
            if event.type == pi.KEYDOWN:
                controls(event.key)

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