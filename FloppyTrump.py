# This game will scale to your display resolution!
# There is sound! So put on your headphones.
# Idea and sound by Justin; Maps and keystroke input by Ricky; Pictures and map modifications by Patrick; Backend by Jason
"""
ESC     |       Quit Game
W       |       Move up
A       |       Move left
D       |       Move Right
S       |       Move down
Q       |       Restart
"""
import pygame as pi, glob
from random import randint

class Blocks(pi.sprite.Sprite):
    def __init__(self, image):
        super(Blocks, self).__init__()
        self.image = pi.transform.scale(pi.image.load(image), (dp.get("height") // len(maps.mapFiles[maps.currentMap]), dp.get("height") // len(maps.mapFiles[maps.currentMap])))
        self.rect = self.image.get_rect()

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def move(self, x_speed):
        self.X_direct += x_speed

    def update(self):
        self.rect.x += self.X_direct

class Load:
    def __init__(self):
        self.maps = glob.glob("levels/*.map")
        self.mapFiles = []
        self.mapLength = []
        self.currentMap = 0

        for file in self.maps:
            self.mapFiles.append([])
            f = open(file)
            for line in f:
                self.mapFiles[-1].append([])
                for character in line:
                    if character != "\n":
                        self.mapFiles[-1][-1].append(character)

class Sound:
    def __init__(self):
        pi.mixer.init()
        self.soundQuotes = glob.glob("sounds/quotes/*")
        self.music = glob.glob("sounds/music/*")
        self.background = pi.mixer.Sound(self.music[randint(0, len(self.music) - 1)])
        self.background.set_volume(.1)
        self.background.play(9)

    def death(self):
        pi.mixer.music.load(self.soundQuotes[randint(0, len(self.soundQuotes) - 1)])
        pi.mixer.music.play()

sounder = Sound()
# Class variables that is taken from pygame sprite library
class Player(pi.sprite.Sprite):
    def __init__(self):
        # Creates all of the pygame sprite standard properties
        super(Player, self).__init__()
        # Image based on passed width and height
        self.image = pi.transform.scale(pi.image.load("img/rocketchair05r.png"), (dp.get("height") // len(maps.mapFiles[maps.currentMap]), dp.get("height") // len(maps.mapFiles[maps.currentMap])))
        # Position tracking using pygame rect taking in from the image properties
        self.rect = self.image.get_rect()


        self.Y_direct = 0
        self.X_direct = 0

        self.total_x = 0

        self.relative_x = 0

    # Used to allow for smoother movement
    def move(self, y_speed, x_speed):
        self.Y_direct += y_speed
        self.X_direct += x_speed

    def kill(self, mapMoveBlocks, won = False):
        run = True
        print("I died, oh no!")
        for block in mapMoveBlocks:
            block.rect.x -= self.total_x
        self.set_pos(dp.get("height") // 2, dp.get("width") // 5)
        self.X_direct = 0
        self.Y_direct = 0
        self.relative_x = 0
        if won:
            maps.currentMap += 1
            remapper.__init__()
        sounder.death()

        while run:
            for event in pi.event.get():
                if event.type == pi.KEYDOWN:
                    if event.key == pi.K_q:
                        run = False
                    if event.key == pi.K_ESCAPE:
                        print("User requested to kill program by pressing ESC")
                        pi.quit()
                        exit()
        self.total_x = 0
        print("Respawned")


    def update(self, collidable, speed, mapMoveBlocks):
        # Gets all of the collided blocks with the player block and puts it into a list called collidables
        self.rect.x -= self.X_direct
        self.relative_x -= self.X_direct
        self.rect.y += self.Y_direct
        collision_list = pi.sprite.spritecollide(self, collidable, False)
        if len(collision_list) > 0 or self.rect.y > dp.get("height") or self.rect.y < 0 or self.rect.x < 0 or self.rect.x > dp.get("width"):
            self.kill(mapMoveBlocks)

        for block in mapMoveBlocks:
            block.rect.x -= speed / 2
        self.total_x -= speed / 2
        self.relative_x += speed / 2

        if self.relative_x > remapper.totalX:
            self.kill(mapMoveBlocks, True)


    # Here for the peps to use, updates the player position
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

# Load all levels into maps variable
maps = Load()

# Set display
screen = pi.display.set_mode((dp.get("width"), dp.get("height")))
pi.display.set_caption("Rocket Trump")

# FPS Limiter Variables
clock = pi.time.Clock()
fps = 60

# Create a group for blocks
drawables = pi.sprite.Group()
# Create block
player = Player()

# Add blocks to group
drawables.add(player)

collidable_objects = pi.sprite.Group()
mapMoveBlocks = pi.sprite.Group()

class Remap:
    def __init__(self):
        global dp
        currentX = 0
        currentY = 0
        self.totalX = 0
        currentLine = 0
        collidable_objects.empty()
        drawables.empty()
        drawables.add(player)
        constant = dp.get("height") // len(maps.mapFiles[maps.currentMap])
        for line in range (len(maps.mapFiles[maps.currentMap])):
            for character in range (len(maps.mapFiles[maps.currentMap][line])):
                converted = maps.mapFiles[maps.currentMap][line][character]
                if converted == " ":
                    pass
                elif converted == "x" or converted == "t":
                    if converted == "x":
                        maps.mapFiles[maps.currentMap][line][character] = Blocks("img/wall01.png")
                    if converted == "t":
                        maps.mapFiles[maps.currentMap][line][character] = Blocks("img/wallfloat01.png")
                    maps.mapFiles[maps.currentMap][line][character].set_pos(currentX, currentY)
                    collidable_objects.add(maps.mapFiles[maps.currentMap][line][character])
                    mapMoveBlocks.add(maps.mapFiles[maps.currentMap][line][character])
                    drawables.add(maps.mapFiles[maps.currentMap][line][character])
                currentX += constant
                if currentLine == 0:
                    self.totalX += constant
            currentLine += 1
            currentX = 0
            currentY += constant
        print(self.totalX)

# Variable that kills program
running = True

speed = 10

# Converts the text arrays into objects
remapper = Remap()
currentMap = 0

# Main Loop
while running:
    # Event Handler
    for event in pi.event.get():
        if event.type == pi.QUIT:
            running = False
        if event.type == pi.KEYDOWN:
            # Kill program when ESC key is pressed
            if event.key == pi.K_ESCAPE:
                print("User requested to kill program by pressing ESC")
                running = False
            # Key movement, - when moving up and to the left, + when moving down and to the right
            if event.key == pi.K_a:
                player.move(0, speed)
            if event.key == pi.K_d:
                player.move(0, -1 * speed)
            if event.key == pi.K_w:
                player.move(-1 * speed , 0)
            if event.key == pi.K_s:
                player.move(speed, 0)

        if event.type == pi.KEYUP:
            if event.key == pi.K_a:
                player.move(0, -1 * speed)
            if event.key == pi.K_d:
                player.move(0, speed)
            if event.key == pi.K_w:
                player.move(speed , 0)
            if event.key == pi.K_s:
                player.move(-1 * speed, 0)
    player.update(collidable_objects, speed, mapMoveBlocks)

    # Draw all blocks on screen
    screen.fill((255, 255, 255))
    drawables.draw(screen)
    # Equiv of flip, updates the display
    pi.display.flip()

    # FPS Limiter
    clock.tick(fps)

pi.quit()
exit()