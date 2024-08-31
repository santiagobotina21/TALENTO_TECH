class Usuario():
    def __init__(self, nombre,edad:int, direccion,numeroCuenta, saldoActual):
        self.nombre = nombre
        self.edad = edad        
        self.direccion = direccion
        self.numeroCuenta = numeroCuenta
        self.saldoActual = saldoActual

    def depositar(self):
        cantidad = float(input("¿Que valor desea depositar?"))
        self.saldoActual+=cantidad
        print(f"Su saldo actual es de ${self.saldoActual}")
        
    def debitar(self):
        if self.saldoActual<=0:
            print(f"Actualmente su cuenta esta en ceros y por ende no cuenta con los fondos suficientes")
        else:
            cantidad = float(input("¿Que valor desea retirar?"))
            if cantidad>self.saldo:
                print(f"Actualmente no cuenta con los fondos suficientes para el valor que desea retirar")
            else:
                self.saldo-=cantidad
    
    def cumpleaños(self):
        self.edad+=1
        print(f"El usuario: {self.nombre} el dia de hoy esta cumpliendo {self.edad} años")




class Cliente(Usuario):
    def __init__(self, nombre,edad, direccion,numeroCuenta, saldoActual,idCliente,profesion):
        super().__init__(nombre,edad, direccion,numeroCuenta, saldoActual)
        self.idCliente = idCliente
        self.profesion = profesion
        self.prestamoEnCurso = False
        
    
    def solicitarPrestamo(self):
        self.prestamoEnCurso=True
        print(f"El usuario: {self.nombre} ha solicitado un prestamo")   

    def informacionDelUsuario(self):
        print(f"Este perro de nombre {self.nombre} tiene {self.patas} patas, es de raza {self.raza} y se encuentra olfateando")






perro1 = Perro(12, "Firulays", "Domestico","Marron","Labrador")

class Gato(Animal):
    def __init__(self, edad, nombre,tipo, color,raza):
        super().__init__(edad, nombre,tipo, color)
        self.patas = 4
        self.raza = raza
    
    def maullar(self):
        print(f"Este gato de nombre {self.nombre} tiene  {self.patas} patas y es de raza {self.raza} y se encuentra maullando")

    def trepar(self):
        print(f"Este gato de nombre {self.nombre} tiene {self.patas} patas, es de raza {self.raza} y se encuentra trepando")

gato1 = Gato(4, "Garfield", "Domestico","Naranja","persa")

class Serpiente(Animal):
    def __init__(self, edad, nombre,tipo, color,largo:float,diametro:float,raza,venenoza:bool):
        super().__init__(edad, nombre,tipo, color)
        self.largo = largo
        self.diametro = diametro
        self.raza = raza
        self.venenoza = venenoza
    
    def morder(self):
        if self.venenoza == True:
            print(f"La serpiente es de raza {self.raza}, tenga cuidado porque es venenoza")
        else:
            print(f"La serpiente es de raza {self.raza}, y no es venenoza")

    def cazar(self):
        print(f"La serpiente es de raza {self.raza}, mide {self.largo} mts de largo y {self.diametro} cms de diametro y se encuentra cazando")

serpiente1= Serpiente(4, "Anaconda", "Salvaje","Negra",2.5,80,"Boa constrictor",True)
serpiente2= Serpiente(4, "Anaconda", "Salvaje","Negra",2.5,80,"Mamba negra",False)

animal1.andar()
animal1.comer()
animal1.dormir()
print(animal1.tipo)

print("---------------------------------")

perro1.ladrar()
perro1.olfatear()
print(perro1.nombre)

print("---------------------------------")

gato1.maullar()
gato1.trepar()
print(gato1.nombre)

print("---------------------------------")

serpiente1.morder()
serpiente2.morder()
serpiente1.cazar()
print(serpiente1.raza)
