'''CONSUMO DE COMBUSTIBLE
Un vehículo consume cierta cantidad de litros de combustible en un viaje. El precio del litro de nafta es de $980.
Si el usuario ingresa la cantidad de litros consumidos, calcular el costo total del viaje.
'''

litroNafta = int(input("Ingresar el valor del litro de nafta: "))
litrosConsumidos = int(input("Ingresar la cantidad de litros de nafta consumidos: "))
costoViaje = litroNafta * litrosConsumidos
print("El costo total del viaje es: ",costoViaje)