class Place:
    transactions = [None] * 20
    pos = 0
    mark = 0
    name = ""
    def __init__(self, name):
        self.name = name

    def addTransaction(self, transaction):
        self.transactions[self.pos] = transaction
        self.pos += 1

    def printPlace(self):
        print(self.name)

    def addMark(self, mark):
        self.mark = mark