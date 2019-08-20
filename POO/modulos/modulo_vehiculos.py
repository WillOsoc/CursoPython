class Vehiculo():

	def __init__(self,marca,modelo):
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("\nMarca;",self.marca,"\nModelo:",self.modelo,"\nEn Marcha:",self.enmarcha,
			"\nAcelerando:",self.acelera,"\nFrenando:",self.frena)

class Moto(Vehiculo):
	hcaballito=""

	def caballito(self):
		if self.enmarcha:
			self.hcaballito="Haciendo caballito"
			
	def estado(self):
		print("\nMarca;",self.marca,"\nModelo:",self.modelo,"\nEn Marcha:",self.enmarcha,
			"\nAcelerando:",self.acelera,"\nFrenando:",self.frena,"\n",self.hcaballito)

class Furgoneta(Vehiculo):
	carga="La Furgoneta no está cargada"

	def cargar(self,cargado):
		if cargado:
			self.carga="La Furgoneta está cargada"
		else:
			self.carga="La Furgoneta no está cargada"
		
	def estado(self):
		print("\nMarca;",self.marca,"\nModelo:",self.modelo,"\nEn Marcha:",self.enmarcha,
			"\nAcelerando:",self.acelera,"\nFrenando:",self.frena,"\n",self.carga)

class VElectricos(Vehiculo):

	def __init__(self,marca,modelo):
		super().__init__(marca,modelo)
		self.autonomia=100
		self.cargando=False

	def cargarEnergia(self):
		self.cargando=True

	def estado(self):
		super().estado()
		print("\nAutonomia:",self.autonomia,"\nCargando:",self.cargando)

class BiciElec(VElectricos):
	
	def __init__(self,marca,modelo):
		super().__init__(marca,modelo)
		self.tamano_rueda=20

	def estado(self):
		super().estado()
		print("\nTamaño de Rueda:",self.tamano_rueda)
