# 8. Escribe un programa que verifique si una lista está ordenada de forma ascendente.

tamaño = int(input("Escriba la cantidad de números que ingresarán en la lista: "))
numeros = []

for i in range(tamaño):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

print("La lista es:", numeros)

ascendente = True  

for i in range(tamaño - 1):
    if numeros[i] > numeros[i + 1]:
        ascendente = False
        break  

if ascendente:
    print("La lista está ordenada de forma ascendente.")
else:
    print("La lista no está ordenada de forma ascendente.")