import validar_palabra_lexicon as ppattern
import random
import itertools as it
#from time import sleep 

lista_atril = []

#lista_atril es una lista con las letras
def combinaciones(lista_atril):
	"""Esta función crea todas las combinaciones posibles con las letras que la computadora
	tiene en su atril"""
	listas_de_fichas = []
	for n in range(2,len(lista_atril)+1):
		a= it.permutations(lista_atril, n)
		listas_de_fichas.extend(a)
	print("control combinaciones ", len(listas_de_fichas))
	return listas_de_fichas	
	    
def lista_a_diccionario(listas_de_fichas,validez):
	""" Esta función devuelve un diccionario cuya clave es el tamaño 
	de la palabra y el valor es una tupla que almacena la palabra en la pos=0 
	y la lista con las fichas correspondientes en la pos=1"""
	dic_palabras = {}
	#comb es una lista con las fichas
	for comb in listas_de_fichas:
		if len(comb)>1 : 
			word = "".join(comb)
			validez = ppattern.analizar_palabra_pat(word, validez)
#			print("control analiza todas ", word,validez)
			if validez == True:
				tamanio = len(word)
				if tamanio in dic_palabras:
					dic_palabras[tamanio].append((word, comb))
				else:
					dic_palabras[tamanio] = [(word, comb)]
	print("diccionario ", dic_palabras)
	return dic_palabras	
	
def palabra_compu_FM(longitud, dic_palabras, atrilC):	
	"""Esta función elige la palabra que la computadora va a poner en el tablero en el nivel F. Devuelve una
	tupla que contiene la palabra elegida en la pos=0 y la lista con las fichas correspondientes en la pos=1"""
	palabra_encontrada = ("",[])
	if longitud in dic_palabras:
		palabra_encontrada = dic_palabras[longitud][-1]
	else:
		while longitud not in dic_palabras and longitud>1:
			longitud = longitud - 1
		if longitud>1 :
			palabra_encontrada = dic_palabras[longitud][-1]		
	#devuelve una tupla (palabra, [lista de fichas]
	return palabra_encontrada


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
	
#def compu_pensando(nivel, window):
#	window["info"].Update("La computadora está pensando...")
#	if nivel=="F":
#		tiempo = random.randint(7,9)
#	elif nivel=="M":
#		tiempo = random.randint(5,7)
#	else:
#		tiempo = random.randint(1,3)
#	sleep(tiempo)

def calcular_puntos_letras(p, coord, nivel,duplica,triplica,casillas_azules,casillas_rojas,casillas_naranja,*args):
	#p=puntos.get(letra)	
	#print("letra",letra,"puntos",p)
	if coord in casillas_azules: 
		p=p*3
		#print("letra",letra,"x",coord_x,"y",coord_y,"triplica")
	if nivel == "F" and coord in args: 
		p=p*2
		#print("letra",letra,"x",coord_x,"y",coord_y,"triplica")
	if nivel == "D" and coord in args:
		p=(-1)*p
		#print("letra",letra,"x",coord_x,"y",coord_y,"descuenta")
	if coord in casillas_rojas:
		triplica = True
	if coord in casillas_naranja:
		duplica = True
	return p,duplica,triplica
	
		

def programaPrincipal(turno_computadora,validez,window,puntos,jugadorC,letras,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada):
	"""Esta función es la que se lleva a cabo cuando es el turno de la computadora. Primero elige posición en el tablero al azar (excepto si es el primer turno), luego elige al azar si va a jugar horizonal o verticalmente, cuanta los espacios vacíos, y elige una palabra de tamaño adecuado para jugar."""
	atrilC=jugadorC.get_atril()
	matriz=jugada.get_matriz()
#	triplica = False
	#print(turno_computadora)
	#print(atrilC)
#	window["turno"].Update("COMPUTADORA")
	if turno_computadora == True:		
		#compu_pensando(jugada.get_nivel(), window)
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
		dicc = lista_a_diccionario(combinaciones(atrilC),validez)  ######******######******######******#######*****
		#print(dicc) #control
		if direccion_palabra[hv]=='horizontal':
#			print('entre a horizontal')  #control
			while (x,y) in desocupadas and x<=14 and espacios_libres<7:
				espacios_libres = espacios_libres + 1
				x = x + 1
			print('ESPACIOS LIBRES: ', espacios_libres)   #control
			if espacios_libres <= 1:
				window["info"].Update("La computadora pasó su turno")
			elif espacios_libres > 1:
				#busco una palabra que tenga una longitud igual o menor
				print('entre!!')
				#print(pal(espacios_libres, dicc))
#				pack_palabra = palabra_compu_F(espacios_libres, dicc, atrilC)
				#palabra encontrada es una tupla (palabra, [fichas])
				pack_palabra_encontrada = palabra_compu_FM(espacios_libres, dicc, atrilC)
#				print("PACKKKKKKKKKKKKK ", pack_palabra_encontrada)
				palabra_encontrada = pack_palabra_encontrada[1]

				print(palabra_encontrada) #control
				#la pasa al tablero
				ptos=jugadorC.get_puntaje()
				puntaje = 0
				triplica = False
				duplica = False
				
#				for letra in palabra_encontrada:
				for letra in palabra_encontrada:
					window[(coord_x, coord_y)].Update(letra)
					window[(coord_x,coord_y)].Update(disabled = True)
					matriz[coord_x][coord_y] = letra
					#elimino del atril
					#window[datos_atril[letra]].Update('')
					#elimino de la lista
					pos=atrilC.index(letra)
					#print("pos",pos)
					#print("letra",letra)
					atrilC[pos]=0
					
					if jugada.get_nivel() == "F":
						p,duplica,triplica=calcular_puntos_letras(puntos.get(letra),(coord_x,coord_y),jugada.get_nivel(),duplica,triplica,casillas_azules,casillas_rojas,casillas_naranja,casillas_celeste)
					if jugada.get_nivel() == "M":
						p,duplica,triplica=calcular_puntos_letras(puntos.get(letra),(coord_x,coord_y),jugada.get_nivel(),duplica,triplica,casillas_azules,casillas_rojas,casillas_naranja)
					if jugada.get_nivel() == "D":	
						p,duplica,triplica=calcular_puntos_letras(puntos.get(letra),(coord_x,coord_y),jugada.get_nivel(),duplica,triplica,casillas_azules,casillas_rojas,casillas_naranja,casillas_descuento)
					
					puntaje=puntaje+p
					
					print((coord_x,coord_y))
					desocupadas.remove((coord_x, coord_y))
					coord_x = coord_x + 1
					
				if triplica:
					puntaje = puntaje*3
				if duplica:
					puntaje = puntaje*2
					
				ptos = ptos + puntaje
				if pack_palabra_encontrada[0] != "":
					window["info"].Update("La computadora jugó la palabra {} y sumó {} puntos.".format(pack_palabra_encontrada[0], puntaje))
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
			if espacios_libres <= 1:
				window["info"].Update("La computadora pasó su turno")
			elif espacios_libres > 1:
				print('entreee')
				#print(pal(espacios_libres, dicc))  #control
				#busco una palabra que tenga una longitud igual o menor	
				pack_palabra_encontrada = palabra_compu_FM(espacios_libres, dicc, atrilC)
				print("PACKKKKKKKKKKKKK ", pack_palabra_encontrada)
				palabra_encontrada = pack_palabra_encontrada[1]
				print(palabra_encontrada)

				print(atrilC)

				#la pasa al tablero
				ptos=jugadorC.get_puntaje()
				puntaje = 0
				triplica = False
				duplica = False
		
	#			for letra in palabra_encontrada:
				for letra in palabra_encontrada:
					window[(coord_x, coord_y)].Update(letra)
					matriz[coord_x][coord_y] = letra
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
				if pack_palabra_encontrada[0] != "":
					window["info"].Update("La computadora jugó la palabra {} y sumó {} puntos.".format(pack_palabra_encontrada[0], puntaje))
				else:
					window["info"].Update("La computadora pasó su turno")	
				jugadorC.set_puntaje(ptos)
					#atrilC.remove(letra)
					#ptos=ptos+puntos.get(letra)
					
					#coord_y = coord_y + 1

		turno_computadora = False
		rellenar_atrilC(window,atrilC,letras)
		print("atrilC",atrilC) 
		window["tot_letras"].Update(len(letras))
		jugadorC.set_atril(atrilC)
		jugadorC.set_dejarJugar()
#		window["turno"].Update("")
		return turno_computadora
