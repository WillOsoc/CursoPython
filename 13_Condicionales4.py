print("Sistema de Evaluación de Becas")

distancia=(int(input("Introduce la distancia en Kms: ")))
hermanos=(int(input("Introduce número de hermanos: ")))
salario=(int(input("Introude ingreso familiar anual: ")))

if distancia>40 and hermanos>2 or salario<15000:
	print("Tienes derecho a Beca")
	asignaturas_disp="Informática - Administración - Matemáticas"
	print("Asignaturas disponibles:")
	print(asignaturas_disp)
	asignatura=input("Escribe la asignatura seleccionada: ")

	if asignatura.lower() in asignaturas_disp.lower():
		print("Inscrito en: " + asignatura)
	else:
		print("La asignatura no está disponible")

else:
	print("No tienes derecho a Beca")

