# Escribir una funcion que calcule el total de una factura tras aplicarle el IVA. La funcion
# debe recibir la cantidad sin IVA y el porcentaje del IVA a aplicar, y devolver  el total 
# de la factura. Si se invoca la funcion sin pasarle el porcentaje de IVA, debera aplcicar un 21%

def calcular_total_factura():    
    while True:
        try:
            subtotal_sin_iva = float(input("Ingresa el subtotal sin IVA: "))
            break
        except ValueError:
            print("Por favor, ingresa un número válido.")

    calcular_iva = input("¿Deseas especificar el porcentaje de IVA? (s/n): ").strip().lower()

    if calcular_iva == 's':

        while True:
            try:
                porcentaje_iva = float(input("Ingresa el porcentaje de IVA: "))
                break
            except ValueError:
                print("Por favor, ingresa un número válido.")
    else:
        porcentaje_iva = 21
        print(" Se aplico el 21% de IVA por defecto.")

    iva = subtotal_sin_iva * (porcentaje_iva / 100)
    total_con_iva = subtotal_sin_iva + iva
    print(f"El total de la factura con IVA incluido es: {total_con_iva:.2f}")


calcular_total_factura()



            
    