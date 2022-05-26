from enum import IntEnum
from lexicon import Lexicon
from syntactic import Syntactic
from semantics import Semantics



class DOMI(IntEnum):
    RESERVED     = 0,          # Reservada
    ASSIGNMENT   = 1,          # Atribuição
    DELIMITER    = 2,          # Delimitadores
    OPERATOR     = 3,          # Operador
    COMPARATIVE  = 4,          # Comparativo
    LITERAL      = 5,          # Literal
    VARIABLE     = 6,          # Variavel/Função
    NUMBER       = 7           # Number


lexicon = Lexicon(DOMI, open("calc.cpp", "r"))
tokens = lexicon.tokenizer()

# for item in tokens:
#     print(type(item['token']), item['token'], item['type'].value)

syntactic = Syntactic(DOMI, tokens)
okay = [syntactic.analyse()]

semantic = Semantics(DOMI, tokens)
okay.append(semantic.check())

if(okay[0] and okay[1]):
    print("Congratulations, the algorithm is perfect for parsing!")







    