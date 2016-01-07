# </> with <3 by Jason Le
# This is my implementation of dem cool classes

import pygame, loadMap
from threading import Thread

pygame.init()

displayInfo = pygame.display.Info()

dp = {
    "width" : displayInfo.current_w,
    "height" : displayInfo.current_h
}

screen = pygame.display.set_mode((dp.get("width"), dp.get("height")))
pygame.display.set_caption("Marsio")

# Array is under map.level
map = loadMap.load()