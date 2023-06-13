from glc import GLC

#L = O conjunto de todas as palavras em {0,1}* com dois zeros consecutivos.

def main():
    V = {'S'}
    Sigma = {'0','1'}
    R = {('S','00'), ('S','S0'), ('S','S1'), ('S','0S'), ('S','1S')
    }
    start = 'S'
    G = GLC(V,Sigma,R,start)
    G.check()
    teste(G)
    
