# 5. Escribe un programa que multiplique cada elemento de una lista por 2 y almacene el resultado en una nueva lista.

tamaño = int(input("Escriba la cantidad de numeros que ingresaran en la lista: "))
numeros = []
operacion=None
numeros2=[]


for i in range(tamaño):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)
    operacion=numero*2
    numeros2.append(operacion)


print("La lista es: ",numeros)
print("La lista de numeros multiplicados por 2 es: ",numeros2)
