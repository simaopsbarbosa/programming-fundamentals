res = []
a = str(input())
b = str(input())

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

for i in range(int(a),int(b)+ 1):
    if i in primes:
        res.append(str(i))
        
res_string = " ".join(res)
        
print(f"Prime numbers between {a} and {b} are: {res_string}")