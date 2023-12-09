n = float(input("number: "))
max = n
min = 0

midpoint = (max + min) / 2
while round(midpoint * midpoint, 5) != n:
    if midpoint * midpoint > n:
        max = midpoint
    else:
        min = midpoint
    midpoint = (max + min) / 2

print(round(midpoint,5))