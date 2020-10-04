class jugadas:
    
	def __init__(self, fecha, nivel, tiempo,tiempoEleccionP,tiempoPensandoPC, jugadorJ, jugadorC, turno, letras,puntos, primerTurno, desocupadas, matriz):
		self._fecha = fecha
		self._nivel = nivel 
		self._tiempo = tiempo
		self._tiempoEleccionP = tiempoEleccionP
		self._tiempoPensandoPC = tiempoPensandoPC
		self._jugadorJ = jugadorJ
		self._jugadorC = jugadorC
		self._turno = turno 
		self._cantCambios = 0
		self._letras = letras
		self._puntos = puntos 
		self._topTen = {}
		self._primerTurno = primerTurno
		self._desocupadas = desocupadas
		self._matriz = matriz
		self._contador = 0
   
	def set_fecha(self, fecha):
		self._fecha = fecha
    
	def get_fecha(self):
		return self._fecha
     
	def set_nivel(self, nivel):
		self._nivel = nivel
 
	def get_nivel(self):
		return self._nivel
 
	def get_tiempo(self):
		return self._tiempo
	
	def get_tiempoPensandoPC(self):
		return self._tiempoPensandoPC
	
	def get_tiempoEleccionP(self):
		return self._tiempoEleccionP
 
	def set_tiempo(self, tiempo):
		self._tiempo = tiempo
	
	def set_tiempoPensandoPC(self, tiempoPensandoPC):
		self._tiempoPensandoPC = tiempoPensandoPC
	
	def set_tiempoEleccionP(self, tiempoEleccionP):
		self._tiempoEleccionP = tiempoEleccionP
    
	def set_jugadorJ(self, jugadorJ):
		self._jugadorJ = jugadorJ
 
	def set_jugadorC(self, jugadorC):
		self._jugadorC = jugadorC
    
	def set_turno(self, turno):
		self._turno = turno
  
	def set_letras(self, letras):
		self._letras = letra

	def get_letras(self):
		return self._letras
  
	def set_topten(self, dic):
		self._topTen = dic
	
	def get_topten(self):
		return self._topTen
 
	def get_puntos(self):
		return self._puntos
  
	def set_turno(self, turno):
		self._turno = turno
  
	def get_jugadorJ(self):
		return self._jugadorJ 
	 
	def get_jugadorC(self):  
		return self._jugadorC
 
	def get_cantCambios(self):  
		return self._cantCambios
		
	def set_primerTurno(self):
		return self._primerTurno
		
	def get_primerTurno(self):
		return self._primerTurno
 
	def sumarCambio(self):  
		self._cantCambios+=1 
     
	def set_desocupadas(self,desocupadas):
		self._desocupadas=desocupadas
		
	def get_desocupadas(self):
		return self._desocupadas
		
	def set_matriz(self,matriz):
		self._matriz=matriz
		
	def get_matriz(self):
		return self._matriz
	
	def set_contador(self,contador):
		self._contador=contador
		
	def get_contador(self):
		return self._contador
	
