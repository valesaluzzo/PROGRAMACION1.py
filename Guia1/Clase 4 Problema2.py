'''SUELDO CON BONO
Un empleado cobra un sueldo base mensual. Además, recibe un bono del 15% sobre su sueldo.
Si el sueldo base es ingresado por teclado, determinar el sueldo final a cobrar.
'''

sueldoBase = int(input("Ingresar valor de su sueldo "))
bono =  (sueldoBase/100)*15
cantidad_a_cobrar = sueldoBase + bono
print("El total a pagar es : ",cantidad_a_cobrar)