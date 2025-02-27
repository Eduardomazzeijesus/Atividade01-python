import os 

os.system("cls")

print("conversor de dolar para reais")

cotação = float(input("digite a cotaçao do dalar"))

dolar = float(input("digite o valor em dolar"))

real = (cotação * dolar )

os.system("cls")

print("cotação do dolar:" ,+ cotação)
print("valor em dolar: " , dolar)
print("valor em rea: " , real )