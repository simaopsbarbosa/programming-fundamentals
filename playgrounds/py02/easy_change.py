preco = int(input("qual é o preço? "))
dado = int(input("qual é o valor dado? "))

troco = dado - preco

cinquenta = 0
vinte = 0
dez = 0
cinco = 0

while troco >= 50:
    cinquenta = cinquenta + (troco // 50)
    troco = troco - 50 * (troco // 50) 
    
while troco >= 20:
    vinte = vinte + (troco // 20)
    troco = troco - 20
    
while troco >= 10:
    dez = dez + (troco // 10)
    troco = troco - 10
    
while troco >= 5:
    cinco = cinco + (troco // 5)
    troco = troco - 5
    
print(str(cinquenta),str(vinte),str(dez),str(cinco))