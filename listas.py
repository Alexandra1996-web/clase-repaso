lista1 = [1,'hola', True]
# Meter un elemento dentro de una lista
lista1.append('kiwi')
# Eliminar un elemento dentro de una lista (recibe un indice)
lista1.pop(0) #eliminamos el primer elemento
# Saber la cantidad de elementos dentro de una lista
len(lista1)

palabra = ['h','o','l','a']
lista = [1994, 1988, 1992, 1990]
# Lista de listas
nueva_lista = [palabra , lista]

# Acceder elementos de una lista, dentro de una lista
print(nueva_lista[1][0])

# Eleminar un elemento de la lista por valor
lista_de_nombres = ['manu','sergio', 'laura', 'alexita']
lista_de_nombres.remove('sergio')
print(lista_de_nombres)

# Sobreescribir un elemento de la lista
lista_de_nombres[0] = 'pancracio'
print(lista_de_nombres)

# Como saber si un elemento esta en una lista
print('manu' in lista_de_nombres) # devuelve un True or False