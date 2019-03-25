class Place:
    from Transaction import Transaction
    from Arc import Arc
    
    transactions = [Transaction] * 20
    arcs = [Arc] * 20
    pos = 0
    mark = 0
    name = ""
    def __init__(self, name):
        self.name = name

    def addtransaction(self, transaction):
        self.transactions[self.pos] = transaction
        self.pos += 1
    
    def addarc(self, arc):
        self.arcs[self.pos] = arc 
        self.pos += 1

    def printplace(self):
        print(self.name)
        print(self.mark)

    def addmark(self, mark):
        self.mark = mark
    
    def gettransactions(self):
        return self.transactions