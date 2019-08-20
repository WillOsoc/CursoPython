for i in range(5,30,4):	#incluye 5, excluye 30, intervalo
	print(f"Valor de la variable: {i}")

print(len("juan"))

arroba=False
punto=False

mail="correo@dominio.do"

for i in range(len(mail)):
	if mail[i]=="@":
		arroba=True
	if mail[i]==".":
		punto=True

if arroba and punto:
	print("eMail tiene arroba y punto")
else:
	print("eMail incorrecto")