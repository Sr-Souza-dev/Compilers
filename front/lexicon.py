import re

class Lexicon:

    def __init__(self, domi, file):
        self.reserved        = ["if", "while", "stdio.h", "const", "void", "cout", "int", "char", "float", "string", "else", "using", "namespace","std", "return", "true", "false", "iostream", "#include", "#define"]
        self.assignment      = ["<<",">>","=","&"]
        self.delimiters      = ["{","}","(",")","[","]", ";", ","]
        self.operator        = ["+","-","*","/", "%"]
        self.comparation     = ["==","<=",">=","!=", "<", ">"]

        self.arq             = file
        self.DOMI            = domi

        self.items          = []
        self.tokens         = []

    def separate(self,word):
        for item in re.findall(r'(#include|#define|[0-9]+.[0-9]+|stdio.h|<<|==|<=|>=|!=|\w*|\W)',word):
            item = item.strip()     
            if(item != ""):
                self.items.append(item)

    def defineToken(self, item, type):
        self.tokens.append({"token":item, "type":type})
        # item += "  "
        # while(len(item) < 62):
        #     item += "-"
        # print(f"{item:63} -> {type:3}")

    def categorize(self):
        for item in self.items:
            if   (item in self.reserved):        self.defineToken(item, self.DOMI.RESERVED)
            elif (item in self.assignment):      self.defineToken(item, self.DOMI.ASSIGNMENT)
            elif (item in self.delimiters):      self.defineToken(item, self.DOMI.DELIMITER)
            elif (item in self.operator):        self.defineToken(item, self.DOMI.OPERATOR)
            elif (item in self.comparation):     self.defineToken(item, self.DOMI.COMPARATIVE)
            elif (re.search("\"|\'", item)):     self.defineToken(item, self.DOMI.LITERAL)
            elif (re.search("\D", item) and 
                (not re.match('[0-9]+.[0-9]+',item))):       self.defineToken(item, self.DOMI.VARIABLE)
            else:                                self.defineToken(item, self.DOMI.NUMBER)

    def tokenizer(self):
        for t in self.arq:
            if(re.search("//", t)):
                t = t[0:t.find("//")]
            if(re.search("\"", t)):
                self.separate(t[0:t.find("\"")])
                self.items.append(t[t.find("\""):t.rfind("\"")+1])
                self.separate(t[t.rfind("\"")+1:])
            elif(re.search("\'", t)):
                self.separate(t[0:t.find("\'")])
                self.items.append(t[t.find("\'"):t.rfind("\'")+1])
                self.separate(t[t.rfind("\'")+1:])
            else:
                self.separate(t)
        self.categorize()
        return self.tokens
