from areas import *

print("------------------------------------------------------")

base = input("Ingrese la base del triángulo: ")
altura = input("Ingrese la altura del triángulo: ")
print(area_triangulo(base, altura))

print("------------------------------------------------------")
    
base = input("Ingrese la base del rectángulo: ")
altura = input("Ingrese la altura del rectángulo: ")
print(area_rectangulo(base, altura))

print("------------------------------------------------------")    
    
lado = input("Ingrese el lado del cuadrado: ")
print(area_cuadrado(lado))

print("------------------------------------------------------")

base_mayor = input("Ingrese la base mayor del trapecio: ")
base_menor = input("Ingrese la base menor del trapecio: ")
altura = input("Ingrese la altura del trapecio: ")
print(area_trapecio(base_mayor, base_menor, altura))

print("------------------------------------------------------")    
    
diagonal_mayor = input("Ingrese la diagonal mayor del rombo: ")
diagonal_menor = input("Ingrese la diagonal menor del rombo: ")
print(area_rombo(diagonal_mayor, diagonal_menor))

print("------------------------------------------------------")    

radio = input("Ingrese el radio del círculo: ")
print(area_circulo(radio))
    

