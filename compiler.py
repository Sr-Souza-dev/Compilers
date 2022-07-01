from enum import IntEnum
from fileinput import filename
from front.lexicon import Lexicon
from front.syntactic import Syntactic
from front.semantics import Semantics
from back.generate import Generate

class DOMI(IntEnum):
    RESERVED     = 0,          # Reservada
    ASSIGNMENT   = 1,          # Atribuição
    DELIMITER    = 2,          # Delimitadores
    OPERATOR     = 3,          # Operador
    COMPARATIVE  = 4,          # Comparativo
    LITERAL      = 5,          # Literal
    VARIABLE     = 6,          # Variavel/Função
    NUMBER       = 7           # Number


fileName = 'code3'
lexicon = Lexicon(DOMI, open(f"codeT/{fileName}.cpp", "r"))
tokens = lexicon.tokenizer()

syntactic = Syntactic(DOMI, tokens)
okay = [syntactic.analyse()]

semantic = Semantics(DOMI, tokens)
okay.append(semantic.check())

if(okay[0] and okay[1]):
    generate = Generate(DOMI, tokens, fileName)
    generate.generate()
    print("Congratulations, the algorithm is perfect for parsing!")







    