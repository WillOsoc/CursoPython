import math

print("Calcular raíz cuadrada")

def calcSqrt(num):
	if num<0:
		raise ValueError("El número no puede ser negativo")
	else:
		return math.sqrt(num)

inputnum=int(input("\nIngrese número: "))

try:
	print(f"\nLa raiz cuadrada de {inputnum} es {calcSqrt(inputnum)}")
except ValueError as ValorNegativo:
	print(ValorNegativo)

print("\nPrograma finalizado")