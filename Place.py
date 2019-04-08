class Place:    
    transition_list = []
    arcs_list = []
    pos = 0
    mark = 0
    name = ""

    def __init__(self, name):
        self.name = name

    def addtransition(self, transition):
        self.transition_list.append(transition)
    
    def addarc(self, arc):
        self.arcs_list.append(arc)

    def printplace(self):
        print(self.name)
        print(self.mark)

    def addmark(self, mark):
        self.mark = mark
    
    def gettransitions(self):
        return self.transition_list