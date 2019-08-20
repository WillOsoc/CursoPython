i=1

while i<=10:
	print(f"Ejecución Nro. {i}")
	i=i+1

print("Fin de la Ejecución")


edad=int(input("Introduce tu edad: "))

while edad<0:
	print("Edad no válida. Intenta de nuevo")
	edad=int(input("Introduce tu edad: "))

print(f"Edad del estudiante: {edad}")