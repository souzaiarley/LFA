from jogador1 import partition
from language import L

def chooseString(m):
  # vamos escolher a palavra $w = a^mb^m$
  w = "a"*m + "b"*(m+1)
  partition(m,w)


def main():
  # o jogador 2 le o valor de m 
  m = int( input() )
  # o jogador 2 escolhe uma palavra usando o valor de m
  chooseString(m)

if __name__ == '__main__':
  main()     
