class Place:
    transactions = []
    pos = 0
    def __init__(self, mark):
        self.mark = mark

    def addTransaction(self, transaction):
        self.transactions[self.pos] = transaction
        self.pos += 1