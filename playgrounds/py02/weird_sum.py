a = int(input("numero 1: "))
b = int(input("numero 2: "))

# can't use conditionals or while
# if diff is even, sum is doubled
# if diff is odd, a * b is added to the sum

diff = a - b
sum = a + b

even = diff % 2 == 0

doubled = sum * 2
product = sum + (a * b)

print(doubled * even + product * (1 - even))
