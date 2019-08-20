# Diccionario
# clave:valor

diccionario01={"Alemania":"Berlin","Francia":"Paris","España":"Madrid","Venezuela":"Caracas"}
diccionario01["Italia"]="Lisboa"
diccionario01["Italia"]="Roma"	#Corregir o sobreescribir un valor
del diccionario01["Francia"]

diccionario02={"Colombia":"Bogotá",12:"años","texto":34}

tupla01=["España","Francia","Reino Unido","Alemania"]
diccionario03={tupla01[0]:"Madrid",tupla01[1]:"Paris",tupla01[2]:"Londres",tupla01[3]:"Berlin"}

diccionario04={
	"clave1":"uno",
	"clave2":2,
	3:"tres",
	"clave4":{
		"valores":[4.1,4.2,4.3]
		},
	5:{
		"valores":(5.1,5.2,5.3)
		}
	}

print(diccionario01["España"])
print(diccionario01)
print(diccionario02)
print(diccionario03)
print(diccionario04)
print(diccionario04["clave4"])

print(diccionario04.keys())
print(diccionario04.values())
print(len(diccionario04))