def bitonic_point(f): # returns integer
    list = f()
    for i in range(len(list)):
        if list[i] > list[i-1] and list[i] > list[i+1]:
            return list[i]
    
    # lol era so ver o maximo :(