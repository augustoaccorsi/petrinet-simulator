class Arc:
    id = 0
    size = 0
    transaction = None
    place = None
    et = None

    def __init__(self, id, transaction, place, size, et):
        self.id = id
        self.transaction = transaction
        self.place = place
        self.size = size 
        self.et = et
    
    def settransaction(self, transaction):
        self.transaction = transaction
    
    def setplace(self, place):
        self.place = place

    def setsize(self, size):
        self.size = size
    
    def setet(self, et):
        self.et = et
