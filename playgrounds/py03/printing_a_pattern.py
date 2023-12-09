num = int(input("number : "))

for i in range(num):
    for j in range(num):
        print(num - j, end=' ')
    print("")
    num = num - 1