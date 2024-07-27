# 4. Escribe un programa que extraiga todos los números pares de una lista y los almacene en una nueva lista.

tamaño = int(input("Escriba la cantidad de numeros que ingresaran en la lista: "))
numeros = []
pares=[]


for i in range(tamaño):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)
    if numero%2==0:
        pares.append(numero)


print("La lista es: ",numeros)
print("La lista de numeros pares es: ",pares)


