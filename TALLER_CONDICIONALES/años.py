# 5. Escriba un programa que pida el año actual y un año cualquiera y que escriba
#  cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.

nombre = input("Ingrese su nombre: ")

año_actual = int(input(f"{nombre}, por favor ingrese el año actual: "))
año_aleatorio = int(input(f"{nombre}, por favor ingrese un año aleatorio: "))

if año_actual > año_aleatorio:
    diferencia = año_actual - año_aleatorio
    print(f"Han pasado {diferencia} años desde {año_aleatorio} hasta el año actual {año_actual}.")
elif año_aleatorio > año_actual:
    diferencia = año_aleatorio - año_actual
    print(f"Faltan {diferencia} años para llegar a {año_aleatorio}.")
else:
    print("Los dos años ingresados son iguales.")

