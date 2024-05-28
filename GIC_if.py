import nltk

gci = """
    S -> B ' ' C ' ' D ' ' Q
    C -> V O H | H O V | V O V | H O H
    D -> V '=' E
    E -> T EP
    EP -> '+' T EP | '-' T EP | 
    T -> F TP
    TP -> '*' F TP | '/' F TP | 
    F -> K FP
    FP -> '^' K FP | K | 
    K -> '(' E ')' | V | H
    V -> L VP
    VP -> I | '_' I
    I -> J VP | L VP | 
    H -> N | M
    O -> '>' | '>' '=' | '<' | '<' '=' | '=' '=' | '~' '=' 
    L -> 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x'| 'y'| 'z'
    J -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
    N -> J | J N
    M -> N '.' N
    B -> 'i' 'f'
    Q -> 'e' 'n' 'd'
"""

grammar = nltk.CFG.fromstring(gci)
parser = nltk.ChartParser(grammar)
print("VALIDADOR DE GIC")

while True:
    try:

        sentence_chars = list(input("Cadena: "))
        tree = parser.parse(sentence_chars)

        if len(list(tree)) == 0:
            print('Cadena no valida')
        else:
            print('Cadena valida')
          ##  for branch in parser.parse(sentence_chars):
            ##   branch.draw()

    except: 
        print('Cadena no valida')