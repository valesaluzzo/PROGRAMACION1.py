'''PROPINA EN EL RESTAURANTE
En un restaurante, el cliente desea dejar una propina del 12% sobre el total consumido.
Si el monto total de la cuenta es ingresado por teclado, calcular el total a pagar incluyendo la propina.
'''

totalCuenta = int(input("Ingresar monto total de la cuenta: "))
propina =  (totalCuenta/100)*12
cantidad_a_pagar = totalCuenta + propina
print("El total a pagar es : ",cantidad_a_pagar)

