def is_composite(number):
    count = 0
    for i in range(1,number+1):

        if number%i == 0:
            count +=1
    if count == 2:
        return False
    else:
        return True
    
def get_composites(n):
    for x in range(n+1):
        if x >= 4 and is_composite(x):
            yield x

print(get_composites(7))