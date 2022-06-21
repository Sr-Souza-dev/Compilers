class Semantics:
    def __init__(self, DOMI, tokens):
        self.tokens = tokens
        self.functionsR = ["getchar","for"]
        self.DOMI = DOMI
        self.contexts = []
        aux =""

    def printError(self, content, text):
        print("[Semantic error] - content: <|> ", content," <|>")
        print("   "+text)
        print("-------------------------------------------------------------------------- \n")

    def verifyContexts(self, token):
        for index in range(0, len(self.contexts[len(self.contexts)-1]["variables"])):
            if(self.contexts[len(self.contexts)-1]["variables"][index]['name'] == token):
                return {"okay": True, "type": self.contexts[len(self.contexts)-1]["variables"][index]['type']}
        
        for index in range(0, len(self.contexts)-1):
            if(self.contexts[index]["name"] == token or token  in self.functionsR):
                return {"okay": True, "type": self.contexts[index]['type']}

        if(token[0] == '\''):
           
            return {"okay": True, "type": "char"}
        elif(token == 'endl' or token in self.functionsR):
            return {"okay": True, "type": "any"}

        return {"okay": False, "type": ""}


    def verifyType(self, token, verifyContext):
        if(token["type"].value == self.DOMI.NUMBER.value):
            verifyContext["okay"] = True
            verifyContext["type"] = "int"
        elif(token["type"].value == self.DOMI.LITERAL.value):
            verifyContext["okay"] = True
            if(len(token["token"]) <= 3):
                verifyContext["type"] = "char"
            else:
                verifyContext["type"] = "string"
        return verifyContext
                
    def check(self):
        result = True
        lastType = 0
        okay = False
        returned = False
        atrib = False
        historic = ""
        menssage = ""
        typeT = ""
        objAux = False
        verifyContext = {}
        for i in range(0, len(self.tokens) - 1):
            if(len(historic) > 50):
                    historic = ""

            historic += " " + self.tokens[i]["token"] 

            if(self.tokens[i]["token"] == "return"):
                returned = True

            elif((self.tokens[i]["type"].value == self.DOMI.NUMBER.value or self.tokens[i]["type"].value == self.DOMI.LITERAL.value or self.tokens[i]["type"].value == self.DOMI.VARIABLE.value or self.tokens[i]["token"] == "main") and self.tokens[i]["token"] != "endl"):
                
                if(self.tokens[i-1]["token"] == "int" or self.tokens[i-1]["token"] == "float" or self.tokens[i-1]["token"] == "char" or self.tokens[i-1]["token"] =="string"):
                    menssage = "A variavel ("+self.tokens[i]["token"]+") já foi declarada nesse escopo"
                    if(self.tokens[i+1]["token"] == "("):

                        if(not(objAux == False or returned)):
                            menssage = "Retorno da função \'" + self.contexts[len(self.contexts)-1]["name"] + "\' não foi encontrado"
                            self.printError(historic,menssage)
                            result = False

                        objAux = {
                            "name": self.tokens[i]["token"],
                            "type": self.tokens[i-1]["token"],
                            "variables": []
                        }
                        self.contexts.append(objAux)
                        returned = False
                        
                    else:
                        atrib = True
                        for index in range(0, len(self.contexts[len(self.contexts)-1]["variables"])):
                            if(self.contexts[len(self.contexts)-1]["variables"][index]['name'] == self.tokens[i]["token"]):
                                okay = True
                        if(okay):
                            self.printError(historic,menssage) 
                            result = False    
                        else:   
                            self.contexts[len(self.contexts)-1]["variables"].append({
                                "name": self.tokens[i]["token"],
                                "type": self.tokens[i-1]["token"],
                            })
                if(not (self.tokens[i-1]["token"] == "int" or self.tokens[i-1]["token"] == "float" or self.tokens[i-1]["token"] == "char" or self.tokens[i-1]["token"] =="string") or atrib):
                    atrib = False
                    menssage = "A variavel ("+self.tokens[i]["token"]+") não foi declarada no escopo de sua utilização"

                    verifyContext = self.verifyType(self.tokens[i], self.verifyContexts(self.tokens[i]["token"]))
                    okay = verifyContext["okay"]
                    typeT = verifyContext["type"]

                  
                    if(okay):
                        if not ((self.contexts[len(self.contexts)-1]['type'] == typeT) or (self.contexts[len(self.contexts)-1]['type'] == "float" and typeT == "int")) and returned:
                            print("Func: ",self.contexts[len(self.contexts)-1]['type'], "   Return: ",typeT)
                            menssage = "Retorno da função \'" + self.contexts[len(self.contexts)-1]["name"] + "\' não condiz com sua atribuição"
                            self.printError(historic,menssage)
                            result = False

                        okay = True
                        menssage = "Você tentou utilizar atributos de tipos diferentes em uma mesma operação"

                        if(self.tokens[i+1]["type"].value == self.DOMI.ASSIGNMENT.value or self.tokens[i+1]["type"].value  == self.DOMI.COMPARATIVE.value or self.tokens[i+1]["type"].value  == self.DOMI.OPERATOR.value):
                            while(True):
                                verifyContext = self.verifyType(self.tokens[i+2], self.verifyContexts(self.tokens[i+2]["token"]))
                                if(verifyContext["type"] != typeT) and (not self.tokens[i+2]["token"] in self.functionsR):
                                    if (typeT == "float" and verifyContext["type"] == "int") or (typeT == "int" and verifyContext["type"] == "float" and self.tokens[i+1]["token"] != "=" or verifyContext["type"] == "any" or self.tokens[i+1]["token"] == "<<"):
                                        okay = True
                                        break
                                    elif self.tokens[i+2]["token"] == "(" or self.tokens[i+2]["token"] == ")" or self.tokens[i+2]["token"] == "+" or self.tokens[i+2]["token"] == "-":
                                        i += 1
                                    else:
                                        okay = False
                                        historic += self.tokens[i+1]["token"] + " " + self.tokens[i+2]["token"]
                                        break
                                break
                                    

                                
                                
                        if(not okay):
                            self.printError(historic,menssage)
                            result = False

                    else:   
                        self.printError(historic,menssage)
                        result = False
                        
                    okay = False
                lastType = self.tokens[i]["type"].value

        return result

                

                        
                            
                    
        
     

