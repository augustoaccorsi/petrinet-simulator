import re
from Place import Place
from Transaction import Transaction

places = [Place] * 20
transactions = [Transaction] * 20

def buildObjects(line):
    if line.find("A") != -1:
        if re.search(r'[0-9]', line):
            index = re.findall(r'[0-9]', line)
            for i in range(int(index[0])):
                places[i] = Place("L"+str(i+1))
                places[i].printPlace()
    elif line.find("B") != -1:
        if re.search(r'[0-9]', line):
            index = re.findall(r'[0-9]', line)
            for i in range(int(index[0])):
                transactions[i] = Transaction("T"+str(i+1))
                transactions[i].printTransaction()

#A Quantos lugares: 3
#B Quantas transicoes: 2
#C Quais são os lugares de entrada de T1? 1, 3
#C Quais são os lugares de entrada de T2? 2, 3
#D Quantas marcas em L1 ? 10
#D Quantas marcas em L2 ? 4
#D Quantas marcas em L3 ? 0
#E Qual o peso do arco de L1 para T1 ? 1
#E Qual o peso do arco de L3 para T1 ? 2




def readFile():
    with open("file.txt", 'r') as f:
        for line in f:
            buildObjects(line)

#    str = file.readlines(1)
#    print(str)

#    for i in range(3):
#        a = Place(4)
#        places[i] = a
#        places[i].printPlace()



#def getData():
    #receber dados do usuário

userinput = input("Digite 1 para buscar os dados do arquivo ou 2 para inserir manulamente: ")  

if userinput == "1":
    readFile()
elif userinput == "2":
    print("dois")
else:
    print("tres")
