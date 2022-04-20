## Introductio
Na ciência da computação, análise léxica, lexing ou tokenização é o processo de converter uma sequência de caracteres (como em um programa de computador ou página da web) em uma sequência de tokens (strings com um significado atribuído e, portanto, identificado). Um programa que realiza análise lexical pode ser denominado lexer, tokenizer, ou scanner, embora scanner também seja um termo para o primeiro estágio de um lexer. Um lexer geralmente é combinado com um analisador, que juntos analisam a sintaxe de linguagens de programação, páginas da Web e assim por diante.

## Description
O suposto diretório trata a análise Lexical de uma linguagem de programção. Para tal feito, foi elaborado um 'compilador' em python e um código em c++ que simula uma calculadora simples. Como explicado na introdução, a ideia do compilador é separar todo o código em categorias de token que façam sentido para o contexto da linguagem. As categoria abordadas no código são:
1. reserved: São um conjunto de palavras reservadas (tem funções definidas dentro da linguagem - if, else, whihle...)
2. assignment: Operadores de atribuição da linguagem (=, <<)
3. delimiters: Delimitam o inicio ou fim de algo dentro da linguagem ({,},(,),[,])
4. operator: São responsaveis por realizar operações matematicas dentro da linguagem
5. comparation: São responsaveis por realizar operações logicas
6. literal: São um conjunto de caracteres delimitados por aspas (são normalmente textos ou strings - "my-text")
7. number: São valores numericos definidos pelo dominio Real.

## References 
<a href="https://pt.wikipedia.org/wiki/An%C3%A1lise_l%C3%A9xica">Introduction<a>