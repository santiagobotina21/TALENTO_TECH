# 7. Escriba un programa que pida tres números y que escriba
#  si son los tres iguales, si hay dos iguales o si son los tres distintos.

nombre=(input("Ingrese su nombre: "))

numero1 = int(input(f"{nombre},Por favor ingrese el primer numero: "))
numero2= int(input(f"{nombre},Por favor ingrese el segundo numero: "))
numero3= int(input(f"{nombre},Por favor ingrese el tercer numero: "))

if numero1 == numero2 == numero3:
    print("Los tres números son iguales")
elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
    print("Hay dos números iguales")
else:
    print("Los tres números son distintos")
