import glob, pygame as pi, os

class load:
    # Loads files on import initialization
    def __init__(self):
        os.chdir("music")
        self.files = glob.glob("*.mp3")
        for self.i in range(len(self.files)):
            self.files[self.i] = pi.mixer.Sound(self.files[self.i])

    # Play clone
    def play(self, sound):
        if sound in self.files:
            self.files(sound).play()