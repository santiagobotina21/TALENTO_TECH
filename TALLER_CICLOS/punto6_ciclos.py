# 6. Escriba un programa que pida una cantidad de números que van a ser sumados. 
# Luego estos números serán ingresados uno a uno por el usuario y al final se debe mostrar el resultado de la suma total

cantidad = int(input("Digite la cantidad de numeros que desea sumar: "))

i=1
suma=0

while i<=cantidad:
    numero= int(input(f"Digite el {i} numero a sumar: "))
    suma=suma+numero
    i+=1
else:
    print("El resultado de la suma de los",cantidad,"numeros es de:",suma)
