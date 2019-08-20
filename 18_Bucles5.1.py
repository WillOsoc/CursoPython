email=input("Introduce email: ")

for i in email:
	if i=="@":
		arroba=True
		break
else:	# se ejecuta al concluir todas las iteraciones del "for"
	arroba=False

print(arroba)