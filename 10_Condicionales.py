print("Programa de Evaluación")

nota_alumno=input("Introduce la nota: ")	#todo input es considerado un string

def evaluacion(nota):
	val01="Aprobado"	#variables pertenecen solo a su ámbito
	if nota<5:
		val01="Reprobado"
	return val01

print("El alumno ha sido: " + evaluacion(int(nota_alumno)))

