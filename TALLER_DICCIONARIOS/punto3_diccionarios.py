# Escriba un programa que permita almacenar los siguientes datos de usuarios
# Llave: Numero de documento
# Valor: Diccionario con los siguientes datos

usuarios = {
    "123456789": {
        "Nombre": "Juan",
        "Apellido": "Pérez",
        "Dirección": "Calle Falsa 123",
        "Teléfono": "555-1234",
        "Placas": ["ABC123", "XYZ789"]
    },
    "987654321": {
        "Nombre": "Ana",
        "Apellido": "Gómez",
        "Dirección": "Avenida Siempre Viva 742",
        "Teléfono": "555-5678",
        "Placas": ["LMN456"]
    },
    "456789123": {
        "Nombre": "Luis",
        "Apellido": "Martínez",
        "Dirección": "Plaza Central 45",
        "Teléfono": "555-8765",
        "Placas": ["OPQ321"]
    }
}

# Dada una placa revise en el diccionario si existe un propietario para la misma, y
# muestre en pantalla la información de ese propietario

def buscar_placa(placa):

    for datos in usuarios.values():
        if placa in datos['Placas']:
            print("Datos del propietario:")
            print(f"Nombre: {datos['Nombre']}")
            print(f"Apellido: {datos['Apellido']}")
            print(f"Dirección: {datos['Dirección']}")
            print(f"Teléfono: {datos['Teléfono']}")
            return
    
    print("No se encontró ningún propietario para la placa o la placa no existe.")

# buscar_placa("LMN456")


# Dado un numero de documento muestre cuantos vehículos están asociados a ese
# usuario, junto con sus placas

def buscar_documento(documento):

    if documento in usuarios:
        placas = usuarios[documento]['Placas']
        print("Vehículos asociados a este usuario:")
        print(f"Cantidad de vehículos: {len(placas)}")
        print(f"Placas: {', '.join(placas)}")
    else:
        print("No se encontró ningún usuario con este número de documento.")

# buscar_documento("123456789")


# Adicione una placa a un usuario determinado y al final muestre la lista 
# de vehículos de ese usuario

def adicionar_placa(documento,placa):

    if documento in usuarios:
        placas = usuarios[documento]['Placas']
        placas.append(placa)
    
        print("Vehículos asociados a este usuario:")
        print(f"Cantidad de vehículos: {len(placas)}")
        print(f"Placas: {', '.join(placas)}")
    else:
        print("No se encontró ningún usuario con este número de documento.")

# adicionar_placa("123456789","XBS03D")


# Elimine una placa de un vehículo, en caso de que esta no esté asociada a ese usuario,
# envíe un mensaje informando la situación

def eliminar_placa(documento, placa):

    if documento in usuarios:
        placas = usuarios[documento]['Placas']
        
        if placa in placas:
            placas.remove(placa)
            print(f"Se eliminó la placa: {placa}, del usuario con número de documento {documento}")
        else:
            print(f"La placa: {placa} no se encontró para el usuario con número de documento {documento}")
        
        # Mostrar la lista actualizada de placas
        print("Vehículos asociados a este usuario:")
        print(f"Cantidad de vehículos: {len(placas)}")
        print(f"Placas: {', '.join(placas)}")
    else:
        print("No se encontró ningún usuario con este número de documento")

# eliminar_placa("123456789","XBS03D")


#Actualice la dirección y teléfono de un usuario

def actualizar_direccion_telefono(documento, nueva_direccion, nuevo_telefono):

    if documento in usuarios:
        usuarios[documento]['Dirección'] = nueva_direccion
        usuarios[documento]['Teléfono'] = nuevo_telefono
        print(f"Dirección y teléfono actualizados para el usuario con número de documento {documento}.")
        print(f"Dirección: {nueva_direccion}")
        print(f"Teléfono: {nuevo_telefono}")
    else:
        print("No se encontró ningún usuario con este número de documento.")

# actualizar_direccion_telefono("123456789", "Nueva Calle 456", "555-9999")


# Permita hacer un cambio de placa de un usuario a otro,
# debe verificar que ambos usuarios existen y que además la placa esta asociada al usuario propietario

def cambiar_placa(documento_origen, documento_destino, placa):

    if documento_origen in usuarios and documento_destino in usuarios:
        if placa in usuarios[documento_origen]['Placas']:
            # Eliminar la placa del usuario origen
            usuarios[documento_origen]['Placas'].remove(placa)
            # Añadir la placa al usuario destino
            usuarios[documento_destino]['Placas'].append(placa)
            print(f"La placa {placa} ha sido transferida de {documento_origen} a {documento_destino}.")
        else:
            print(f"La placa {placa} no está asociada al usuario con número de documento {documento_origen}.")
    else:
        if documento_origen not in usuarios:
            print(f"No se encontró ningún usuario con el número de documento {documento_origen}.")
        if documento_destino not in usuarios:
            print(f"No se encontró ningún usuario con el número de documento {documento_destino}.")

    # Mostrar la lista actualizada de placas para ambos usuarios
    print(f"Vehículos asociados al usuario {documento_origen}:")
    print(f"Cantidad de vehículos: {len(usuarios[documento_origen]['Placas'])}")
    print(f"Placas: {', '.join(usuarios[documento_origen]['Placas'])}")
    
    print(f"Vehículos asociados al usuario {documento_destino}:")
    print(f"Cantidad de vehículos: {len(usuarios[documento_destino]['Placas'])}")
    print(f"Placas: {', '.join(usuarios[documento_destino]['Placas'])}")

# cambiar_placa("123456789", "456789123", "XYZ789")


# Verifique si una placa esta asociada a mas de un usuario, a un único usuario o a ningún usuario

def verificar_placa(placa):

    usuarios_asociados = [documento for documento, datos in usuarios.items() if placa in datos['Placas']]
    
    if len(usuarios_asociados) > 1:
        print(f"La placa {placa} está asociada a más de un usuario.")
        for doc in usuarios_asociados:
            print(f"Usuario: {doc}")
    elif len(usuarios_asociados) == 1:
        print(f"La placa {placa} está asociada a un único usuario.")
        print(f"Usuario: {usuarios_asociados[0]}")
    else:
        print(f"La placa {placa} no está asociada a ningún usuario.")

# Ejemplo de uso
verificar_placa("XYZ789")
verificar_placa("LMN456")
verificar_placa("NONEXISTENT")



