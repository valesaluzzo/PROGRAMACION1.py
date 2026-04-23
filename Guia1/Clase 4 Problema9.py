'''DESCUENTO POR CANTIDAD
Una tienda vende camisetas a $8000 cada una.
Si el cliente compra más de 5, obtiene un descuento del 25% sobre el total.
Ingresar la cantidad de camisetas y calcular el monto final.
'''

camiseta = int(input("Ingresar el valor de una camiseta: "))
cantidadCamisetas = int(input("Ingresar la cantidad de camisetas compradas: "))
precioTotal = camiseta * cantidadCamisetas
if camiseta > 5:
    descuento = (precioTotal/100)*25
    totalPagar= precioTotal - descuento
    print("El total a pagar es: ",totalPagar)
else:
    print("El total a pagar es: ",precioTotal)