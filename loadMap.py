import os, glob

class load:
    def __init__(self):
        os.chdir("levels")
        self.files = glob.glob("*.map")

        self.map = []

        for self.file in self.files:
            self.f = open(self.file)
            for self.line in self.f:
                self.map.append([])
                for self.character in self.line:
                    self.map[-1].append(self.character)