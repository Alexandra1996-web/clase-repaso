# while significa mientras
# vueltas = 0

# while vueltas < 5:
#     vueltas = vueltas +  1
#     print("ahora di", vueltas, "vuelta(s)")

# print("aca estoy fuera del while y tengo el valor de" , vueltas)

numero = 23

while True:
    numero_ingresado = int(input("Pasame un numero"))
    if numero == numero_ingresado:
        print("acertaste kp")
        break
    else:
        print("erraste kp")
