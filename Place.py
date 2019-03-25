class Place:
    from Transaction import Transaction
    from Arc import Arc
    
    transaction_list = []
    arcs_list = []
    pos = 0
    mark = 0
    name = ""

    def __init__(self, name):
        self.name = name

    def addtransaction(self, transaction):
        #self.transactions[self.pos] = transaction
        #self.pos += 1
        self.transaction_list.append(transaction)
    
    def addarc(self, arc):
        self.arcs_list.append(arc)

    def printplace(self):
        print(self.name)
        print(self.mark)

    def addmark(self, mark):
        self.mark = mark
    
    def gettransactions(self):
        return self.transaction_list