class Arc:
    size = 0
    transaction = None
    place = None

    def __init__(self, transaction, place, size):
        self.transaction = transaction
        self.place = place
        self.size = size 
    
    def settransaction(self, transaction):
        self.transaction = transaction
    
    def setplace(self, place):
        self.place = place

    def setsize(self, size):
        self.size = size