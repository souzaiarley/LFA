def sufixos(x):
  if x == "":
     return [x]
  sufs = [x]
  sufs = sufs + sufixos(x[1:])
  return sufs
        
def main():
    x = input()
    
    print( sufixos(x) )


if __name__ == "__main__":
    main()
    