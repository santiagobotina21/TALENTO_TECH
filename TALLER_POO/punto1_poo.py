class UsuarioBanco ():
    def __init__(self, nombre,edad,cedula,telefono):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
        self.telefono = telefono
        self.saldo = 0

     
    def depositar(self):
        deposito = float(input("¿Que valor desea depositar?"))
        self.saldo+=deposito
        print(f"Su saldo actual es de ${self.saldo}")
      
        
    def retirar(self):
        if self.saldo<=0:
            print(f"Actualmente su cuenta esta en ceros y por ende no cuenta con los fondos suficientes")
        else:
            retiro = float(input("¿Que valor desea retirar?"))
            if retiro>self.saldo:
                print(f"Actualmente no cuenta con los fondos suficientes para el valor que desea retirar")
            else:
                self.saldo-=retiro


    def consultar(self):
        print(f"Su saldo actual es de ${self.saldo}")


usuario1 = UsuarioBanco("Santiago Botina", 24,1017793242,3188541987)
usuario1.depositar()
usuario1.retirar()
usuario1.consultar()
   

