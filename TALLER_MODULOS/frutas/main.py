
from frutas import Frutas

manzana = Frutas("Manzana", 1200, 100)

print("Descripción de la fruta:")
print(manzana.descripcion())

print("\nIngresar inventario:")
manzana.Ingresar_inventario(50)

print("\nVenta de fruta:")
total_venta = manzana.vender(30)
print(f"Total de la venta: ${total_venta}")

print("\nIntentar vender más unidades de las disponibles:")
manzana.vender(150)

print("\nDescripción de la fruta actualizada:")
print(manzana.descripcion())

