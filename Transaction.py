class Transaction:
    locations = []
    pos = 0

    def addlocations(self, location):
        self.locations[self.pos] = location
        self.pos += 1