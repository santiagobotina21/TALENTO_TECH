# INGRESO DE NOMBRE
nombre=(input("Ingrese su nombre: "))
print("--------------------------------------------------------------------")

# INGRESO DE NÚMEROS
numero = int(input(f"{nombre},Por favor ingrese el primer número: "))
numero2 = int(input(f"{nombre},Por favor ingrese el segundo número: "))


if numero > numero2:
  print("El numero",numero,"es mayor que el numero",numero2)

if numero == numero2:
  print("El numero",numero,"es igual que el numero",numero2)
else:
  print ("El numero",numero,"es diferente que el numero",numero2)

if numero < numero2:
  print("El numero",numero,"es menor que el numero",numero2)

if numero >= numero2:
  print("El numero",numero,"es mayor o igual que el numero",numero2)

if numero <= numero2:
  print("El numero",numero,"es menor o igual que el numero",numero2)