def dividir(num,den):
    try:
        num=float(num)
        den=float(den)
        return f"El resultado es {num/den}"
    except ZeroDivisionError:
        return "No es posible dividir por cero"
    except ValueError:
        return "Los datos ingresados no son numericos"