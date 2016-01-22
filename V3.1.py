# This is the proper version that I'm working on!
# Everything is also commented for better editing with others.
# Classes can be moved to new files and then imported if wish
# Current key binds
"""
ESC     |       Quit Game
W       |       Jump
A       |       Move left
D       |       Move Right
SPACE   |       Shoot
"""
import pygame as pi, glob

class Blocks(pi.sprite.Sprite):
    def __init__(self):
        super(Blocks, self).__init__()
        self.image = pi.image.load("img/wall01.png")
        self.rect = self.image.get_rect()

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def move(self, x_speed):
        self.X_direct += x_speed

    def update(self):
        self.rect.x += self.X_direct

    def set_img(self, image):
        self.image = pi.image.load(image)
class Load:
    def __init__(self):
        self.maps = glob.glob("levels/*.map")
        self.mapFiles = []

        for file in self.maps:
            self.mapFiles.append([])
            f = open(file)
            for line in f:
                self.mapFiles[-1].append([])
                for character in line:
                    if character != "\n":
                        self.mapFiles[-1][-1].append(character)

# Class variables that is taken from pygame sprite library
class Player(pi.sprite.Sprite):
    def __init__(self):
        # Creates all of the pygame sprite standard properties
        super(Player, self).__init__()
        # Image based on passed width and height
        self.image = pi.image.load("img/rocketchair05r.png")
        # Position tracking using pygame rect taking in from the image properties
        self.rect = self.image.get_rect()

        # Loads sound effect
        self.sound = pi.mixer.Sound("sounds/effects/jump.wav")

        self.Y_direct = 0
        self.X_direct = 0

    # Used to allow for smoother movement
    def move(self, y_speed, x_speed):
        self.Y_direct += y_speed
        self.X_direct += x_speed

    def update(self, collidable, speed, mapMoveBlocks):
        # Gets all of the collided blocks with the player block and puts it into a list called collidables
        self.rect.x -= self.X_direct
        collision_list = pi.sprite.spritecollide(self, collidable, False)
        for collided_obj in collision_list:
            if self.X_direct < 0:
                self.rect.right = collided_obj.rect.left
                print("Collision on Right")
            if self.X_direct > 0:
                self.rect.left = collided_obj.rect.right
                print("Collision on Left")

        for block in mapMoveBlocks:
            block.rect.x -= speed / 2

        self.rect.y += self.Y_direct

        collision_list = pi.sprite.spritecollide(self, collidable, False)

        for collided_obj in collision_list:
            if self.Y_direct > 0:
                self.rect.bottom = collided_obj.rect.top
            elif self.Y_direct < 0:
                self.rect.top = collided_obj.rect.bottom

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

def remap():
    global dp
    currentX = 0
    currentY = 0
    currentMap = 0
    print(dp)
    for map in range (len(maps.mapFiles)):
        constant = dp.get("height") // len(maps.mapFiles[currentMap])
        for line in range (len(maps.mapFiles[map])):
            for character in range (len(maps.mapFiles[map][line])):
                converted = maps.mapFiles[map][line][character]
                if converted == " ":
                    pass
                elif converted == "x" or converted == "t":
                    maps.mapFiles[map][line][character] = Blocks()
                    maps.mapFiles[map][line][character].set_pos(currentX, currentY)
                    collidable_objects.add(maps.mapFiles[map][line][character])
                    mapMoveBlocks.add(maps.mapFiles[map][line][character])
                    if currentX == 0:
                        pass
                        #print(maps.mapFiles[map][line][character].rect)
                    if map == currentMap:
                        drawables.add(maps.mapFiles[map][line][character])
                if converted == "t":
                    maps.mapFiles[map][line][character].set_img("img/wallfloat01.png")
                currentX += constant
            currentX = 0
            currentY += constant


# Variable that kills program
running = True

speed = 10

# Converts the text arrays into objects
remap()
currentMap = 0

# Main Loop
while running:
    # Event Handler
    for event in pi.event.get():
        if event.type == pi.QUIT:
            running = False
        if event.type == pi.KEYDOWN:
            if event.key == pi.K_SPACE:
                print("space key pressed")

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