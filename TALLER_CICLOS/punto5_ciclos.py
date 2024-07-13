# 5. Escriba un programa que pida números enteros mientras sean cada vez más grandes.

numero1 = int(input("Escriba un numero: "))
numero2 = int(input(f"Escriba un numero mayor que {numero1}: "))

while numero2 <= numero1:
    numero2 = int(input(f"{numero2} no es mayor que {numero1}. Intentelo de nuevo: "))
    while numero2 > numero1:
                numero1 = numero2
                numero2 = int(input(f"Escriba un numero mayor que {numero1}: "))