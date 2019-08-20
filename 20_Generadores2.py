def devuelve_ciudades(*ciudades):	# "*" indica q es una cantidad indeterminada de argumentos
	for elemento in ciudades:
		yield from elemento		# evita anidar un "for", para recorrer internamente el elemento

ciudades=devuelve_ciudades("Madrid", "Caracas","Medellin","Bogotá")

print(next(ciudades))
print(next(ciudades))
