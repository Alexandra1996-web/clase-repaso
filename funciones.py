num1 = 1
num2 = 2
num3 = 6
num4 = 2

def suma (puerta1,puerta2):
    resultado = puerta1 + puerta2
    return resultado

# operacion1
operacion1 = suma(num1,num2)
print(operacion1)
# operacion2
operacion2 = suma(num3,num4)
print(operacion2)

# operacion3 
operacion3 = suma(operacion1,operacion2)
print(operacion3)
operacion3 = operacion1 + operacion2
print(operacion3)
