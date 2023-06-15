def main():
    sigma = eval(input())
    (states1, edges1, initial1, final1) = eval(input())
    (states2, edges2, initial2, final2) = eval(input())
    
    #adicionando um par ordenado relacionando os dois autômatos 
    states3 = [states1, states2]
    for x in states1:
        for y in states2:
            states3.append( (x,y) )
    #adicionar as transições
    edges3 = {}
    for st in states3:
        st_1 = st[0]
        st_2 = st[1]
        edges3[(st_1, st_2), '0'] = (edges1[st_1, '0'], edges2[st_2, '0'])
        edges3[(st_1, st_2), '1'] = (edges1[st_1, '1'], edges2[st_2, '1'])
        
    edges3[ ((1,2), '0')] = (2,3)
    #estado inicial
    initial3 = (initial1, initial2)
    #adicionar os estados finais
    final3 = []
    
    for x in final1:
        for y in states2:
            final3.append( (x, y) )
    
    for x in states1:
        for y in final2:
            final3.append( (x, y) )

    teste(states3, edges3, initial3, final3) 