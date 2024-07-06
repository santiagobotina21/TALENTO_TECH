# 4. La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los
# ingredientes para cada tipo de pizza aparecen a continuación:
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
# y en función de su respuesta le muestre un menú con los ingredientes disponibles.


print("Hola bienvenido a la pizzería Bella Napoli")
nombre=(input("Por favor ingrese su nombre: "))

respuesta = (input(f"{nombre},¿Desea adquirir una pizza vegetariana? Responda con SI o NO: "))

if respuesta=="SI" or respuesta=="si":
    print("Los ingredientes de la pizza vegetariana son:Pimiento y tofu.")
elif respuesta=="NO" or respuesta=="no":
    print("Los ingredientes de la pizza NO vegetariana son:Peperoni, Jamón y Salmón.")
else:
    print("La respuesta no es valida")
