class Place:    
    transaction_list = []
    arcs_list = []
    pos = 0
    mark = 0
    name = ""

    def __init__(self, name):
        self.name = name

    def addtransaction(self, transaction):
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