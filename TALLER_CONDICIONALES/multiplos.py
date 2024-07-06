# 6. Escriba un programa que pida dos números enteros y que escriba
#  si el mayor es múltiplo del menor.

nombre=(input("Ingrese su nombre: "))

numero1 = int(input(f"{nombre},Por favor ingrese el primer numero entero: "))
numero2= int(input(f"{nombre},Por favor ingrese el segundo numero entero: "))

if numero1 > numero2:
    mayor = numero1
    menor = numero2
elif numero2 > numero1:
    mayor = numero2
    menor = numero1
else:
    print("Los dos números son iguales.")
    exit()


if mayor % menor == 0:
    print(f"El numero mayor {mayor} ES múltiplo del numero menor {menor}.")
else:
    print(f"El numero mayor {mayor} NO es múltiplo del numero menor {menor}.")
