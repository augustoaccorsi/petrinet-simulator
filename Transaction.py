class Transaction:
    from Place import Place

    locations = [Place] * 20
    pos = 0
    name = ""
    size = 0

    def __init__(self, name):
        self.name = name

    def addlocation(self, location):
        self.locations[self.pos] = location
        self.pos += 1

    def printtransaction(self):
        print(self.name)
        for i in range (len(self.locations)):
            if self.locations[i].name != "":
                print(self.locations[i].name)
    
    def getname(self):
        return self.name
    
    def setsize(self, size):
        self.size = size