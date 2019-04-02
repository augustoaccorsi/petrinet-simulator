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
    with open("file2.txt", 'r') as f:
        for line in f:
            buildobjects(line)

def printDetails():
    print("Rede de Petri inicial")
    print("--------------------------------------------------------------")
    print("Lugares      ", end = " | ")
    for i in range(len(places)):
        print(places[i].name, end = " | ")
    print()
    print("Marcas       ", end = " | ")
    for i in range(len(marks_list)):
        print(" "+str(marks_list[i]), end = " | ")
    print()
    print("--------------------------------------------------------------")
    print("Transação    ", end = " | ")
    for i in range(len(transactions)):
        print(transactions[i].name, end = " | ")
    print()
    print("Habilitdo    ", end = " | ")
    for i in range(len(transactions)):
        if transactions[i].enabled:
            print(" S", end = " | ")
        else:        
            print(" N", end = " | ")
    print("\n--------------------------------------------------------------")
    print("Arcos entrada", end = " | ")
    for i in range(len(arcs_in)):
        print(arcs_in[i].id+":"+str(arcs_in[i].size), end = " | ")
    print()
    print("Arcos saida  ", end = " | ")
    for i in range(len(arcs_out)):
        print(arcs_out[i].id+":"+str(arcs_out[i].size), end = " | ")
    print("\n--------------------------------------------------------------")        

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

def printCicle(num):
    setTransEnable()   
    print("|       "+str(num)+"      ", end = " | ")
    for i in range(len(places)):
        print(" "+str(places[i].mark), end = " | ")
    for i in range(len(transactions)):
        if transactions[i].enabled:
            print(" S", end = " | ")
        else:        
            print(" N", end = " | ")
    print()
    print("---------------------------------------------------------------------------------------------")    

def printPetriNet():
    print("---------------------------------------------------------------------------------------------")
    print("|               |   Quantidades de Marcas em cada Lugar |    Transação hablitada            |")
    print("---------------------------------------------------------------------------------------------")
    print("|   Num ciclo  ", end = " | ")
    for i in range(len(places)):
        print(places[i].name, end = " | ")
    for i in range(len(transactions)):
        print(transactions[i].name, end = " | ")
    print()
    print("---------------------------------------------------------------------------------------------") 

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

userinput = "1" #input("Digite 1 para buscar os dados do arquivo ou 2 para inserir manulamente: ")  

if userinput == "1":
    readFile()
elif userinput == "2":
    print("dois")
else:
    print("tres")
print()
printDetails()
print("\nRede de execução passo a passo\n")

printPetriNet()
i = 0

setTransEnable()  
while stopLoop() == False:
    printCicle(i)
    consume()
    i += 1