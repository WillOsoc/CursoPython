print("Contar caracteres y espacios en blanco")
print("")

frase=input("Ingresa una frase: ")
contador=0
espacios=0

for i in frase:
	if i==" ":
		espacios=espacios+1
		continue
	contador+=1

print(f"""La frase tiene {contador} caracteres
y {espacios} espacios en blanco""")
