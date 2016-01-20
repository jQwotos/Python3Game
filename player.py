import pygame as pi
class Create:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.relative = 0
        self.jumping = 0
        self.jumpHeight = 50
        self.left = False
        self.right = False
        self.speed = 5
        self.image = pi.image.load("img/rocketchair05r.png")

    def jump(self):
        if self.jumping > 0:
            self.y += 5
        else:
            if self.y > 0:
                self.y -= 8

    def move(self):
        if self.left == True:
            self.x += self.speed
        if self.right == True:
            self.x -= self.speed

        map