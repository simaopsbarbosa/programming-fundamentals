def factorial(n):
    if n == 0:
        return 1
    else: 
        result = n
        while n > 1:
            n = n - 1
            result = result * n
        return result
    
def C(n,r):
    return int(factorial(n) / (factorial(r) * factorial(n - r)))
    
print(C(100,10))