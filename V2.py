# </> with <3 by Jason Le
# This is my implementation of dem cool classes

import pygame
from threading import Thread

pygame.init()

displayInfo = pygame.display.Info()

dp = {
    "width" : displayInfo.current_w,
    "height" : displayInfo.current_h
}

screen = pygame.display.set_mode((dp.get("width"), dp.get("height")))
pygame.display.set_caption("Marsio")

class CreateOnScreen:
    def __init__(self):
        self.x = dp.get("width") // 3
        self.y = dp.get("height") // 3

class CreatePlayer:
    def __init__(self):
        try:
            self.image = pygame.image.load("img/projectile01.png")
        except:
            print("Unable to load image")
        self.jumping = 0
        self.offScreen = 0
        self.onScreen = CreateOnScreen()

    def fall(self):
        if self.onScreen.y <= dp.get("height") // 3 and self.jumping == 0:
            self.onScreen.y += 1
        print(self.onScreen.y)

    def jump(self):
        if self.jumping == 0:
            self.jumping = 50

def draw(object, x, y):
    screen.blit(object, (x, y))

def controlScheme(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player.jumping == False:
                player.jump()
        if player.jumping > 0:
            player.onScreen.y += 1
    player.fall()

def main():
    player = CreatePlayer()
    while True:
        controlScheme(player)
        # Holder white background
        screen.fill((255, 255, 255))
        draw(player.image, player.onScreen.x, player.onScreen.y)
        pygame.display.flip()

main()
