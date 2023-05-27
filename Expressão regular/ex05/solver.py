# Expressão regular: terceiro símbolo da direita para a esquerda é 1
from regexp import *

def main():
    r0 = Literal("0")
    r1 = Literal("1")
    r2 = Or(r0, r1)
    r3 = Star(r2)
    r4 = Concat(r2, r2)
    r5 = Concat(r3, r1)
    r6 = Concat(r5, r4)

    str = input()
    E = r6
    print( E.matches(str) )


if __name__ == "__main__":
    main()