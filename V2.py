import loadMap,
import pygame as pi
from threading import Thread

pi.init()

displayInfo = pi.display.Info()

dp = {
    "width" : displayInfo.current_w,
    "height" : displayInfo.current_h
}

screen = pi.display.set_mode((dp.get("width"), dp.get("height")))
pi.display.set_caption("Marsio")

# Array is under map.level
map = loadMap.load()

def Main():
    while True:
        for event in pi.event.get():
            if event.type == pi.QUIT():
                pi.quit()
                exit()
            if event.type == pi.KEYDOWN:
                pass