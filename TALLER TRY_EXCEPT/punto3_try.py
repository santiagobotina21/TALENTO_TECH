# 3. Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el
# programa se bloquee y además explica en un mensaje al usuario la causa y/o solución.

try:
    resultado = 15 + "20"
except TypeError:
    print("Error: No se puede sumar un número entero con una cadena. A continuacion se convertira la cadena a número para realizar la operación.")
    # Ejemplo de solución:
    resultado = 15 + int("20")
    print("Resultado después de la conversión:", resultado)


