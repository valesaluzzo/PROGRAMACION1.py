'''ENTRADA AL CINE
Un cine cobra $3500 por entrada. Si una persona compra varias entradas, obtiene un descuento del 20% sobre el total.
Ingresar la cantidad de entradas y calcular cuánto deberá pagar.
'''

entradaIndivudual = int(input("Ingresar el valor de la entrada: "))
cantidadEntradas= int(input("Ingresar la cantidad de entradas a adquirir: "))
entradasTotal = cantidadEntradas * entradaIndivudual    #Calculo la cantidad de entradas que compro por el precio de la entrada individual
if cantidadEntradas >= 2:
    descuento = (entradasTotal/100)*20
    totalPagar= entradasTotal - descuento
    print("El total a pagar es: ",totalPagar)
else:
    print("El total a pagar es: ",entradaIndivudual)
