# Qualquer string binaria, exceto 01, 101, 0100
edges = { (0, '0') :  [1],
          (0, '1') :  [3],
          (1, '0') : [6],
          (1, '1') : [2], 
          (2, '0') : [4],
          (2, '1') : [6],
          (3, '0') : [7],
          (3, '1') : [6],
          (4, '0') : [5],
          (4, '1') : [6],       
          (5, '0') : [6],
          (5, '1') : [6],
          (6, '0') : [6],
          (6, '1') : [6],
          (7, '0') : [9],
          (7, '1') : [8],
          (8, '0') : [6],
          (8, '1') : [6],
          (9, '0') : [9],
          (9, '1') : [6],

 }
initial   = 0
accepting = [1,3,4,6,7,9] 

def epsilon_nfa(string, current, edges, accepting): 
    #print ("current: " + str(current) + "string: " + string )    
    if string == "":
        return  current in accepting       
    else:
        if (current, '') in edges:
          for next in edges[(current,'')]:
            if epsilon_nfa(string, next, edges, accepting):
                    return True
        c = string[0]
        if (current,c) in edges:
            for next in edges[(current,c)]:
                if epsilon_nfa(string[1:], next, edges, accepting):
                    return True
        
        return False
        

string = input()
print (epsilon_nfa( string , initial, edges, accepting) )      