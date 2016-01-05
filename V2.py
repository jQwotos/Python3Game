# </> with <3 by Jason Le
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

player = {
    "image" : pygame.image.load('img/trump mount open head.jpg'),
    "onScreen" : {"x": dp.get("width") // 3, "y": dp.get("height") // 3},
    "offScreen" : 0,
    "jumping" : False
}

global player

def Jumper():
    for x in range(10):
        player["onScreen"]["y"] += 1
    for x in range(10):
        player["onScreen"]["y"] -= 1
    player["jumping"] = False

def draw(object, x, y):
    screen.blit(object, (x, y))

def jump():
    if player.get["jumping"] == False:
        player["jumping"] = True
        Thread(target=Jumper).start()

def controlScheme():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump()

def main():
    while True:
        controlScheme()
        # Holder white background
        screen.fill((255, 255, 255))
        draw(player.get("image"), player.get("onScreen").get("x"), player.get("onScreen").get("y"))
        pygame.display.flip()

main()
