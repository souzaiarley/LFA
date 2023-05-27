# Expressão regular: L = {a^m b^n|m+n é par}
from regexp import *

def main():
    r1 = Literal("a")
    r2 = Literal("b")
    r3 = Concat(r1, r1)
    r4 = Concat(r2, r2)
    r5 = Star(r3)
    r6 = Star(r4)
    r7 = Concat(r5, r1)
    r8 = Concat(r6, r2)
    r9 = Concat(r7, r8)
    r10 = Concat(r5, r6)
    r11 = Or(r10, r9)

    str = input()
    E = r11 
    print( E.matches(str) )


if __name__ == "__main__":
    main()