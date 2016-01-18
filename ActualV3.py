# This is the proper version that I'm working on!
# Everything is also commented for better editing with others.
import pygame as pi, os

# Class variables that is taken from pygame sprite library
class Block(pi.sprite.Sprite):
    def __init__(self, width = 64, height = 64):
        # Creates all of the pygame sprite standard properties
        super(Block, self).__init__()
        # Image based on passed width and height
        self.image = pi.image.load("img/wall01.png")
        # Position tracking using pygame rect taking in from the image properties
        self.rect = self.image.get_rect()

        # Loads sound effect
        self.sound = pi.mixer.Sound("sounds/effects/jump.wav")

    # Allows for movement
    def set_pos(self,x ,y):
        # Redefine x
        self.rect.x = x
        # Redefine y
        self.rect.y = y

    # Plays sound effect
    def play(self):
        self.sound.play()

pi.init()

# Game is relative to user's display, so I use these
displayInfo = pi.display.Info()
dp = {
    "width" : displayInfo.current_w,
    "height" : displayInfo.current_h
}

# Set display
screen = pi.display.set_mode((dp.get("width"), dp.get("height")))
pi.display.set_caption("Rocket Trump")

# FPS Limiter Variables
clock = pi.time.Clock()
fps = 60

# Create a group for blocks
block_group = pi.sprite.Group()
# Create block
test_block = Block()
# Move block
test_block.set_pos(dp.get("width") // 2, dp.get("height") // 2)

# Create new block with designated color
tester_block = Block()

# Add blocks to group
block_group.add(test_block, tester_block)
# Draw all blocks in group
block_group.draw(screen)

# Variable that kills program
running = True

while running:
    # Event Handler
    for event in pi.event.get():
        if event == pi.QUIT:
            running = False

    pi.display.update()

    # FPS Limiter
    clock.tick(fps)

pi.quit()
exit()