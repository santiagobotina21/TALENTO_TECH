# 1. Escribe un programa que sume todos los elementos de una lista.


tamaño = int(input("Escriba la cantidad de numeros que ingresaran en la lista: "))
numeros = []
suma=0

for i in range(tamaño):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)
    suma = suma+numero

print("La lista es: ",numeros)
print("La suma de los numeros ingresados es: ",suma)