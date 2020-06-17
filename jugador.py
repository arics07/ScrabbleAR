import random

class jugador:
        
	def __init__(self, nom):
		self._nombre = nom
		self._puntaje = 0 
		self._atril = []
		self._turno = False
   
	def get_nombre(self):
		return self._nombre
       
	def get_puntaje(self):
		return self._puntaje
        
	def set_puntaje(self, nuevo_puntaje):
		self._puntaje = nuevo_puntaje
       
	def get_atril(self):
		return self._atril
  
	def set_atril(self, nuevo_atril):
		self._atril = nuevo_atril
    
	def verificoatrilcompleto(self,atril):
		completo=True
		print(atril)			
		for i in atril:
			print(i)
			if i == 0:
				completo=False
		return completo
        			     						
	def sacarAtril(self, pos):
		self._atril[pos] = " "  
             
	def set_jugar(self):
		self._turno = True
  
	def get_turno(self):
		return self._turno 
        
	def set_dejarJugar(self):
		self._turno = False 
    
	def elijoL(self, letras):
		ll=[]
		for i in range(7):
			#elije una letra aleatoriamente de la lista de letras
			letra=random.choice(letras)		 
			#la agrega a la lista de la jugada actual
			ll.append(letra)
			#se borra la letra de esa lista 
			letras.remove(letra)
		return self.set_atril(ll) 
           
	#Cuando elige cambiar las letras
	def cambioL(self, letras, jugadaJ, window):
		for i in range(len(jugadaJ)):
			letras.append(jugadaJ[i])
			jugadaJ[i] = 0
		for indice in range(7):
			letra=random.choice(letras)
			jugadaJ[indice]= letra
			letras.remove(letra)
			window.FindElement("Letra" + str(indice)).Update(letra)
		
		self.set_atril(jugadaJ)
		return self._atril
  
