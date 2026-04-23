'''PRECIO CON IVA
Un producto tiene un precio base. Se debe calcular el precio final con IVA del 21%.
El precio base debe ser ingresado por el usuario.
'''

precioBase = int(input("Ingresar el precio base: "))
iva =  (precioBase/100)*21
precioFinal = precioBase + iva
print("El precio final es : ",precioFinal)