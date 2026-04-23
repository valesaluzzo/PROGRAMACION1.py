'''COMPRA EN SUPERMERCADO
Un cliente realiza una compra en un supermercado y adquiere 3 productos. Los precios
son de $4500, $3200 y $2100. El supermercado aplica un descuento del 10% sobre el total de la compra.
Determinar cuanto debera pagar el cliente luego del descuento.'''

producto1 = int(input("Ingresar valor del producto 1: "))
producto2 = int(input("Ingresar valor del producto 2: "))
producto3 = int(input("Ingresar valor del producto 3: "))
totalProductos = producto1 + producto2 + producto3
descuento =  (totalProductos/100)*10
cantidad_a_pagar = totalProductos - descuento
print("El total a pagar es : ",cantidad_a_pagar)