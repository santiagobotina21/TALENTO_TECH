# 2. Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el
# programa se bloquee y además explica en un mensaje al usuario la causa y/o solución.

lista=[1,2,3,4,5]

try:
    print(lista[10])
except IndexError:
    print("Error: El índice está fuera del rango de la lista. La lista solo tiene {} elementos.".format(len(lista)))