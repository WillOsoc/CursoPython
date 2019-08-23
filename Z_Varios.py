# Crea una lista de 10 elementos (range(1,11))
# donde cada elemento es el cuadrado de "x" (x**2)
square=[x**2 for x in range(1,11)]
print(square)


diccionario01={"Alemania":"Berlin","Francia":"Paris","España":"Madrid","Venezuela":"Caracas"}
diccionario01["Italia"]="Lisboa"
diccionario01["Italia"]="Roma"

# Imprime cada key:value pair, como una tupla ex.('Alemania','Berlin')
print(diccionario01)
for i in diccionario01.items():
	print(i)

set01={1,2,2,3,3,3,4,4,4,4}
print(4 in set01)	# Está el valor "4" en el set? --> devuelve "True"

set02={"uno","dos",3,4,"dos"}
print(set02)	# No mantiene el orden original

'''triple comilla simple
para comentar'''

"""también triple
comilla doble"""

#Puedes tener varias instrucciones en una misma línea
#Separada por ";"
var01="hola"; print(var01)

print(type(square))