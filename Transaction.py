class Transaction:
    locations = []
    pos = 0

    def addlocation(self, location):
        self.locations[self.pos] = location
        self.pos += 1