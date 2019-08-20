import time

class Coche():
	
	def __init__(self, id):	#Constructor --> __nombre__
		self.__cocheId=id
		self.__largoChasis=250
		self.__anchoChasis=150
		self.__ruedas=4		# Encapsulada --> __propiedad, no puede ser modificada
		self.__enmarcha=False

# una función, no pertenece a la clase
# un método, pertenece a la clase

	def arrancar(self,avanzar):	#self hace referencia a la instancia propia de la clase que hace el llamado
		self.__enmarcha=avanzar
		
		if(self.__enmarcha):
			if self.__chequeo_interno():
				print("Chequeo interno correcto")
				return("Coche " + str(self.__cocheId) + " está en marcha")
			else:
				print("Alerta. Revisar vehículo")
				return("El vehículo no se debe poner en marcha")
		else:
			return("Coche " + str(self.__cocheId) + " está detenido")


	def estado(self):
		print("\nCoche",self.__cocheId,"tiene",self.__largoChasis,"cms de largo y",self.__anchoChasis,"cms de ancho, tiene",self.__ruedas,"ruedas") 


	# Video 28 - Encapsulación de métodos
	def __chequeo_interno(self):
		print("Realizando chequeo interno...")
		time.sleep(3)

		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
			return True
		else:
			return False

# Crear objeto, crear instancia, instanciar clase, ejemplarizar clase
Coche01=Coche("01") # Pasa el propio objeto como parámetro

Coche01.estado()
print(Coche01.arrancar(True))	#Dentro de print, porque método devuelve un valor y no lo imprime en pantalla

print("\n----- Segundo Coche -------")

Coche02=Coche("02")

Coche02.__ruedas=23 # No hace efecto porque la propiedad está encapsulada
Coche02.estado()
print(Coche02.arrancar(False))
# print(Coche02.__chequeo_interno())  # No hace efecto porque el método está encapsulado
