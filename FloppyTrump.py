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
# Import pygame as pi, because pygame is too long; Glob is a module that I use to gather list of files
import pygame as pi, glob
# I only want randint from random
from random import randint

# I truly love clases, no need to deal with globals! Blocks is used for every block that you see
class Blocks(pi.sprite.Sprite):
    def __init__(self, image):
        # Great command, it initializes a template of pygame's sprites
        super(Blocks, self).__init__()
        # Lets load it's image and here comes the relativity code! Convert the size of the image to match display specs!
        self.image = pi.transform.scale(pi.image.load(image), (dp.get("height") // len(maps.mapFiles[maps.currentMap]), dp.get("height") // len(maps.mapFiles[maps.currentMap])))
        # Create a rect which is basically a x, y, width, height system
        self.rect = self.image.get_rect()

    # This is an extra function that allows to reset the positions of the block
    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    # Move the blocks side to side, no need for up and down
    def move(self, x_speed):
        self.X_direct += x_speed

    # Actuall update the position of the block
    def update(self):
        self.rect.x += self.X_direct

# Basic loading
class Load:
    def __init__(self):
        # Puts all files into an array
        self.maps = glob.glob("levels/*.map")
        # Creates a blank array for the letters that will have to be stored
        self.mapFiles = []
        # Creates an array for the length of each map
        self.mapLength = []
        # Variable for maps
        self.currentMap = 0

        # Let's start to register the maps into the mapFiles array!
        for file in self.maps:
            # Sub array!
            self.mapFiles.append([])
            # Open dat file
            f = open(file)
            # Now we actually convert the files into to array
            for line in f:
                self.mapFiles[-1].append([])
                for character in line:
                    if character != "\n":
                        self.mapFiles[-1][-1].append(character)

# Yea, I love classes that much. Even made a sound class...
class Sound:
    def __init__(self):
        # Initialize the mixer module from the pygame library
        pi.mixer.init()
        # Gather quotes
        self.soundQuotes = glob.glob("sounds/quotes/*")
        # Gather background music
        self.music = glob.glob("sounds/music/*")
        # Load the file into a background variable
        self.background = pi.mixer.Sound(self.music[randint(0, len(self.music) - 1)])
        # Lower the volume of the background variable
        self.background.set_volume(.1)
        # Play the music
        self.background.play(9)

    def death(self):
        # Death, erm it doesn't actually mean you died, but it just plays a random quote from the quote box
        pi.mixer.music.load(self.soundQuotes[randint(0, len(self.soundQuotes) - 1)])
        pi.mixer.music.play()

# Lets create a variable for our presious sound class
sounder = Sound()
# Now, to the madness that is the player class
class Player(pi.sprite.Sprite):
    def __init__(self):
        # Creates all of the pygame sprite standard properties
        super(Player, self).__init__()
        # Image based on passed width and height
        self.image = pi.transform.scale(pi.image.load("img/rocketchair05r.png"), (dp.get("height") // len(maps.mapFiles[maps.currentMap]), dp.get("height") // len(maps.mapFiles[maps.currentMap])))
        # Position tracking using pygame rect taking in from the image properties
        self.rect = self.image.get_rect()
        # Movement direction of Y
        self.Y_direct = 0
        # Movement direction of X
        self.X_direct = 0
        # Total x movement, this is outdated and can be replaced with relative_x movement. It stores the data registered to see how much it has to move blocks back
        self.total_x = 0
        # Relative x movement, this is used to calculate a win
        self.relative_x = 0

    # Used to allow for smoother movement
    def move(self, y_speed, x_speed):
        self.Y_direct += y_speed
        self.X_direct += x_speed

    # Oh no! I died, not really. I found out about using an = during a function pass to avoid errors and it allows for a standard to be set unless given
    def kill(self, mapMoveBlocks, won = False):
        run = True
        # Dev line
        print("I died, oh no!")
        # Move every block back to original position
        for block in mapMoveBlocks:
            block.rect.x -= self.total_x
        # Reset the position of the player
        self.set_pos(dp.get("height") // 2, dp.get("width") // 5)
        # Reset the movement of the player
        self.X_direct = 0
        self.Y_direct = 0
        # Reset the relative x, which is used for detecting a win
        self.relative_x = 0
        # If the player actually won
        if won:
            # Move to next map
            maps.currentMap += 1
            # Register next map
            remapper.__init__()
        # Play that quote!
        sounder.death()
        # Now we wait for the player to press q to allow the program to continue
        while run:
            for event in pi.event.get():
                if event.type == pi.KEYDOWN:
                    if event.key == pi.K_q:
                        run = False
                    if event.key == pi.K_ESCAPE:
                        print("User requested to kill program by pressing ESC")
                        pi.quit()
                        exit()
        # Reset total x, explained above
        self.total_x = 0
        print("Respawned")


    def update(self, collidable, speed, mapMoveBlocks):
        # Move the player forward and backward
        self.rect.x -= self.X_direct
        # Increase the relative x, which is still used to detect a win
        self.relative_x -= self.X_direct
        # Move the player up and down
        self.rect.y += self.Y_direct
        # Gets all of the collided blocks with the player block and puts it into a list called collidables
        collision_list = pi.sprite.spritecollide(self, collidable, False)
        # If the player touches a block or goes out of the screen, MURDER THE PLAYER
        if len(collision_list) > 0 or self.rect.y > dp.get("height") or self.rect.y < 0 or self.rect.x < 0 or self.rect.x > dp.get("width"):
            self.kill(mapMoveBlocks)

        # move the map forward slowl
        for block in mapMoveBlocks:
            block.rect.x -= speed / 2
        # more replativity code and checking
        self.total_x -= speed / 2
        self.relative_x += speed / 2

        # This is what we have been building up for! This checks if the player wins! Too bad it's only a sad two lines...
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

collidable_objects = pi.sprite.Group()
mapMoveBlocks = pi.sprite.Group()

# Don't, don't even look at this madness
class Remap:
    def __init__(self):
        # Grabs the display variables
        global dp
        # Local currentX variable that does not need to be affected by others it represents the relative symbol to a position on the map
        currentX = 0
        # same as currentX but with verticle position
        currentY = 0
        # TotalX is used to detect a win, it represents the length of a map
        self.totalX = 0
        # Assistance to totalx
        currentLine = 0
        # clear out the colidable_objects sprite group
        collidable_objects.empty()
        # clear out the drawabales sprite group
        drawables.empty()
        # add the player to the group
        drawables.add(player)
        # Fetch a constant because i'm too lazy to re-write this line many times, and it speeds up the program ever so slightly
        constant = dp.get("height") // len(maps.mapFiles[maps.currentMap])
        # Lets begin the madness
        for line in range (len(maps.mapFiles[maps.currentMap])):
            for character in range (len(maps.mapFiles[maps.currentMap][line])):
                converted = maps.mapFiles[maps.currentMap][line][character]
                if converted == "x" or converted == "t":
                    if converted == "x":
                        # This is how we set the image, X represents a wall block
                        maps.mapFiles[maps.currentMap][line][character] = Blocks("img/wall01.png")
                    if converted == "t":
                        # T represents a floaty block
                        maps.mapFiles[maps.currentMap][line][character] = Blocks("img/wallfloat01.png")
                    # change the position of the block
                    maps.mapFiles[maps.currentMap][line][character].set_pos(currentX, currentY)
                    # add it co collidable_objects sprite group, honestly, most of these groups are useless. This was made very early on and I wanted to experiment
                    collidable_objects.add(maps.mapFiles[maps.currentMap][line][character])
                    # add it to the mapMoveBlocks sprite group
                    mapMoveBlocks.add(maps.mapFiles[maps.currentMap][line][character])
                    # add it to the drawables sprite group
                    drawables.add(maps.mapFiles[maps.currentMap][line][character])
                # We have passed a single character yay!
                currentX += constant
                # If we are on line 0, then let's count
                if currentLine == 0:
                    self.totalX += constant
            # Add to helper
            currentLine += 1
            # Reset X position
            currentX = 0
            # We moved down vertically once!
            currentY += constant

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
    # This moves the block and checks everything
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