class Animal():
    def __init__(self, edad, nombre,tipo, color):
        self.edad = edad
        self.nombre = nombre
        self.tipo = tipo
        self.color = color

    def andar(self):
        print(f"Soy un {self.nombre} y estoy andando")
        
    def comer(self):
        print(f"Soy un {self.nombre} y estoy comiendo")
    
    def dormir(self):
        print(f"Soy un {self.nombre} y estoy durmiendo")


animal1 = Animal(12, "Oso", "Salvaje","Marron")   

class Perro(Animal):
    def __init__(self, edad, nombre,tipo, color,raza):
        super().__init__(edad, nombre,tipo, color)
        self.patas = 4
        self.raza = raza
    
    def ladrar(self):
        print(f"Este perro de nombre {self.nombre} tiene  {self.patas} patas y es de raza {self.raza} y se encuentra ladrando")

    def olfatear(self):
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
