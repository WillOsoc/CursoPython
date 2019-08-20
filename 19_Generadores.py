#Usando una lista
def generaParesL(limite):

	num=1
	miLista=[]

	while num<limite:
		miLista.append(num*2)
		num+=1

	return miLista

print(generaParesL(10))

# Usando Generador
def generaParesG(limite):

	num=1

	while num<limite:
		yield num*2
		num+=2

devuelvePares=generaParesG(10)

print(next(devuelvePares))
print("Código después de leer generador")
print(next(devuelvePares))
print("Código después de leer generador")
print(next(devuelvePares))
print("Código después de leer generador")

for i in devuelvePares:
	print(i)

for i in devuelvePares:
	print(i)