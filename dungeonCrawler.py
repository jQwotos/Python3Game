# </> with <3 by Jason Le for Testing Purposes

import pygame as pi, math

pi.init()

displayInfo = pi.display.Info()

dp = {
    "width" : displayInfo.current_w,
    "height" : displayInfo.current_h
}

dp = {
    "width" : 600,
    "height" : 600
}

screen = pi.display.set_mode((dp.get("width"), dp.get("height")))
pi.display.set_caption("Spooky Scary Trump")

class CreateControls:
    def __init__(self):
        self.up = False
        self.down = False
        self.right = False
        self.left = False

class CreateOffScreen:
    def __init__(self):
        self.x = 0
        self.y = 0

class CreatePlayer:
    def __init__(self):
        self.image = pi.image.load("img/projectile01.png")
        self.offScreen = CreateOffScreen()
        self.controls = CreateControls()

    def draw(self):
        screen.blit(self.rotIMG, (dp.get("width") // 2, dp.get("height") // 2))

    def move(self):
        if

    def rotate(self, mousePOS):
        # Angle line created by user2746752
        self.angle = 360-math.atan2(mousePOS[1]-300,mousePOS[0]-400)*180/math.pi
        self.rotIMG = pi.transform.rotate(self.image, self.angle)
        self.move(self)


def controller(player):
    for event in pi.event.get():
        if event.type == pi.QUIT:
            pi.quit()
            exit()
        if event.type == pi.MOUSEMOTION:
            player.rotate(pi.mouse.get_pos())
        if event.type == pi.KEYDOWN:

def main():
    player = CreatePlayer()
    while True:
        controller(player)
        screen.fill((255, 255, 255))
        player.draw()
        pi.display.flip()

main()