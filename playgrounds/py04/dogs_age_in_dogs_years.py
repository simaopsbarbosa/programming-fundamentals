def dogs(h_age):
    sum = 0
    for i in range(1,h_age+1):
        if i == 1 or i == 2:
            sum += 10.5
        else:
            sum += 4
    return sum