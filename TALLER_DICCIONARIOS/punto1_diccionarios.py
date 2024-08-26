# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono
# y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje
# <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es
# <teléfono>.

diccionario={}

diccionario["nombre"] = input("Ingrese su nombre: ")
diccionario["edad"] = int(input("Ingrese su edad: "))
diccionario["direccion"] = input("Ingrese su direccion: ")
diccionario["telefono"] = input("Ingrese su telefono: ")

print(f"{diccionario['nombre']} tiene {diccionario['edad']} años, vive en {diccionario['direccion']} y su número de teléfono es {diccionario['telefono']}.")


            
    