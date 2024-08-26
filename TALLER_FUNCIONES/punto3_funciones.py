# Escribir una funcion que reciba una muestra de numeros en una lista y devuelva 
# su media

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
            

def calcular_media(numeros):
    if not numeros:
        raise ValueError("La lista de números está vacía, no se puede calcular la media.")
    
    suma = sum(numeros)
    media = suma / len(numeros)
    return media


media = calcular_media(numeros)

print("La lista es:", numeros)
print("La suma de los números ingresados es:", sum(numeros))
print("La media de los números es:", media)
