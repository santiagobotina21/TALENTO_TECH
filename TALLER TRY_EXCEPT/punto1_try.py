# 1. Localiza el error en la siguiente bloque de codigo. Crea una excepcion para evitar que el
# programa se bloquee y además explica en un mensaje al usuario la causa y/o solución 

resultado =10/0

try:
    resultado =10/0
except ZeroDivisionError:
    print("Error: No se puede dividir por cero. Por favor, utiliza un divisor diferente de cero.")
