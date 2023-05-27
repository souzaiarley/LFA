#Código Python 
# Automato que aceita string binarias multiplas de 5 iniciadas com '1'
# 
# 

Q = {1,2,3,4,5,6,7}
sigma = {'0', '1'}

edges = { # função de transição
(6, '0') : 7,
(6, '1') : 2,
(7, '0') : 7,
(7, '1') : 7,
(1, '1') : 2,
(1, '0') : 1,
(2, '0') : 3,
(2, '1') : 4,
(3, '0') : 5,
(3, '1') : 1,
(4, '0') : 2,
(4, '1') : 3,
(5, '1') : 5,
(5, '0') : 4
}

current = 6 # estado inicial
accepting = [1] # estados finais

# Função que roda o autômato
def dfa(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        remainder = string[1:]
        if (current, letter) in edges:
            newstate = edges[(current, letter)]
            return dfa(remainder, newstate, edges, accepting)
        return False


string = input()
print (dfa(string, current, edges, accepting))