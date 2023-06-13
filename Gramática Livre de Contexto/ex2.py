from glc import GLC


def main():
    V = {'S', 'A'}
    Sigma = {'a','b', 'c'}
    R = {('S', ''), ('S', 'AaAbA'), ('S', 'AbAaA'),
         ('A', ''), ('A', 'AaA'), ('A', 'AbA'), ('A', 'AcA')
    }
    start = 'S'
    G = GLC(V,Sigma,R,start)
    G.check()
    teste(G)
    
