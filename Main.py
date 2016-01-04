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

    'positionOnScreen': pi.Rect((dp_width // 3, dp_height // 3), (dp_width // 10, dp_width // 10))
}

def Globals():
    global player

def controls(contaminated):
    key = chr(contaminated).lower()
    if key == 'w':

    elif key == 's':

    elif key == 'a':

    elif key == 'd':
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