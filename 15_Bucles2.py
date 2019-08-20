list01=["uno","dos","tres"]

for i in list01:
	print("Hola " + str(i), end=" ")

print()
for i in "pepe@python.com":
	if (i=="@"):
		mail=True
	print(i)

if mail:
	print("Correcto")
else:
	print("Incorrecto")

for i in range(5):
	print(i)
