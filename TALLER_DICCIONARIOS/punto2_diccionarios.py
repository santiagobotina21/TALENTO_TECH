# 2. Escribir un programa que guarde en un diccionario los precios de las frutas de la
# tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla
# el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe
# mostrar un mensaje informando de ello.


frutas = {
    "Platano": 1.35,
    "Manzana": 0.80,
    "Pera": 3.00,
    "Naranja": 4.00
}


while True:
    nombre_fruta = input("Ingrese el nombre de la fruta: ")
    if nombre_fruta in frutas:
        break
    else:
        print(f"La fruta '{nombre_fruta}' no está en el diccionario. Por favor, ingrese una fruta válida.")

while True:
    try:
        kilos = float(input("Ingrese el número de kilos: "))
        if kilos <= 0:
            print("La cantidad de kilos debe ser un número positivo. Inténtelo de nuevo.")
        else:
            break
    except ValueError:
        print("Por favor, ingrese un número válido para los kilos.")


precio_total = frutas[nombre_fruta] * kilos
print(f"El precio de {kilos} kilos de {nombre_fruta} es: ${precio_total}")

