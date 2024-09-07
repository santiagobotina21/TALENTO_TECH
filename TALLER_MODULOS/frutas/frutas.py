class Frutas():
    def __init__(self, nombre, precio_unidad, stock):
        self.nombre = nombre
        self.precio_unidad = precio_unidad        
        self.stock = stock


    def Ingresar_inventario(self, cantidad):
        try:
            if cantidad <= 0:
                return "Debe ingresar un valor mayor que cero."
            
            self.stock += cantidad
            print(f"Se han agregado {cantidad} unidades de {self.nombre}. Stock actual: {self.stock}")

        except ValueError:
            return "El dato ingresado no es numérico."
        
        
    def vender(self, cantidad):
        try:
            if cantidad <= 0:
                return "Debe ingresar un valor mayor que cero."
            
            if cantidad <= self.stock:
                self.stock -= cantidad
                total_venta = cantidad * self.precio_unidad
                return f"Venta realizada. {cantidad} unidades de {self.nombre} vendidas. Total: ${total_venta}"
            else:
                return f"No hay suficiente stock para vender {cantidad} unidades de {self.nombre}. Stock actual: {self.stock}"
            
        except ValueError:
            return "El dato ingresado no es numérico."
        
        
    def descripcion(self):
            return (f"Nombre: {self.nombre}\n"
                    f"Precio por unidad: ${self.precio_unidad}\n"
                    f"Stock disponible: {self.stock}")

        
