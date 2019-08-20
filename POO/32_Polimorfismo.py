class Coche():

	def desplazamiento(self):
		print("Me desplazo en 4 ruedas")

class Moto():

	def desplazamiento(self):
		print("Me desplazo en 2 ruedas")

class Camion():

	def desplazamiento(self):
		print("Me desplazo en 6 ruedas")

def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()

vehiculo01=Moto()
vehiculo02=Coche()
vehiculo03=Camion()

desplazamientoVehiculo(vehiculo01)
desplazamientoVehiculo(vehiculo02)
desplazamientoVehiculo(vehiculo03)