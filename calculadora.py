# CALCULADORA

# INGRESO DE NOMBRE
nombre=(input("Ingrese su nombre: "))

# SUMA
sum1 = int(input(f"{nombre},Por favor ingrese el primer número para sumar: "))
sum2 = int(input(f"{nombre},Por favor ingrese el segundo número para sumar: "))

print("La suma de",sum1,"y de",sum2,"es:",sum1+sum2)

# RESTA
res1 = int(input(f"{nombre},Por favor ingrese el primer número para restar: "))
res2 = int(input(f"{nombre},Por favor ingrese el segundo número para restar: "))

print("La resta de",res1,"y de",res2,"es:",res1-res2)

# MULTIPICACIÓN
mul1 = int(input(f"{nombre},Por favor ingrese el primer número para multiplicar: "))
mul2 = int(input(f"{nombre},Por favor ingrese el segundo número para multiplicar: "))

print("La multiplicación de",mul1,"y de",mul2,"es:",mul1*mul2)

# DIVISIÓN
div1 = int(input(f"{nombre},Por favor ingrese el primer número para dividir: "))
div2 = int(input(f"{nombre},Por favor ingrese el segundo número para dividir: "))

print("La división de",div1,"y de",div2,"es:",div1/div2)

# DIVISIÓN ENTERA
divE1 = int(input(f"{nombre},Por favor ingrese el primer número para dividir con resultado entero: "))
divE2 = int(input(f"{nombre},Por favor ingrese el segundo número para dividir con resultado entero: "))

print("La división de",divE1,"y de",divE2,"es:",divE1//divE2)

# RESIDUO DE LA DIVISIÓN
mod1 = int(input(f"{nombre},Por favor ingrese el primer número para calcular el residuo de la division: "))
mod2 = int(input(f"{nombre},Por favor ingrese el segundo número para calcular el residuo de la division: "))

print("El residuo de la division de",mod1,"y de",mod2,"es:",mod1%mod2)

# POTENCIA
pot1 = int(input(f"{nombre},Por favor ingrese el primer número de base: "))
pot2 = int(input(f"{nombre},Por favor ingrese el segundo número de exponente: "))

print("La potencia de",pot1,"y de",pot2,"es:",pot1**pot2)



