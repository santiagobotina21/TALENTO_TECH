# COMENTARIO
print("Hola mundo")

edad=18

#Imprimiendo la variable edad
print(edad)

edad=input("Ingrese su edad: ")

if int(edad) >=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


## TIPOS DE DATOS

flag=True
flagF=False
number=17
number2=20
nota1=1.8
nota2=3.5
name="Santiago Esteban"
last_name="Botina Arciniegas"
peers=(2,4,6,8,10,11)
odd=(1,3,5,7,9)
concatenar=name+" "+last_name


print('la variable: ',flag,'es de tipo: ',type(flag))
print('la variable: ',flagF,'es de tipo: ',type(flagF))
print('la variable: ',number,'es de tipo: ',type(number))
print('la variable: ',number2,'es de tipo: ',type(number2))
print('la variable: ',nota1,'es de tipo: ',type(nota1))
print('la variable: ',nota2,'es de tipo: ',type(nota2))
print('la variable: ',name,'es de tipo: ',type(name))
print('la variable: ',last_name,'es de tipo: ',type(last_name))
print('la variable: ',peers,'es de tipo: ',type(peers))
print('la variable: ',odd,'es de tipo: ',type(odd))
print(concatenar)


