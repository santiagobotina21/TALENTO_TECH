# 4. Escriba un programa que pida dos números enteros. El programa pedirá de nuevo el segundo
# número mientras no sea mayor que el primero. El programa terminará escribiendo los dos números.


numero1 = int(input("Escriba un numero: "))
numero2 = int(input(f"Escriba un numero mayor que {numero1}: "))

while numero2<=numero1:
    numero2 = int(input(f"{numero2} no es mayor que {numero1}. Intentelo de nuevo: "))
else:
    print("El numero",numero2, "es mayor que el numero",numero1)