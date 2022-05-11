from enum import IntEnum
from lexicon import Lexicon
from syntactic import Syntactic



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

syntactic = Syntactic(DOMI, tokens)
syntactic.analyse()







    