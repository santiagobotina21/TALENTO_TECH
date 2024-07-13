# 7. Escriba un programa que reciba números enteros y finalice cuando se escriba un numero impar,
# al final se debe mostrar cual fue el número impar que permitió la salida del bucle

numero = int(input("Escriba un numero: "))

while numero%2==0:
    print("El numero es par")
    numero = int(input("Digite un nuevo numero: "))
else:
    print("El numero",numero, "es impar y se sale del bucle")