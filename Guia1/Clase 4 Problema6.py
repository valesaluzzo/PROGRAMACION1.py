'''CONVERSION DE TEMPERATURA
Se desea convertir una temperatura ingresada en grados Celsius a grados Fahrenheit.
La fórmula es:
F = (C × 9/5) + 32
Mostrar el resultado.
'''
c = int(input("Ingresar los grados Celsius: "))  #c = grados Celsius
f = (c * 9/5) + 32
print("La conversion de Celsius a Fahrenheit es: ", f)