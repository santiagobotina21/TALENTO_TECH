# 7. Escribe un programa que elimine los elementos duplicados de una lista. 

tamaño = int(input("Escriba la cantidad de números que ingresarán en la lista: "))
numeros = []
sinDuplicar = []

for i in range(tamaño):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

print("La lista es:", numeros)

for numero in numeros:
    if numero not in sinDuplicar:
        sinDuplicar.append(numero)

print("La lista sin elementos duplicados es:", sinDuplicar)




