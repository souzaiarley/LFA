# Exemplo de NFA que aceita as strings binárias que terminam em 00 ou 11

Q = {1,2,3,4,5}
delta = {'0', '1'}

edges = {  (1,'0') : [2,5],
           (1,'1') : [1],
           (2,'0') : [5],
           (2,'1') : [2,4],
           (3,'0') : [3],
           (3,'1') : [2,4],
           (4,'0') : [2],
           (4,'1') : [1],
           (5,'0') : [3],
           (5,'1') : [2]
}
initial   =  1 # estado inicial
accepting = [1,3] # conjunto de estado final

def nfa(string, current, edges, accepting): 
    if string == "":
        return  current in accepting        
    else:
        c = string[0]
        if (current,c) in edges:
            for next in edges[(current,c)]:
                if nfa(string[1:], next, edges, accepting):
                    return True
        return False
        

string = input()
print ( nfa(string, initial, edges, accepting) )