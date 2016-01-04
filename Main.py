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

# X, Y
player = []

# Set display
screen = pi.display.set_mode((dp_width, dp_height))
pi.display.set_caption('Marsio')

# Holder player image
playerImage = pi.image.load("img/projectile01.png")

# Multithreaded quitting
def Quitter():
    while True:
        for event in pi.event.get():
            if event.type == pi.QUIT:
                pi.quit()
                exit()

# Main program that draws
def Main():
    while True:
        screen.fill((255, 255, 255))
        screen.blit(playerImage)
        pi.display.flip()


# Initialize and start functions
mainThread = Thread(target=Main)
exitThread = Thread(target=Quitter)

mainThread.start()
exitThread.start()