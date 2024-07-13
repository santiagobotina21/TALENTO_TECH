# 8.Cree una calculadora que le permita al usuario hacer las siguientes operaciones mientras se este ejecutando

print("BIENVENIDO A LA CALCULADORA")
print("--------------------------------------")
nombre = input("Por favor ingrese su nombre: ")

operacion = 0

while operacion != 6:
    print("\nA continuación seleccione la operación que desea realizar digitando el número:")
    print("1. SUMA")
    print("2. RESTA")
    print("3. MULTIPLICACION")
    print("4. DIVISION")
    print("5. PAR/IMPAR")
    print("6. SALIR\n")

    operacion = int(input("Digite el número de la operación que desea realizar: "))

    if operacion == 1:
        numero1 = int(input("Digite el primer número para sumar: "))
        numero2 = int(input("Digite el segundo número para sumar: "))
        suma = numero1 + numero2
        print("El resultado de la suma de",numero1,"y",numero2,"es",suma)
    elif operacion == 2:
        numero1 = int(input("Digite el primer número para restar: "))
        numero2 = int(input("Digite el segundo número para restar: "))
        resta = numero1 - numero2
        print("El resultado de la resta de",numero1,"y",numero2, "es",resta)
    elif operacion == 3:
        numero1 = int(input("Digite el primer número para multiplicar: "))
        numero2 = int(input("Digite el segundo número para multiplicar: "))
        multiplicacion = numero1 * numero2
        print("El resultado de la multiplicación de",numero1,"y",numero2, "es", multiplicacion)
    elif operacion == 4:
        numero1 = int(input("Digite el primer número para dividir: "))
        numero2 = int(input("Digite el segundo número para dividir: "))
        if numero2 == 0:
            print("Error: No se puede dividir por cero.")
        else:
            division = numero1 / numero2
            print("El resultado de la división de",numero1,"entre",numero2,"es:",division)
    elif operacion == 5:
        numero1 = int(input("Digite un número para saber si es par o impar: "))
        if numero1 % 2 == 0:
            print("El número",numero1,"es par")
        else:
            print("El número",numero1,"es impar")
    elif operacion == 6:
        print("Gracias",nombre,"por usar nuestra calculadora. ¡Que tengas un buen día!")
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 6 para seleccionar una operación.")
