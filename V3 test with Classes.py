# </> with <3 by Jason Le
# This is me poking around with classes on Python

class CreatePlayer:
    def __init__(self):
        self.y = 5

    def jump(self):
        print("hop")

player = CreatePlayer()
player.jump()
print(player.y)