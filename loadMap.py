import os, glob

class load:
    def __init__(self):
        os.chdir("levels")
        files = glob.glob("*.map")

        self.map = []

        for file in files:
            f = open(self.file)
            for line in f:
                self.map.append([])
                for character in line:
                    self.map[-1].append(character)

        for x in self.map: