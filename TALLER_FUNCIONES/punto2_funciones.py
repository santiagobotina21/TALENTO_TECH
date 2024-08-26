# Escribir una funcion que calcule el area de un circulo, y otra que calcule el 
# volumen de un cilindro usando la primera funcion 

import math

def calcular_area_o_volumen():

    while True:
        eleccion = input("¿Qué deseas calcular? (1) Área de un círculo (2) Volumen de un cilindro (q) Salir: ").strip().lower()
        
        if eleccion == '1':
            while True:
                try:
                    radio = float(input("Ingresa el radio del círculo: "))
                    if radio < 0:
                        print("El radio no puede ser negativo. Intenta nuevamente.")
                        continue
                    break
                except ValueError:
                    print("Por favor, ingresa un número válido.")
            
            area = math.pi * (radio ** 2)
            print(f"El área del círculo con radio {radio} es: {area:.2f}")
        
        elif eleccion == '2':
            while True:
                try:
                    radio = float(input("Ingresa el radio de la base del cilindro: "))
                    altura = float(input("Ingresa la altura del cilindro: "))
                    if radio < 0 or altura < 0:
                        print("El radio y la altura no pueden ser negativos. Intenta nuevamente.")
                        continue
                    break
                except ValueError:
                    print("Por favor, ingresa un número válido.")
            
            area_base = math.pi * (radio ** 2)
            volumen = area_base * altura
            print(f"El volumen del cilindro con radio {radio} y altura {altura} es: {volumen:.2f}")
        
        elif eleccion == 'q':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Intenta nuevamente.")

calcular_area_o_volumen()
