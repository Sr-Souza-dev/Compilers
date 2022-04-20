import re

reserved        = ["if", "while", "const", "cout", "int", "char", "float", "string", "else", "include", "using", "namespace","std", "return","#", "true", "false", "iostream", "getchar"]
assignment      = ["<<",">>","="]
delimiters      = ["{","}","(",")","[","]", ";", ","]
operator        = ["+","-","*","/"]
comparation     = ["==","<=",">=","!=", "<", ">"]

arq = open("calc.cpp", "r")
tokens = []

def separate(word):
    for item in re.findall(r'(\w*|<<|==|<=|>=|!=|\W)',word):
        item = item.strip()     

        if(item != ""):
            tokens.append(item)

def printFormated(item, type):
    item += "  "
    while(len(item) < 62):
        item += "-"

    print(f"{item:63} -> {type:25}")


def categorize(tokens):
   
    for item in tokens:



        if   (item in reserved):        printFormated(item, "Reservada")
        elif (item in assignment):      printFormated(item, "Atribuição")
        elif (item in delimiters):      printFormated(item, "Delimitadores")
        elif (item in operator):        printFormated(item, "Operador")
        elif (item in comparation):     printFormated(item, "Comparativo")
        elif (re.search("\"", item)):   printFormated(item, "Literal")
        elif (re.search(r"\D", item)):  printFormated(item, "Variavel/Função")
        else:                           printFormated(item, "Number")

for t in arq:
    if(re.search("\"", t)):
        separate(t[0:t.find("\"")])
        tokens.append(t[t.find("\""):t.rfind("\"")+1])
        separate(t[t.rfind("\"")+1:])
    else:
        separate(t)

categorize(tokens)
    