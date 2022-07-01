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

        for index in range(0, len(self.tokens)):        

            if(self.tokens[index]["token"]  in self.types and self.tokens[index+2]["token"]  == "(" and okay):
                self.line = "def "
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
                self.line += "\n"
                file.write(self.line)
                self.cleanLine(ident)
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
            elif(not (self.tokens[index]["token"] in self.types) and okay):
                self.line += self.tokens[index]["token"]
            



    