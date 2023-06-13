from glc import GLC

#L = conjunto de todas as strings formadas por a’s e b’s com a mesma quantidade de a’s e b’s.

def main():
    V = {'S'}
    Sigma = {'a','b'}
    R = {('S',''), ('S','aSb'), ('S','bSa'), ('S', 'SS')
    }
    start = 'S'
    G = GLC(V,Sigma,R,start)
    G.check()
    teste(G)

