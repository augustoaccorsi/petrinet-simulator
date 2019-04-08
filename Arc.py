class Arc:
    id = ""
    size = 0
    transition = None
    place = None

    def __init__(self, id, transition, place, size):
        self.id = id
        self.transition = transition
        self.place = place
        self.size = size
            
    def addtransition(self, transition):
        self.transition = transition
    
    def addplace(self, place):
        self.place = place

    def setsize(self, size):
        self.size = size