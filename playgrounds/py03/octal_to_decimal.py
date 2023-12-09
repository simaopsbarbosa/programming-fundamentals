num = input("number: ")
valid = True

for i in range(len(num)):
    if int(num[i]) == 8 or int(num[i]) == 9:
        valid = False


sum = 0
if valid == False:
    print("Not a valid number.")
else: 
    for i in range(len(num)):
        sum = sum + 8 ** i * int(num[-(i +1)])
    print(sum)