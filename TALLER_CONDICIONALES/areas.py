#8.  Escriba un programa que pregunte primero si se quiere calcular
#  el área de un triángulo o la de un círculo. 
#  Si se contesta que se quiere calcular el área de un triángulo
#   (escribiendo T o t), el programa tiene que pedir entonces la base y la altura
#    y escribir el área. Si se contesta que se quiere calcular el área de un círculo
#     (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.

nombre = input("Ingrese su nombre: ")

respuesta = input(f'{nombre}, por favor digite la letra "T" para calcular el área de un triángulo o "C" para calcular el área de un círculo: ')

if respuesta=="T" or respuesta=="t":
    base = int(input("Por favor ingrese la base del triangulo: "))
    altura = int(input("Por favor ingrese la altura del triangulo: "))
    area=(base*altura)/2
    print("El area del triangulo es:",area)
elif respuesta=="C" or respuesta=="c":
    radio = int(input("Por favor ingrese el radio del circulo: "))
    area = radio * 3.1416
    print("El area del circulo es:",area)
else:
    print("La respuesta no es valida")
