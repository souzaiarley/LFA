from glc import GLC

#L = {a^ib^jc^k | i >= 0, j>= 0, k = i+j}

def main():
    V = {'S', 'A', 'B'}
    Sigma = {'a','b','c'}
    R = {('S',''), ('S','A'),
         ('A', 'aAc'), ('A', 'B'), ('A', ''),
         ('B', 'bBc'), ('B', '')
    }
    start = 'S'
    G = GLC(V,Sigma,R,start)
    G.check()
    teste(G)
    
