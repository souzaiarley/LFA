from ap import AP

#L = Nenhum prefixo tem mais 1's do que 0's

def main():
    Q = {'q1','q2','q3'}
    Sigma = {'0','1'}
    Gamma = {'$'}
    delta = {('q1','0','' ):{('q1','0')},
         ('q1','1','0' ):{('q1','' )},
         ('q1','','$'):{('q3','' )},
         ('q1','' ,'0'):{('q3', '' )},
         }
    q0 = 'q1'
    Z0 = '$'
    F = {'q3'}
    M = AP(Q,Sigma,Gamma,delta,q0,Z0, F)
    teste(M)