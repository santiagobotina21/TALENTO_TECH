from mi_modulo import *
from calculadora import dividir
from usuarios import Usuario

# name= input("Ingresa tu nombre: ")

# saludar(name)

# radio = 3

# area_circulo= PI * (radio ** 2)
# print(f"El area del circulo es {area_circulo}")

# numerador=input("Ingrese el numerador: ")
# denominador=input("Ingrese el denominador: ")

# resultado=dividir(numerador,denominador)

# print(resultado)

mi_usuario=Usuario("Santiago","Gonzales",8929292)
mi_usuario.consulta()
print(mi_usuario.consignar(100000))
mi_usuario.consulta()