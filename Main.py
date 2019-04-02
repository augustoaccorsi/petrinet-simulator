import re
from Place import Place
from Transaction import Transaction
from Arc import Arc

places = []
transactions = []
arcs_in = []
arcs_out = []
marks_list =[]
arc_list = []
trans_count = 0
places_count = 0

def getArc(id):
    for i in range(len(arcs_in)):
        arc_list.append(arcs_in[i])
    for i in range(len(arcs_out)):
        arc_list.append(arcs_out[i])

    for i in range(len(arc_list)):
        if arc_list[i].id == id:
            return arc_list[i]
    return Arc

def getPlace(name):
    for i in range(len(places)):
        if places[i].name == name:
            return places[i]
    return False

def getTransaction(name):
    for i in range(len(transactions)):
        if transactions[i].name == name:
            return transactions[i]
    return False

def createplaces(line):
    if re.search(r'[0-9]', line):
            index = re.findall(r'[0-9]', line)
            for i in range(int(index[0])):
                places.append(Place("L"+str(i+1)))

def createtransactions(line):
    if re.search(r'[0-9]', line):
            index = re.findall(r'[0-9]', line)
            for i in range(int(index[0])):
                transactions.append(Transaction("T"+str(i+1)))

def addplacestotransactions(line):
    parts = re.split('(^.*)?\?', line)
    parts = re.split('(^.*)?\?', parts[2])
    place_numbers = re.findall(r'[0-9]', parts[0])
    for i in range(len(place_numbers)):
        place_numbers[i] = "L"+str(place_numbers[i])
    for i in range(len(transactions)):
        if line.find(transactions[i].name) != -1:
            for j in range(len(places)):
                for k in range(len(place_numbers)):
                    if places[j].name == place_numbers[k]:
                        arc = Arc(places[j].name+transactions[i].name, transactions[i], places[j], 1)
                        arcs_in.append(arc)                        
                        transactions[i].addarcin(arc)
                        places[j].addarc(arc)
                        transactions[i].addlocation(places[j])

def addtransactionstoplaces(line):
    parts = re.split('(^.*)?\?', line)
    parts = re.split('(^.*)?\?', parts[2])
    place_numbers = re.findall(r'[0-9]', parts[0])
    for i in range(len(place_numbers)):
        place_numbers[i] = "L"+str(place_numbers[i])
    for i in range(len(transactions)):
        if line.find(transactions[i].name) != -1:
            for j in range(len(places)):
                for k in range(len(place_numbers)):
                    if places[j].name == place_numbers[k]:
                        arc = Arc(transactions[i].name+places[j].name, transactions[i], places[j], 1)
                        arcs_out.append(arc)                        
                        transactions[i].addarcout(arc)
                        places[j].addarc(arc)
                        transactions[i].addlocation(places[j])

def addmarks(line):
    marks = re.split('(^.*)?\?', line)
    place = re.findall(r'[0-9]', marks[1])
    place = "L"+place[0]
    marks = re.split('(^.*)?\?', marks[2])
    marks = int(marks[0])
    for i in range(len(places)):
        if places[i].name == place:
            places[i].addmark(marks)
            marks_list.append(marks)

def addsize(line):
    marks = re.split('(^.*)?\?', line)
    index = re.findall(r'[0-9]', marks[1])
    if line.find("E") != -1:
        arc_id = "L"+index[0]+"T"+index[1]
        size = int(marks[2])
        for i in range(len(arcs_in)):
            if arcs_in[i].id == arc_id:
                arcs_in[i].setsize(size)
    else:
        arc_id = "T"+index[0]+"L"+index[1]
        size = int(marks[2])
        for i in range(len(arcs_out)):
            if arcs_out[i].id == arc_id:
                arcs_out[i].setsize(size)
                
def buildobjects(line):
    if line.find("A") != -1:
        createplaces(line)
    elif line.find("B") != -1:
        createtransactions(line)
    elif line.find("C") != -1:
        addplacestotransactions(line)
    elif line.find("D") != -1:
        addmarks(line)
    elif line.find("E") != -1:
        addsize(line)
    elif line.find("F") != -1:
        addtransactionstoplaces(line)
    elif line.find("G") != -1:
        addsize(line)

def readFile():
    with open("file.txt", 'r') as f:
        for line in f:
            buildobjects(line)

def printDetails(file):
    header = "Rede de Petri inicial"
    header = header+"\n--------------------------------------------------------------"
    data = "Lugares       | "
    for i in range(len(places)):
        data = data + places[i].name + " | "
    print(header)
    data = data+"\nMarcas        | "
    for i in range(len(marks_list)):
        data = data + " "+str(marks_list[i]) + " | "
    data = data + "\n--------------------------------------------------------------"
    data = data + "\nTransação     | "
    setTransEnable()
    for i in range(len(transactions)):
        data = data + transactions[i].name + " | "
    data = data + "\nHabilitdo     | "
    for i in range(len(transactions)):
        if transactions[i].enabled:
            data = data + " S | "
        else:        
            data = data + " N | "
    data = data + "\nArcos entrada | "
    for i in range(len(arcs_in)):
        data = data + arcs_in[i].id+":"+str(arcs_in[i].size) + " | "
    data = data + "\nArcos saida   | "
    for i in range(len(arcs_out)):
        data = data + arcs_out[i].id+":"+str(arcs_out[i].size) + " | "
    data = data + "\n--------------------------------------------------------------"
    print(data)
    file.write(header+"\n")
    file.write(data+"\n")       

def setTransEnable():
    aux1 = 0
    aux2 = 0
    for i in range(len(transactions)):
        for j in range(len(arcs_in)):
            if arcs_in[j].id.find(transactions[i].name) != -1: #conta os arcos de entrada da transação
                aux1 += 1
                arc_size = arcs_in[j].size
                place_marks = arcs_in[j].place.mark
                if place_marks >= arc_size:
                    aux2 += 1
        if aux1 == aux2:
            transactions[i].setEnabled(True)
        else:            
            transactions[i].setEnabled(False)
        aux1 = 0
        aux2 = 0

def stopLoop():
    for i in range(len(transactions)):
        if transactions[i].enabled:
            return False
    return True

def printCicle(num, file):
    setTransEnable() 
    data = "|       "+str(num)+"      "+" | "
    for i in range(len(places)):
        data = data+" "+str(places[i].mark) + " | "
    for i in range(len(transactions)):
        if transactions[i].enabled:
            data = data + " S | "
        else:        
            data = data + " N | "
    data = data + "\n---------------------------------------------------------------------------------------------"
    print(data)
    file.write(data+"\n")

def printPetriNet(file):
    header = "\nRede de execução passo a passo\n"
    header = header +"---------------------------------------------------------------------------------------------"
    header = header + "\n|               |   Quantidades de Marcas em cada Lugar |    Transação hablitada            |"
    header = header + "\n---------------------------------------------------------------------------------------------"
    print(header)
    data = "|   Num ciclo   | "
    for i in range(len(places)):
        data = data + places[i].name + " | "
    for i in range(len(transactions)):
        data = data + transactions[i].name + " | "
    print(data)
    footer = "---------------------------------------------------------------------------------------------"
    print(footer)
    file.write(header+"\n")
    file.write(data+"\n")
    file.write(footer+"\n")

def consume(): #executa passo a passo a rede de petri
    for i in range(len(transactions)):
        if transactions[i].enabled:
            arcs = transactions[i].arcs_in
            for j in range(len(arcs)):
                if arcs[j].id.find(transactions[i].name) != -1:
                   place = arcs[j].place
                   place.mark = place.mark - arcs[j].size
                   arcs[j].addplace(place) #ajusta a nova marca do lugar
            arcs = transactions[i].arcs_out
            for j in range(len(arcs)):
                if arcs[j].id.find(transactions[i].name) != -1:
                   place = arcs[j].place
                   place.mark = place.mark + arcs[j].size
                   arcs[j].addplace(place) #ajusta a nova marca do lugar

readFile()

file = open('output.txt', 'w')
printDetails(file)
printPetriNet(file)
i = 0
  
while stopLoop() == False:
    printCicle(i, file)
    consume()
    i += 1


file.close()