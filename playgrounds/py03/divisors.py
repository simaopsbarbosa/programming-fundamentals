num = int(input("what is num?"))

for i in range(num):
    if num % (i+1) == 0:
        sum = sum + i+1
        
print(sum)
        
        

