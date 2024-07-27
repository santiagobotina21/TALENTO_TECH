# 3. Escribe un programa que cuente cuántas veces aparece un elemento específico en una lista.

tamaño = int(input("Escriba la cantidad de numeros que ingresaran en la lista: "))
numeros = []


for i in range(tamaño):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

print("La lista es: ",numeros)

buscar=int(input("Ingresa el número a buscar en la lista: "))
encontrado=0

for numero in numeros:
    if numero == buscar:
        encontrado += 1

print(f"El elemento {buscar} aparece {encontrado} veces en la lista")
