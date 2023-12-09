travel = int(input("How many km? "))
litre = float(input("How many litres for 100km? "))
price = float(input("How much for a litre of fuel? "))

gasto = (travel * litre) / 100
custo = (gasto * price)

print(round(custo, 2))
