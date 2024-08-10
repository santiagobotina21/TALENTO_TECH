# def saludar(nombre):
#     saludo= f"Hola {nombre}"
#     return saludo

# print(saludar("Juan"))
# print(saludar("Santiago"))



# def sumar(numero1,numero2):
#     suma=numero1+numero2
#     return suma

# print(sumar(2,8))
# print(sumar(8,8))

# def multiplicar(numero1,numero2,numero3):
#     multiplicacion=numero1*numero2*numero3
#     return multiplicacion

# print(multiplicar(3,3,2))
# print(multiplicar(8,9,6))


def calcular_hipotenusa(CO,CA):
    try:
        CO=float(CO)
        CA=float(CA)
    except:
        return "Debe ingresar valores numericos"
    else:
        if CO <=0 or CA <=0:
            return "Valores no validos, procure ingresar valores mayores a cero"
        else:
            h= ((CO**2)+(CA**2)) ** (1/2)
            
            
    