# Expressão regular: todas as strings exceto "", "01" e "001" 
from regexp import *

def main():
    r1 = Literal("0")
    r2 = Literal("1")
    r3 = Star(r1)
    r4 = Concat(r1, r3)
    r5 = Concat(r4, r2)
    r6 = Or(r1, r2)
    r7 = Star(r6)
    r8 = Concat(r6, r7)
    r9 = Concat(r5, r8)
    r10 = Concat(r6, r6)
    r11 = Concat(r10, r10)
    r12 = Concat(r11, r7)
    r13 = Concat(r2, r7)
    r14 = Or(r4, r9)
    r15 = Or(r12, r13)
    r16 = Or(r14, r15)


    str = input()
    E = r16
    print( E.matches(str) )


if __name__ == "__main__":
    main()