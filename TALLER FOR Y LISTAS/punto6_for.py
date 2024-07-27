# 6. Escribe un programa que invierta los elementos de una lista.

tamaño = int(input("Escriba la cantidad de numeros que ingresaran en la lista: "))
numeros = []

for i in range(tamaño):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

print("La lista es: ",numeros)
numeros.reverse()
print("La lista invertida es: ",numeros)




