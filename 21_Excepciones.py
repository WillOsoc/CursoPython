def suma(num1,num2):
	return num1+num2

def resta(num1,num2):
	return num1-num2

def multi(num1,num2):
	return num1*num2

def divi(num1,num2):
	try:	# Try: --> debe tener al menos uno de los dos (except:) o (finally:)
		return num1/num2
	except ZeroDivisionError:
		print("División entre cero(0) no permitida")
		return "Operación NO permitida"

while True:
	try:
		op1=int(input("Introduce el primer número: "))
		op2=int(input("Introduce el segundo número: "))
		break
	except ValueError:
		print("\nUno de los valores introducidos no es válido. Intenta de nuevo")

operacion=(input("\nQué operacion desea realizar? suma(S), resta(R), multiplicación(M), división(D): ").lower())

if (operacion=="suma") or (operacion=="s"):
	print(suma(op1,op2))

elif (operacion=="resta") or (operacion=="r"):
	print(resta(op1,op2))

elif (operacion=="multiplicación") or (operacion=="m"):
	print(multi(op1,op2))

elif (operacion=="división") or (operacion=="d"):
	print(divi(op1,op2))

else:
	print("Operación inválida")

print("\nAquí sigue el resto del cógido")