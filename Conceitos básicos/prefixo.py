def prefixo(x, y):
    if x == "":
        return True
    elif y == "":
        return False;
    else:
        if x[0] == y[0] and prefixo(x[1:], y[1:]):
            return True
        return False

def main():
    x = input()
    y = input()
    print( prefixo(x,y) )


if __name__ == "__main__":
    main()