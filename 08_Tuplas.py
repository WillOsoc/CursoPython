#Listas inmutables

tupla01=("Will",11,"03",1978,"Will")

lista01=list(tupla01)

tupla02=tuple(lista01)

nombre,dia,mes,agno,nombre2=tupla01	#desempaquetado. asigna etiqueta a elementos en tupla

print(tupla01[2])
print(tupla01)		# Imprime toda la lista (no hace falta ":" como en la lista)
print(lista01[:])
print(tupla02)
print("Will" in tupla02)
print(tupla02.count("Will"))
print(len(tupla02))	# Cuantos elementos tiene
print(len(lista01))	# Cuantos elementos tiene
print(agno)