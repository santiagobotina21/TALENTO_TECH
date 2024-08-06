# 4. Usando try – except, convierta los valores de una lista a enteros e ingréselos a una nueva 
# lista, aquellos que no puedan ser convertidos deben también agregarse a la lista como str, 
# floats, lista o como valores booleanos

lista = ["1","Juan","3",True,"16,4","45","Hola","32",["hola","mundo"]]
lista2 = []


for item in lista:
    try:
        nuevo_item = int(item)
        lista2.append(nuevo_item)
    except (ValueError, TypeError):        
        nuevo_item = (item)
        lista2.append(nuevo_item)
        print("El valor no se puede pasar a INT")

for item in lista2:
    print(f"{item}:{type(item)}")



print("\nEsta es la lista inicial", lista)
print("Esta es la lista con enteros", lista2)
