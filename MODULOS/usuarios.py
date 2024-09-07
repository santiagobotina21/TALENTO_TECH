class Usuario:
    def __init__(self,nombre,apellido,telefono):
        self.fitstName = nombre 
        self.lastName = apellido 
        self.phone = telefono 
        self.salty = 0 

    def consignar(self,cantidad):
        self.salty += cantidad 
        return f"Consignacion exitosa, el nuevo saldo es {self.salty}"
    
    def debitar(self,cantidad):
        if cantidad <= self.salty:
            self.salty -= cantidad 
            return f"Retiro exitoso, el nuevo saldo es {self.salty}"
        else:
            return f"Fondos insuficientes para realizar el retiro"
        
    def consulta(self):
        print(f"El usuario {self.fitstName} tiene un saldo de {self.salty}")