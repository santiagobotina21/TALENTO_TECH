# 2. Escribir un programa que pida al usuario dos números enteros 
# y muestre si el resultado de la multiplicación entre ambos es par o impar

nombre=(input("Ingrese su nombre: "))

numero1 = int(input(f"{nombre},Por favor ingrese el primer numero entero: "))
numero2= int(input(f"{nombre},Por favor ingrese el segundo numero entero: "))

resultado=numero1*numero2

if resultado%2==0:
    print("El resultado de la multiplicacion entre",numero1,"y",numero2,"es:",resultado," y este numero es PAR")
else:
    print("El resultado de la multiplicacion entre",numero1,"y",numero2,"es:",resultado," y este numero es IMPAR")

