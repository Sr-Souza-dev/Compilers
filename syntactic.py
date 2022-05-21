
class Syntactic:
    def __init__(self, DOMI, tokens):
        self.tokens = tokens
        self.okay = True
        self.stack = []
        self.DOMI = DOMI
        self.tree = {

            #Functions Defined
            str(self.DOMI.RESERVED.value)+"1": ["(1"],
            'if': ["(1"],
            'else':["(1", 'if'],
            '{':[],
            '}':[],

            # * Inserção de class
            '#include':                         ['<'],
            '<':                                [str(self.DOMI.RESERVED.value)],
            str(self.DOMI.RESERVED.value):            ['>'],
            '>':[],                                                                 # ***** Terminal *****

            # * Definição de Using
            'using':                        ['namespace'],
            'namespace':                    ['std'],
            'std':                          [';'],   
            ';':[],                                                                   # ***** Terminal *****

            # * Declaração: Variavel - Função
            'int':                                  ['main', str(self.DOMI.VARIABLE.value)],
            'string':                               [str(self.DOMI.VARIABLE.value)],
            'float':                                [str(self.DOMI.VARIABLE.value)],
            'char':                                [str(self.DOMI.VARIABLE.value)],
            str(self.DOMI.VARIABLE.value):                ['(', '='],
            # Declaração de Função
            'main':                                 ['('],
            '(':                                    ['int1','string1', 'float1', ')'],
            'int1':                                 [str(self.DOMI.VARIABLE.value)+'1'],
            'string1':                              [str(self.DOMI.VARIABLE.value)+'1'],
            'float1':                               [str(self.DOMI.VARIABLE.value)+'1'],
            str(self.DOMI.VARIABLE.value)+'1':            [',',')'],
            ',':                                    ['int1','string1','float1'],
            ')':[],                                                             # ***** Terminal *****
            # Declaração Variavel
            '=':                                [str(self.DOMI.VARIABLE.value)+'2', str(self.DOMI.NUMBER.value), str(self.DOMI.LITERAL.value)],
            str(self.DOMI.VARIABLE.value)+'2':        [str(self.DOMI.OPERATOR.value), str(self.DOMI.COMPARATIVE.value), ";",'(1'],
            str(self.DOMI.NUMBER.value):              [str(self.DOMI.OPERATOR.value), str(self.DOMI.COMPARATIVE.value), ";"],
            str(self.DOMI.LITERAL.value):             [str(self.DOMI.OPERATOR.value), str(self.DOMI.COMPARATIVE.value), ";"],
            str(self.DOMI.OPERATOR.value):            [str(self.DOMI.VARIABLE.value)+'2', str(self.DOMI.NUMBER.value), str(self.DOMI.LITERAL.value)], 
            str(self.DOMI.COMPARATIVE.value):         [str(self.DOMI.VARIABLE.value)+'2', str(self.DOMI.NUMBER.value), str(self.DOMI.LITERAL.value)],

            # * Atribuição: Função-Variavel
            str(self.DOMI.VARIABLE.value)+'3':            ['(1', '='],
            '(1':                                   [str(self.DOMI.VARIABLE.value)+'4', str(self.DOMI.NUMBER.value)+'1', str(self.DOMI.LITERAL.value)+'1', ')1'],
            str(self.DOMI.VARIABLE.value)+'4':            [str(self.DOMI.OPERATOR.value)+'1', str(self.DOMI.COMPARATIVE.value) + '1', ')1', ',1'],
            str(self.DOMI.NUMBER.value)+'1':              [str(self.DOMI.OPERATOR.value)+'1', str(self.DOMI.COMPARATIVE.value) + '1', ')1', ',1'],
            str(self.DOMI.LITERAL.value)+'1':             [str(self.DOMI.OPERATOR.value)+'1', str(self.DOMI.COMPARATIVE.value) + '1', ')1', ',1'],
            str(self.DOMI.OPERATOR.value)+'1':            ['(1', str(self.DOMI.VARIABLE.value)+'4', str(self.DOMI.NUMBER.value)+'1', str(self.DOMI.LITERAL.value)+'1'],
            str(self.DOMI.COMPARATIVE.value)+'1':         ['(1', str(self.DOMI.VARIABLE.value)+'4', str(self.DOMI.NUMBER.value)+'1', str(self.DOMI.LITERAL.value)+'1'],
            ',1':                                   ['(1', str(self.DOMI.VARIABLE.value)+'4', str(self.DOMI.NUMBER.value)+'1', str(self.DOMI.LITERAL.value)+'1', ],
            ')1':                                   [',1', ';', str(self.DOMI.OPERATOR.value), str(self.DOMI.COMPARATIVE.value)],

            # * Print 
            'cout':                      ['<<1'],
            '<<1':                       [str(self.DOMI.VARIABLE.value)+'2', str(self.DOMI.NUMBER.value), str(self.DOMI.LITERAL.value)],

            # * Return
            'return':                    [str(self.DOMI.VARIABLE.value)+'2', str(self.DOMI.NUMBER.value), str(self.DOMI.LITERAL.value)]
        }
    def checkTree(self, currentState, states, historic):
        reading = False
        while(currentState):
            historic += " " + states[0]['token']    
            if(states[0]['token'] == '{' or states[0]['token'] == '}' or states[0]['token'] == '(' or states[0]['token'] == ')'):
                not self.stackControl(states[0])
            if(states[0]['token'] == "<<"):
                reading = True                                           
            if(states[0]['token'] in currentState):
                currentState = self.tree[states[0]['token']]
                states.pop(0)
            elif((states[0]['token'] + "1") in currentState):
                historic += states[0]['token']+"1"
                currentState = self.tree[states[0]['token']+"1"]
                states.pop(0)
            elif(str(states[0]['type'].value) in currentState):
                currentState = self.tree[str(states[0]['type'].value)]
                states.pop(0)
            elif((str(states[0]['type'].value)+"1") in currentState):
                currentState = self.tree[str(states[0]['type'].value) +"1"]
                states.pop(0)
            elif((str(states[0]['type'].value)+"2") in currentState):
                currentState = self.tree[str(states[0]['type'].value) +"2"]
                states.pop(0)
            elif((str(states[0]['type'].value)+"3") in currentState):
                currentState = self.tree[str(states[0]['type'].value) +"3"]
                states.pop(0)
            elif((str(states[0]['type'].value)+"4") in currentState):
                currentState = self.tree[str(states[0]['type'].value) +"4"]
                states.pop(0)

            elif(states[0]['token'] == "{"):
                states.pop(0)
                break

            elif(reading == True and states[0]['token'] == "<<"):
                currentState = self.tree["<<1"]
                states.pop(0)

            else:
                self.okay = False
                print("[Syntax error] - content: \"", historic,"\"")
                print("No definition for the character in this context: \'", states[0]['token'],"\'")
                print("-------------------------------------------------------------------------- \n")
                return historic
        return historic

    def stackControl(self, state):
        if(state['token'] == "{" or state['token'] == "("):
            self.stack.append(state['token'])
            return True

        if(self.stack):
            if(state['token'] == ")" and self.stack[len(self.stack)-1] == "("):
                self.stack.pop(len(self.stack)-1)
                return True
            elif(state['token'] == "}" and self.stack[len(self.stack)-1] == "{"):
                self.stack.pop(len(self.stack)-1)
                return True
            
        print("[Syntax error] - The algorithm presents terminal operator unbalance")
        print("no symbol expected: \'",state['token'],"\'")
        print("-------------------------------------------------------------------------- \n")
        self.okay = False

        return False


    def analyse(self):
        currentState = ""
        historic = ""
        states = self.tokens[:]
        errorsHistoric = []
        errorsStates = []
        
        while(states):
                    
            historic += " " + states[0]['token']    

            if(states[0]['token'] in self.tree and states[0]['token'] != "(" and states[0]['token'] != ")" and states[0]['token'] != "{" and states[0]['token'] != "}"):
                currentState = self.tree[states[0]['token']]
                states.pop(0)
                historic = self.checkTree(currentState, states, historic)

            elif(states[0]['type'] == self.DOMI.VARIABLE):
                currentState = self.tree[str(self.DOMI.VARIABLE.value)+'3']
                states.pop(0)
                historic =  self.checkTree(currentState, states, historic)
            else:
                self.okay = False
                if(states[0]['token'] == '{' or states[0]['token'] == '}' or states[0]['token'] == '(' or states[0]['token'] == ')'):
                    self.stackControl(states[0])
                else:
                    errorsHistoric.append(historic)
                    errorsStates.append(states[0]['token'])
                states.pop(0)           

            if(states[0]['token'] == '{' or states[0]['token'] == '}' or states[0]['token'] == '(' or states[0]['token'] == ')'):
                historic += " " + states[0]['token']  
                self.stackControl(states[0])
                states.pop(0)  

            historic = historic.rstrip()
            if(len(historic) > 20):
                historic = ""

        for i in range(0, len(errorsHistoric)):
            print("[Syntax error] - content: \"", errorsHistoric[i],"\"")
            print("No definition for the character in this context: \'", errorsStates[i],"\'")
            print("-------------------------------------------------------------------------- \n")
            
        if(len(self.stack)):
            print("[Syntax error] - The algorithm presents terminal operator unbalance")
            print("no symbol expected: \'",self.stack[len(self.stack) - 1],"\'")
            return

        elif(self.okay):
            print("Congratulations, the algorithm is perfect for parsing syntactically!")        