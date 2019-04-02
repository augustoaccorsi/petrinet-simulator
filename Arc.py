class Arc:
    id = ""
    size = 0
    transaction = None
    place = None

    def __init__(self, id, transaction, place, size):
        self.id = id
        self.transaction = transaction
        self.place = place
        self.size = size
            
    def addtransaction(self, transaction):
        self.transaction = transaction
    
    def addplace(self, place):
        self.place = place

    def setsize(self, size):
        self.size = size