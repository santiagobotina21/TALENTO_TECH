# 3. Escriba un programa al que usted ingrese una frase y el programa muestre en consola esta frase 
# desde el final hasta el principio de la misma como se muestra en la imagen

nombre = input("Ingrese su nombre: ")
respuesta = input(f'{nombre}, por favor ingrese una frase: ')

longitud_texto = len(respuesta)

i = longitud_texto -1 
print(longitud_texto)

while i >= 0:
    print(respuesta[i]) 
    i -= 1

