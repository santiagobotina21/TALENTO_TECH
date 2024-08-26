# Escribir una funcion que reciba una muestra de numeros en una lista y otra 
# lista con sus cuadrados 

tamaño = int(input("Escriba la cantidad de números que ingresarán en la lista: "))
numeros = []

for i in range(tamaño):
    while True:
        try:
            numero = int(input(f"Ingrese el número {i+1}: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")
            

def calcular_cuadrados(numeros):
    if not numeros:
        raise ValueError("La lista de números está vacía, no se puede calcular sus cuadrados.")
    
    cuadrados = [numero ** 2 for numero in numeros]
    return cuadrados


cuadrados = calcular_cuadrados(numeros)

print("La lista inicial es:", numeros)
print("La lista de cuadrados es:", cuadrados)

