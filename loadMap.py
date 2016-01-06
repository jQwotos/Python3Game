# </> with <3 by Jason Le
class load:
    def __init__(self):
        try:
            self.f = open("levels/1.map")
        except:
            print("Unable to load map")

        self.map = []

        for self.line in self.f:
            self.map.append([])
            for self.character in self.line:
                self.map[-1].append(self.character)