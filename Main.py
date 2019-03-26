import re
from Place import Place
from Transaction import Transaction
from Arc import Arc

places = []
transactions = []
arcs = []
marks_list =[]
trans_count = 0
places_count = 0

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
                        arcs.append(arc)                        
                        transactions[i].addarcin(arc)
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
    arc_id = "L"+index[0]+"T"+index[1]
    size = int(marks[2])
    for i in range(len(arcs)):
        if arcs[i].id == arc_id:
            arcs[i].setsize(size)

                
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

def readFile():
    with open("file.txt", 'r') as f:
        for line in f:
            buildobjects(line)

def prinPetriNet():
    print("Lugares   ", end = " | ")
    for i in range(len(places)):
        print(places[i].name, end = " | ")
    print()
    print("Marcas    ", end = " | ")
    for i in range(len(marks_list)):
        print(marks_list[i], end = " | ")
    print()
    print("Transação ", end = " | ")
    for i in range(len(transactions)):
        print(transactions[i].name, end = " | ")
    print()
    print("Habilitdo ", end = " | ")
    for i in range(len(transactions)):
        if transactions[i].enabled:
            print("S", end = " | ")
        else:        
            print("N", end = " | ")
    

def consume(): #executa passo a passo a rede de petri
    for i in range(len(places)):
        arc_list = places[i].arcs_list
        for j in range(len(arc_list)):
            size = arc_list[j].size

userinput = input("Digite 1 para buscar os dados do arquivo ou 2 para inserir manulamente: ")  

if userinput == "1":
    readFile()
elif userinput == "2":
    print("dois")
else:
    print("tres")
print()
print("Rede de Petri inicial-----------------------------------------")
prinPetriNet()
print("\n--------------------------------------------------------------")

#consume()
