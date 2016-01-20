import loadSounds, pygame as pi, loadMap, player

pi.init()

displayInfo = pi.display.Info()

dp = {
    "width" : displayInfo.current_w,
    "height" : displayInfo.current_h
}

screen = pi.display.set_mode((dp.get("width"), dp.get("height")))
pi.display.set_caption("Marsio")

# Setup sounds
sound = loadSounds.load()
map = loadMap.load()
player = player.Create()

def Main():
    while True:
        for event in pi.event.get():
            if event.type == pi.QUIT():
                pi.quit()
                exit()
            if event.type == pi.KEYDOWN:
                if event.key == pi.K_SPACE:
                    player.jump()
                if event.key == pi.K_d:
                    player.right = True
                if event.key == pi.K_a:
                    player.left = True
            if event.type == pi.KEYUP:
                if event.key == pi.K_d:
                    player.right = False
                if event.key == pi.K_a:
                    player.left = False

        player.move()

        if player.jumping > 0:
            player.jump()