class Generate:
    def __init__(self, domi, tokens, fileName):
        self.tokens = tokens
        self.DOMI = domi
        self.fileName = fileName
        self.types = ["float", "int", "char", "void", "string"]
        self.reserved = ["return","=", "printf", "scanf"]
        self.line = ""

    def cleanLine(self, ident):
        self.line = ""
        for i in range (0, ident):
            self.line += "   "

    def generate(self):
        file = open(f"result/{self.fileName}.py", "w")
        ident = 0
        okay = True
        declaration = False
        separate = True
        isMain = False

        for index in range(0, len(self.tokens)): 

            if(self.tokens[index]["token"] == "main" and self.tokens[index-1]["token"] in self.types and self.tokens[index+1]["token"] == "("):       
                isMain = True

            if(self.tokens[index]["token"]  in self.types and self.tokens[index+2]["token"]  == "(" and okay):
                self.line = "def "
                ident = 0

            elif(self.tokens[index]["token"] == "}" and ident > 0 and okay):
                ident -= 1
                file.write("\n")
                self.cleanLine(ident)

            elif(self.tokens[index]["token"] == "{" and okay):
                ident += 1
                self.line += ":\n"
                file.write(self.line)
                self.cleanLine(ident)

            elif(self.tokens[index]["token"] == ";"):
                if not declaration or not separate:
                    self.line += "\n"

                if(not self.line.strip() == ""):
                    file.write(self.line)

                self.cleanLine(ident)
                declaration = False
                separate = True
                okay = True

            elif (self.tokens[index]["token"] in self.reserved and okay):
                if(self.tokens[index]["token"] == "printf"):
                    self.line += "print"
                elif(self.tokens[index]["token"] == "scanf"):
                    okay = False
                    self.line += self.tokens[index+5]["token"] + " = " + "input(" + self.tokens[index+2]["token"] + ")"
                elif(self.tokens[index]["token"] == "="):
                    self.line += " " + self.tokens[index]["token"] + " "
                else:
                    self.line += self.tokens[index]["token"] + " "

            elif(self.tokens[index]["token"] in self.types) and okay:
                declaration = True

            elif(not(self.tokens[index]["token"] in self.types) and okay):
                if declaration:
                    if(self.tokens[index]["type"].value == self.DOMI.VARIABLE.value and self.tokens[index+1]["token"] != "," and self.tokens[index+1]["token"] != ";"):
                        separate = False
                    
                else:
                    self.line += self.tokens[index]["token"] 

                if(not separate and declaration):
                    if(self.tokens[index]["token"] == ","):
                        self.line += "\n"
                        file.write(self.line)
                        self.cleanLine(ident)
                        separate = True             
                    else:
                        self.line += self.tokens[index]["token"]

        if isMain:
            file.write("\nmain()")  