import math

a = int(input("what is number 1? "))
b = int(input("what is number 2? "))
c = int(input("what is number 3? "))

solution1 = round((- b + math.sqrt(b**2 - 4 * a * c)) / (2 * a), 2)
solution2 = round((- b - math.sqrt(b**2 - 4 * a * c)) / (2 * a), 2)

print(f"The solutions are {solution1} and {solution2}")