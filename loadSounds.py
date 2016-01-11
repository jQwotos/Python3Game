import glob, pygame as pi, os

class load:
    # Loads files on import initialization
    def __init__(self):
        os.chdir("music")
        self.files = glob.glob("*.mp3")

    # Play clone
    def play(self, sound):
