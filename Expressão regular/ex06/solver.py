# Expressão regular: Conjunto de palavras com no máximo um par de 1's consecutivos
from regexp import *

def main():
    r0 = Literal("0")
    r1 = Literal("1")
    r2 = Star(r0)
    r3 = Concat(r0, r1)
    r4 = Star(r3)
    r5 = Concat(r1, r0)
    r6 = Star(r5)
    r7 = Or(r2, r1)
    r8 = Concat(r4, r2)
    r9 = Concat(r8, r6)
    r10 = Concat(r7, r9)
    r11 = Concat(r10, r7)

    str = input()
    E = r11
    print( E.matches(str) )


if __name__ == "__main__":
    main()