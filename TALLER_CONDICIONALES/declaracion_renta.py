# 3.Pregunte el sueldo devengado por el usuario y realice el calculo 
# de cuanto debe pagar el usuario según sus ingresos

nombre = input("Ingrese su nombre: ")

salario = int(input(f"{nombre},Por favor ingrese su salario: "))

if (salario < 10000 and salario > 0 ): 
    print("Su impuesto es del 5 % ")
    impuesto = salario * 0.05             
    print(f"{nombre} Su impuesto es de {impuesto}") 

elif (salario > 10000 and salario <= 20000 ): 
    print("Su impuesto es del 15 % ")
    impuesto = salario * 0.15            
    print(f"{nombre} Su impuesto es de {impuesto}")  

elif (salario > 20000 and salario <= 35000 ): 
    print("Su impuesto es del 20 % ")
    impuesto = salario * 0.20           
    print(f"{nombre} Su impuesto es de {impuesto}")       
                                                    
elif (salario > 35000 and salario <= 60000 ): 
    print("Su impuesto es del 30 % ")
    impuesto = salario * 0.30             
    print(f"{nombre} Su impuesto es de {impuesto}") 

elif (salario > 60000 ): 
    print("Su impuesto es del 45 % ")
    impuesto = salario * 0.45            
    print(f"{nombre} Su impuesto es de {impuesto}")

else:
    print("Usted ingreso un valor fuera del rango")