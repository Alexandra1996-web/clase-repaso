'''
Adivina el número
El programa genera un número secreto y aleatorio entre 1 y 100 (o cualquier rango especificado) 
y el usuario debe adivinar el número tras una pista de la computadora. Cada vez que un usuario se 
equivoca, se le ofrece una pista para que le resulte más fácil adivinar el número, pero a costa de 
reducir la cantidad de intentos. La pista puede ser si el número ingresado es mayor o menor al número 
secreto. El programa también requiere funciones para:

Comparar el número ingresado con el número secreto
Encontrar si el número ingresado es menor o mayor al número secreto
jazgamarra @ 10/10/2022

'''

import random

def es_mayor_menor(numero_ingresado, numero_secreto): 
    if (numero_ingresado > numero_secreto): 
        print("El numero secreto es menor")
    elif (numero_ingresado < numero_secreto): 
        print("El numero secreto es mayor")

def comparar_iguales(numero_secreto, numero_ingresado): 
    if (numero_secreto == numero_ingresado):
        return True
    
# Declaracion de variables antes del ciclo 
numero_secreto = 8
numero_ingresado = 0
cantidad_intentos = 3 

print ('''>> Bienvenido a ADIVINA EL NUMERO! 
>> El numero esta en el rango del 1 al 10
-------------------------------------------''')


# Ciclo principal
while True: 
    numero_ingresado = int(input("Ingrese un numero: "))
    print("-------------------------------------------")
    
    # Si se adivino el numero, sale del ciclo
    son_iguales = comparar_iguales(numero_secreto, numero_ingresado)
    if son_iguales == True:
        print(f"Adivinaste! El numero secreto es {numero_secreto} ")
        break; 
    # Si no se adivino, llama a la funcion para comparar 
    else: 
        es_mayor_menor(numero_ingresado, numero_secreto)
        cantidad_intentos -= 1
        # Si ya no se tienen intentos 
        if (cantidad_intentos == 0):
            print("-------------------------------------------")
            print(f"Lo siento, no te quedan intentos! El numero era {numero_secreto}")
            break; 
        
    print(f"La cantidad de intentos es {cantidad_intentos} ")
