from glc import GLC

#L = O conjunto das palavras formada por 0’s e 1’s com no máximo um par 1’s consecutivos

def main():
    V = {'S', 'A', 'T', 'I'}
    Sigma = {'0','1'}
    R = { ('S', '1T'), 
          ('S', '0S'), 
          ('S', ''), 
          ('S', '10S'), 
          ('S', '11I'),
          ('T', '1A'), 
          ('T', '0T'), 
          ('T', ''), 
          ('A', ''), 
          ('A', '0T'), 
          ('I', '01I'), 
          ('I', '0I')
    }
    start = 'S'
    G = GLC(V,Sigma,R,start)
    G.check()
    teste(G)
    
