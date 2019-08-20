def evaluacion(edad_u):
	val01="Bienvenido"	#variables pertenecen solo a su ámbito
	if edad_u>50:
		val01="Estás muy viejo"
	return val01

print("Validar Edad de Usuario")
print("")

edad=int(input("Introduce tu edad: "))	#todo input es considerado un string

if edad<18:
	analisis="Eres un pelado"
elif edad>100:
	analisis="Edad incorrecta"
else:
	analisis=evaluacion(edad)

print("Resultado de análisis: " + analisis)
