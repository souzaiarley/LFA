from language import L

def pumpingOut(x,y,z):
    # O jogador 2 recebe uma particao
    # deve escolher uma maneira de bombear a string para fora da linguagem
    i = 0
    p = x + y*i + z
    return not L(p)