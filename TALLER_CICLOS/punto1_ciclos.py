# 1. Escriba un programa que cuente hasta el numero 100 avanzando 5 unidades en cada iteración

import time 

contador=0

while contador<=100:
    print("Contador: ",contador)
    contador+=5
    time.sleep(0.2)
else:
    print("Hemos terminado el conteo")