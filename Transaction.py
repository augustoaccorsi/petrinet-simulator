class Transaction:
    palce_list = []
    arcs_in= []
    arcs_out= []
    arcs_list = []
    pos = 0
    name = ""
    size = 0
    enabled = False

    def __init__(self, name):
        self.name = name

    def addlocation(self, location):
        self.palce_list.append(location)
    
    def addarc(self, arc):
        self.arcs_list.append(arc)
    
    def addarcin(self, arc):
        self.arcs_in.append(arc)
    
    def addarcout(self, arc):
        self.arcs_out.append(arc)

    def printtransaction(self):
        print("Transação: "+self.name)
        for i in range (len(self.palce_list)):
            if self.palce_list[i].name != "":
                print(self.palce_list[i].name)
            print(self.size)
        
    def setsize(self, size):
        self.size = size

    def setEnabled(self, enabled):
        self.enabled = enabled