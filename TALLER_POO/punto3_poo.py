class Usuario():
    def __init__(self, nombre, edad: int, direccion, numeroCuenta, saldoActual):
        self.nombre = nombre
        self.edad = edad        
        self.direccion = direccion
        self.numeroCuenta = numeroCuenta
        self.saldoActual = saldoActual

    def depositar(self, cantidad=None):
        if cantidad is None:
            cantidad = float(input("¿Qué valor desea depositar? "))
        self.saldoActual += cantidad
        print(f"Su saldo actual es de ${self.saldoActual}")
        
    def debitar(self):
        if self.saldoActual <= 0:
            print(f"Actualmente su cuenta está en ceros y por ende no cuenta con los fondos suficientes")
        else:
            cantidad = float(input("¿Qué valor desea retirar? "))
            if cantidad > self.saldoActual:
                print(f"Actualmente no cuenta con los fondos suficientes para el valor que desea retirar")
            else:
                self.saldoActual -= cantidad
                print(f"Se ha debitado: {cantidad}. Saldo actual: {self.saldoActual}")
    
    def cumpleaños(self):
        self.edad += 1
        print(f"El usuario {self.nombre} hoy está cumpliendo {self.edad} años")


class Cliente(Usuario):
    def __init__(self, nombre, edad, direccion, numeroCuenta, saldoActual, idCliente, profesion):
        super().__init__(nombre, edad, direccion, numeroCuenta, saldoActual)
        self.idCliente = idCliente
        self.profesion = profesion
        self.prestamoEnCurso = False
        
    def solicitarPrestamo(self):
        self.prestamoEnCurso = True
        print(f"El usuario {self.nombre} ha solicitado un préstamo.")   

    def informacionDelUsuario(self):
        print(f"Datos del usuario {self.idCliente}: Nombre: {self.nombre}, Edad: {self.edad}, Dirección: {self.direccion}, Profesión: {self.profesion}, Número de cuenta: {self.numeroCuenta}, Saldo actual: {self.saldoActual}.")


class Empleado(Usuario):
    def __init__(self, nombre, edad, direccion, numeroCuenta, saldoActual, id_Empleado, cargo, sueldo):
        super().__init__(nombre, edad, direccion, numeroCuenta, saldoActual)
        self.id_Empleado = id_Empleado
        self.cargo = cargo
        self.sueldo = sueldo
        self.adelanto = 0

    def pagar_nomina(self):
        if self.adelanto > 0:
            print(f"Descontando adelanto de sueldo: {self.adelanto}")
            self.depositar(self.sueldo - self.adelanto)
            self.adelanto = 0
        else:
            self.depositar(self.sueldo)
            print(f"Nómina pagada. Saldo actual: {self.saldoActual}")

    def adelantar_sueldo(self, cantidad):
        if cantidad <= self.sueldo:
            self.adelanto += cantidad
            self.depositar(cantidad)
            print(f"Se ha adelantado un sueldo de {cantidad}. Adelanto total: {self.adelanto}")
        else:
            print("No se puede adelantar más del sueldo total.")

    def informacionDelEmpleado(self):
        print(f"Datos del empleado {self.id_Empleado}: Nombre: {self.nombre}, Edad: {self.edad}, Dirección: {self.direccion}, Cargo: {self.cargo}, Número de cuenta: {self.numeroCuenta}, Sueldo: {self.sueldo}.")



cliente1 = Cliente("Juan Lopez", 30, "Calle 123 B/La Carolona", "1234567890", 1000.0, "C001", "Ingeniero")
empleado1 = Empleado("Ana García", 28, "Avenida Santander 742", "0987654321", 2000.0, "E001", "Gerente", 3000.0)

print("---------------------------------")

cliente1.depositar(500)
cliente1.debitar()
cliente1.cumpleaños()
cliente1.solicitarPrestamo()
cliente1.informacionDelUsuario()

print("---------------------------------")

empleado1.pagar_nomina()
empleado1.adelantar_sueldo(2500)
empleado1.pagar_nomina()
empleado1.informacionDelEmpleado()
