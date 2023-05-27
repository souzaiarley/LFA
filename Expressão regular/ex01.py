# Expressão regular: ab*ba(ab)*
# Coloque aqui as transições do seu autômato
edges = {
   (0,'a') : 1,
   (1,'a') : 4,
   (1,'b') : 5,
   (2,'a') : 3,
   (2,'b') : 4,
   (3,'a') : 4,
   (3,'b') : 2,
   (4,'a') : 4,
   (4,'b') : 4,
   (5,'a') : 2,
   (5,'b') : 5,
}

#Coloque aqui os estados finais do seu autômato
accepting = [2]

initial   = 0

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
print(dfa(string, initial, edges, accepting))