edad=int(input("Ingresa tu edad: "))

def evaluaEdad(edad):

	if edad<0:
		raise NameError("Edad no válida")

	if edad<20:
		return "Eres muy joven"
	elif edad<40:
		return "Eres joven"
	elif edad<65:
		return "Eres maduro"
	elif edad<100:
		return "Cuídate..."

try:
	print(evaluaEdad(edad))
except NameError:
	print("Has introducido una edad no válida")
finally:
	print("El programa ha finalizado")