#Código Python 
# Automato que aceita string binarias com a substring 011
# 
# 

Q = {1,2,3,4}
sigma = {'0', '1'}

edges = { # função de transição
(1, '1') : 1,
(1, '0') : 4,
(2, '0') : 4,
(2, '1') : 3,
(3, '0') : 3,
(3, '1') : 3,
(4, '1') : 2,
(4, '0') : 4, 
}

current = 1 # estado inicial
accepting = [3] # estados finais

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