def kolakoski():

    yield 1
    yield 2
    yield 2
    
    # utilize a sequência para descobrir o tamanho dos blocos seguintes
    gerador = kolakoski()
    next(gerador)
    next(gerador)
    n = 1
    
    for a in gerador:
        for i in range(a):
            yield n
        if n == 1:
            n = 2
        else:
            n = 1
        
def main():
    
    n = int(input())
    gerador = kolakoski()
    l = [ next(gerador) for i in range(n)]
    print(l)


if __name__ == "__main__":
    main()
