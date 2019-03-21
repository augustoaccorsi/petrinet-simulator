class Transaction:
    locations = [None] * 20
    pos = 0
    name = ""
    def __init__(self, name):
        self.name = name

    def addlocation(self, location):
        self.locations[self.pos] = location
        self.pos += 1

    def printtransaction(self):
        print(self.name)
    
    def getname(self):
        return self.name