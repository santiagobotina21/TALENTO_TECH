#1. Cree un programa que permita clasificar a un usuario  en un rango de edad.
nombre=(input("Ingrese su nombre: "))

# SUMA
edad = int(input(f"{nombre},Por favor ingrese su edad: "))

if edad >=0 and edad <=5:
    print("Usted se encuentra en la primera infancia")
elif edad >=6 and edad <=11:
    print("Usted se encuentra en la infancia")
elif edad >=12 and edad <=14:
    print("Usted se encuentra en la adolescencia")
elif edad >=15 and edad <=26:
    print("Usted se encuentra en la juventud")
elif edad >=27 and edad <=59:
    print("Usted se encuentra en la adultez")
elif edad >=60:
    print("Usted se encuentra en la categoria de personas mayores")
else:
    print("Por favor ingrese un valor dentro del rango")
