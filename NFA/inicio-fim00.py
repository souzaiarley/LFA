# Exemplo de NFA que aceita as strings binárias que começam ou terminam em 01

Q = {1,2,3,4,5,6}
sigma = {'0','1'}

edges = {  (0,'0') : [1],
           (0,'1') : [3],
           (1,'0') : [1,3],
           (1,'1') : [2],
           (2,'0') : [2],
           (2,'1') : [2],
           (3,'0') : [3,4],
           (3,'1') : [3],
           (4,'0') : [3,4],
           (4,'1') : [5],
           (5,'0') : [4],
           (5,'1') : [3]
}
initial   =  0 # estado inicial
accepting = [2,5] # conjunto de estado final

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