class Create:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.relative = 0
        self.jumping = 0
        self.jumpHeight = 50

    def jump(self):
        if self.jumping > 0:
            self.y += 5
        else:
            if self.y > 0:
                self.y -= 8