import re

def readFile():
    filename = "file.txt"
    file = open(filename, "r")
    
    locations = []
    transactions = []

    str = file.readlines(1)
    print(str)

#def getData():
    #receber dados do usuário

userinput = input("Digite 1 para buscar os dados do arquivo ou 2 para inserir manulamente: ")  

if userinput == "1":
    readFile()
elif userinput == "2":
    print("dois")
else:
    print("tres")
