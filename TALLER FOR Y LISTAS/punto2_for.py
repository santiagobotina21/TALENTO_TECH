# 2. Escribe un programa que encuentre el valor máximo en una lista de números.

tamaño = int(input("Escriba la cantidad de numeros que ingresaran en la lista: "))
numeros = []
mayor=0

for i in range(tamaño):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)
    if numero >= mayor:
        mayor=numero



print("La lista es: ",numeros)
print("El numero mayor de la lista es: ",mayor)