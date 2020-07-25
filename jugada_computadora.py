import validar_palabra_lexicon as ppattern
import random
import itertools as it

lista_atril = []

#lista_atril es una lista con las letras
def build_words(lista_atril):
	"""Esta función crea todas las combinaciones posibles con las letras que la computadora
	tiene en su atril"""
	word = "".join(lista_atril)
	#control
	#print(word)
	combinaciones = set()
	for i in range(2, len(word)+1):
		combinaciones.update((map("".join, it.permutations(word, i))))
	todas_las_palabras = list(combinaciones)
	#control
	#print(todas_las_palabras)
	return todas_las_palabras
	
    
def lista_a_diccionario(todas_las_palabras,validez):
	""" Esta función devuelve un diccionario cuya clave es el tamaño 
	de la palabra y el valor es una palabra válida"""
	dic_palabras = {}
	for palabra in todas_las_palabras:
		validez = ppattern.analizar_palabra_pat(palabra,validez)
		if validez==True:
			tamanio = len(palabra)
			if tamanio in dic_palabras:
				dic_palabras[tamanio].append(palabra)
			else:
				dic_palabras[tamanio] = [palabra]
	return dic_palabras

#para el nivel facil y medio
def busca_palabra_al_azar(lista_de_keys, dic_palabras):
	#si el diccionario está vacío trae problemas!
	if len(lista_de_keys) != 0:
		try:
			tam_elegido = random.randint(0, len(lista_de_keys)-1)
			pos_palabra_elegida = random.randint(0, len(dic_palabras[lista_de_keys[tam_elegido]])-1)
			palabra_encontrada = dic_palabras[lista_de_keys[tam_elegido]][pos_palabra_elegida]
			dic_palabras[lista_de_keys[tam_elegido]].remove(palabra_encontrada)
		except:
			palabra_encontrada = ""
			pass
	return palabra_encontrada

def lista_de_fichas(palabra_encontrada, atrilC):
	"""Esta función devuelve una lista con las fichas que la computadora va a poner en el tablero, en el orden correcto"""
	palabra_en_lista = []
	for i in palabra_encontrada:
		palabra_en_lista.append(i)
	letras_jugadas = []
	pos = 0
	while pos<len(palabra_en_lista):
		if palabra_en_lista[pos]=="RR":
			if pos+1<len(palabra_encontrada) and palabra_encontrada[pos+1]=="R" and "RR" in atrilC:
				letras_jugadas.append("RR")
				pos = pos + 1 
			else:
				letras_jugadas.append("R")
		elif palabra_en_lista[pos]=="L":
			if pos+1<len(palabra_encontrada) and palabra_encontrada[pos+1]=="L" and "LL" in atrilC:
				letras_jugadas.append("LL")
				pos = pos + 1
			else:
				letras_jugadas.append("L")
		else:
			letras_jugadas.append(palabra_en_lista[pos])
		pos = pos + 1
	print("Fichas: ", letras_jugadas)
	return letras_jugadas
	
def palabra_compu_F(longitud, dic_palabras, atrilC):	
	"""Esta función elige la palabra que la computadora va a poner en el tablero en el nivel F"""
	palabra_encontrada = ""
	lista_de_keys = []
	for i in dic_palabras:
		lista_de_keys.append(i)
	if len(lista_de_keys) != 0:
		palabra_encontrada = busca_palabra_al_azar(lista_de_keys, dic_palabras)
		#check es una lista con las fichas que va a usar
		check = lista_de_fichas(palabra_encontrada,  atrilC)
		cant = len(check)
		sin_loop = 0
		while sin_loop<50 and ("R" in palabra_encontrada.upper() and "R" not in atrilC) or ("L" in palabra_encontrada.upper() and "L" not in atrilC) or cant>longitud:
			print(1, cant)
			palabra_encontrada = busca_palabra_al_azar(lista_de_keys, dic_palabras)
			check = lista_de_fichas(palabra_encontrada, atrilC)
			cant = len(check)
			sin_loop = sin_loop + 1
	return palabra_encontrada
	
	

#def palabra_compu_M(longitud, dic_palabras, atrilC):	
#	"""Esta función elige la palabra que la computadora va a poner en el tablero en el nivel M"""
#	palabra_encontrada = ''
#	pass
	
#def palabra_compu_D(longitud, dic_palabras, atrilC):	
#	"""Esta función elige la palabra que la computadora va a poner en el tablero en el nivel D"""
#	palabra_encontrada = ''
#	pass


#porque elige al azar si va a jugar la palabra en forma horizontal o vertical
direccion_palabra = {0:'horizontal', 1:'vertical'}

desocupadas = []

def cargar_tuplas_desocupadas(desocupadas):
	"""Esta funcion inicializa la lista 'desocupadas', que almacena las tuplas correspondientes a las keys de los casilleros del tablero que están desocupados."""
	for i in range(15):
		for j in range(15):
			desocupadas.append((i,j))
	#print(desocupadas)

def eliminar_coord_en_pc(listaCoordenadas):
	"""Esta función elimina de la lista 'desocupadas' las tuplas correspondientes a lask keys de los casilleros que se van ocupando en el tablero."""
	#print('listacoord ', listaCoordenadas)
	for coord in listaCoordenadas:
		desocupadas.remove(coord)
	#print('desocupadas ',desocupadas)
	return desocupadas	
	
def rellenar_atrilC(window,atrilC,letras):
	"""Esta función completa las siete letras en el atril de la cumputadora luego de que ésta juega su turno."""
	for indice in range(len(atrilC)):
		if atrilC[indice] == 0:
			letra=random.choice(letras)
			atrilC[indice] = letra
			#window.FindElement("LetraC" + str(indice)).Update(letra)
			letras.remove(letra)
	print("relleno atrilC",atrilC)
	return 
	

def programaPrincipal(turno_computadora,validez,window,puntos,jugadorC,letras,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada):
	"""Esta función es la que se lleva a cabo cuando es el turno de la computadora. Primero elige posición en el tablero al azar (excepto si es el primer turno), luego elige al azar si va a jugar horizonal o verticalmente, cuanta los espacios vacíos, y elige una palabra de tamaño adecuado para jugar."""
	atrilC=jugadorC.get_atril()
#	triplica = False
	#print(turno_computadora)
	#print(atrilC)
	while turno_computadora == True:
		#va a buscar una posicion en el tablero al azar
		if (7,7) in desocupadas:
			x=7
			y=7
		else:
			x=random.randint(0,14)
			y=random.randint(0,14)
		#print('x= ', x, 'y=', y)  #control
		#va a elegir horizontal o vertical al azar (1:horiz
		hv = random.randint(0,1)
#		print(direccion_palabra[hv])  #control
		coord_x, coord_y = x, y  #guardo los valores x e y de la key del casillero inicial
		#dependiendo de lo que haya salido va a contar los casilleron libres desde la posicion elegida
		espacios_libres = 0
		#creo diccionario con las palabras validas
		dicc = lista_a_diccionario(build_words(atrilC),validez)
		#print(dicc) #control
		if direccion_palabra[hv]=='horizontal':
#			print('entre a horizontal')  #control
			while (x,y) in desocupadas and x<=14 and espacios_libres<7:
				espacios_libres = espacios_libres + 1
				x = x + 1
			print('ESPACIOS LIBRES: ', espacios_libres)   #control
			if espacios_libres > 1:
				#busco una palabra que tenga una longitud igual o menor
				print('entre!!')
				#print(pal(espacios_libres, dicc))
				palabra_encontrada = palabra_compu_F(espacios_libres, dicc, atrilC)
	#--------------------------------------------------------------
				letras_jugadas = lista_de_fichas(palabra_encontrada, atrilC)
#				print(letras_jugadas)
				print(atrilC)
	#--------------------------------------------------------------		
				print(palabra_encontrada) #control
				#la pasa al tablero
				ptos=jugadorC.get_puntaje()
				puntaje = 0
				triplica = False
				duplica = False
	#--------------------------------------------------------------
#				letras_jugadas = lista_de_fichas(palabra_encontrada, atrilC)
#				print(letras_jugadas)
#				print(atrilC)
	#--------------------------------------------------------------			
#				for letra in palabra_encontrada:
				for letra in letras_jugadas:
					window[(coord_x, coord_y)].Update(letra)
					window[(coord_x,coord_y)].Update(disabled = True)
					#elimino del atril
					#window[datos_atril[letra]].Update('')
					#elimino de la lista
					pos=atrilC.index(letra)
					#print("pos",pos)
					#print("letra",letra)
					atrilC[pos]=0
					
					p=puntos.get(letra)	
					print("letra",letra,"puntos",p)
#					if (coord_x, coord_y) in casillas_naranja:
#						p=p*2
#						print("letra",letra,"x",coord_x,"y",coord_y,"duplica")
					if (coord_x, coord_y) in casillas_azules: 
						p=p*3						
						print("letra",letra,"x",coord_x,"y",coord_y,"triplica")
					if jugada.get_nivel() == "F" and (coord_x, coord_y) in casillas_celeste: 
						p=p*2
						print("letra",letra,"x",coord_x,"y",coord_y,"triplica")
					if jugada.get_nivel() == "D" and (coord_x, coord_y) in casillas_descuento:
						p=(-1)*p
						print("letra",letra,"x",coord_x,"y",coord_y,"descuenta")
					if (coord_x, coord_y) in casillas_rojas:
						triplica = True
					if (coord_x, coord_y) in casillas_naranja:
						duplica = True
					puntaje=puntaje+p
					
					print((coord_x,coord_y))
					desocupadas.remove((coord_x, coord_y))
					coord_x = coord_x + 1
					
				if triplica:
					puntaje = puntaje*3
				if duplica:
					puntaje = puntaje*2
					
				ptos = ptos + puntaje
				if palabra_encontrada != "":
					window["info"].Update("La palabra jugó la palabra {} y sumó {} puntos.".format(palabra_encontrada, puntaje))
				else:
					window["info"].Update("La computadora pasó su turno")
				jugadorC.set_puntaje(ptos)
					#ptos=ptos+puntos.get(letra)
					
					#coord_x = coord_x + 1
				#jugadorC.set_puntaje(ptos)
				#rellenar_atrilC(window,atrilC,letras)
				#jugadorC.set_atril(atrilC)
				#print("atrilC",atrilC)
				#turno_computadora = False
				#jugadorC.set_dejarJugar()
				#return turno_computadora 
					##-------------------------------------------------#
		else:
#			print('entre a vertical')  #control
			while (x,y) in desocupadas and y<=14 and espacios_libres<7:
				espacios_libres = espacios_libres + 1
				y = y + 1
			print('ESPACIOS LIBRES: ', espacios_libres)   #control
			if espacios_libres > 1:
				print('entreee')
				#print(pal(espacios_libres, dicc))  #control
				#busco una palabra que tenga una longitud igual o menor	
				palabra_encontrada = palabra_compu_F(espacios_libres, dicc, atrilC)
				print(palabra_encontrada)
		#--------------------------------------------------------------
				letras_jugadas = lista_de_fichas(palabra_encontrada, atrilC)
#				print(letras_jugadas)
				print(atrilC)
#--------------------------------------------------------------	
				#la pasa al tablero
				ptos=jugadorC.get_puntaje()
				puntaje = 0
				triplica = False
				duplica = False
		#--------------------------------------------------------------
#				letras_jugadas = lista_de_fichas(palabra_encontrada, atrilC)
#				print(letras_jugadas)
#				print(atrilC)
#--------------------------------------------------------------			
	#			for letra in palabra_encontrada:
				for letra in letras_jugadas:
					window[(coord_x, coord_y)].Update(letra)
					
					#print('voy a deshabilitar')
					window[(coord_x,coord_y)].Update(disabled = True)
					#elimino del atril
					#window[datos_atril[letra]].Update('')
					#elimino de la lista
					pos=atrilC.index(letra)
					#print("pos",pos)
					#print("letra",letra)
                     
					atrilC[pos]=0
					p=puntos.get(letra)	
					print("letra",letra,"puntos",p)
#					if (coord_x, coord_y) in casillas_naranja:
#						p=p*2
#						print("letra",letra,"x",coord_x,"y",coord_y,"duplica")
					if (coord_x, coord_y) in casillas_azules: 
						p=p*3						
						print("letra",letra,"x",coord_x,"y",coord_y,"triplica")
					if jugada.get_nivel() == "F" and (coord_x, coord_y) in casillas_celeste: 
						p=p*2
						print("letra",letra,"x",coord_x,"y",coord_y,"triplica")
					if jugada.get_nivel() == "D" and (coord_x, coord_y) in casillas_descuento:
						p=(-1)*p
						print("letra",letra,"x",coord_x,"y",coord_y,"descuenta")
					if (coord_x, coord_y) in casillas_rojas:
						triplica = True
					if (coord_x, coord_y) in casillas_naranja:
						duplica = True
					puntaje=puntaje+p
					
					print((coord_x,coord_y))
					desocupadas.remove((coord_x, coord_y))
					coord_y = coord_y + 1
					
				if triplica:
					puntaje = puntaje*3
				if duplica:
					puntaje = puntaje*2
				
				ptos = ptos + puntaje
				if palabra_encontrada != "":
					window["info"].Update("La palabra jugó la palabra {} y sumó {} puntos.".format(palabra_encontrada, puntaje))
				else:
					window["info"].Update("La computadora pasó su turno")	
				jugadorC.set_puntaje(ptos)
					#atrilC.remove(letra)
					#ptos=ptos+puntos.get(letra)
					
					#coord_y = coord_y + 1

#		jugadorC.set_puntaje(ptos)
		turno_computadora = False
		rellenar_atrilC(window,atrilC,letras)
		print("atrilC",atrilC) 
		window["tot_letras"].Update(len(letras))
		jugadorC.set_atril(atrilC)
		jugadorC.set_dejarJugar()
		return turno_computadora
