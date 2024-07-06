# INGRESO DE NOMBRE
nombre=(input("Ingrese su nombre: "))
print("--------------------------------------------------------------------")

# Pide al usuario que ingrese dos números y luego imprime si ambos números son mayores que 10.Pide al usuario que ingrese dos números y luego imprime si al menos uno de los números es mayor que 10.

numero = int(input(f"{nombre},Por favor ingrese el primer número: "))
numero2 = int(input(f"{nombre},Por favor ingrese el segundo número: "))

if (numero > 10) and (numero2 > 10):
  print("Los dos numeros ingresados SON mayores que 10")
else:
 print("Los dos números ingresados NO son mayores que 10")

if (numero > 10) or (numero2 > 10):
  print("Uno de los dos numeros ingresados es mayor que 10")
else:
 print("Ninguno de los dos numeros son mayores que 10")

print("--------------------------------------------------------------------")

# Pide al usuario que ingrese un número y luego imprime si el número no es mayor que 10. (Use el operador ‘not’)

numero3=int(input(f"{nombre},Ingrese un numero para verificar si es mayor que 10: "))

print(f'El numero ingresado es mayor que 10 : { not numero3 > 10}')


#Pide al usuario que ingrese tres números y luego imprime si el primer número es mayor que 5 y el segundo número es menor que 10 o el tercer número es igual a 20.

numero4=int(input(f"{nombre},Ingrese el NUMERO 1 para verificar si es mayor que 5: "))
numero5=int(input(f"{nombre},Ingrese el NUMERO 2 para verificar si es menor que 10: "))
numero6=int(input(f"{nombre},Ingrese un NUMERO 3 para verificar si es igual que 20: "))

if (numero4 > 5) and (numero5 < 10) or (numero6==20):
  print("El NUMERO 1:",numero4, "es mayor que 5")
  print("El NUMERO 2:",numero5, "es menor que 10")
  print("El NUMERO 3:",numero6, "es igual que 20")

