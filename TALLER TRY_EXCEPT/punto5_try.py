# 5. Realice una calculadora que me permita sumar, multiplicar, restar y dividir 
# sin que sufra fallos durante su ejecución y que además informe si hay algún
# error en el ingreso de valores por parte del usuario, puede ser de ciclo 
# repetitivo o de una sola ejecución.


print("BIENVENIDO A LA CALCULADORA")
print("--------------------------------------")
nombre = input("Por favor ingrese su nombre: ")

operacion = 0

while operacion != 5:
    print("\nA continuación seleccione la operación que desea realizar digitando el número:")
    print("1. SUMA")
    print("2. RESTA")
    print("3. MULTIPLICACION")
    print("4. DIVISION")
    print("5. SALIR\n")

    try:
        operacion = int(input("Digite el número de la operación que desea realizar: "))
    except:
        print("\n ERROR: Opción no válida. Por favor, ingrese un número del 1 al 5 para seleccionar una operación.")
        operacion = 0

    if operacion == 1:
        try:
            numero1 = int(input("Digite el primer número para sumar: "))
            numero2 = int(input("Digite el segundo número para sumar: "))
            suma = numero1 + numero2
        except:
            print("\n ERROR: Por favor, ingrese numeros enteros")
        else:
            print("El resultado de la suma de",numero1,"y",numero2,"es",suma)

    elif operacion == 2:
        try:
            numero1 = int(input("Digite el primer número para restar: "))
            numero2 = int(input("Digite el segundo número para restar: "))
            resta = numero1 - numero2
        except:
             print("\n ERROR: Por favor, ingrese numeros enteros")
        else:
             print("El resultado de la resta de",numero1,"y",numero2, "es",resta)

    elif operacion == 3:
        try:
            numero1 = int(input("Digite el primer número para multiplicar: "))
            numero2 = int(input("Digite el segundo número para multiplicar: "))
            multiplicacion = numero1 * numero2
        except:
            print("\n ERROR: Por favor, ingrese numeros enteros")            
        else:
            print("El resultado de la multiplicación de",numero1,"y",numero2, "es", multiplicacion)

    elif operacion == 4:
        try:
            numero1 = int(input("Digite el primer número para dividir: "))
            numero2 = int(input("Digite el segundo número para dividir: "))
            division = numero1 / numero2
        except ValueError:
            print("Error: Por favor, ingrese solo números enteros.")
        except ZeroDivisionError:
            print("Error: No se puede dividir por cero.")
        else:
            print("El resultado de la división de", numero1, "entre", numero2, "es:", division)

    elif operacion == 5:
        print("Gracias",nombre,"por usar nuestra calculadora. ¡Que tengas un buen día!")