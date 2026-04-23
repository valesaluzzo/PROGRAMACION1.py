'''PAGO POR HORAS TRABAJADAS
Un trabajador cobra $2500 por hora.
Si el usuario ingresa la cantidad de horas trabajadas, calcular el sueldo total.
'''

cobro_por_hora = int(input("Ingresar el monto de cobro por hora: "))
horasTrabajadas = int(input("Ingresar cantidad de horas trabajadas: "))
sueldoTotal = cobro_por_hora * horasTrabajadas
print("El sueldo total es : ",sueldoTotal)