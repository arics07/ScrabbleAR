import validar_palabra_lexicon as ppattern
import random
import itertools as it
import fin_del_juego as pantalla_final 

lista_atril = []

#lista_atril es una lista con las letras
def combinaciones(lista_atril):
	"""Esta función crea todas las combinaciones posiblegss con las letras que la computadora
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
#direccion_palabra = {0:'horizontal', 1:'vertical'}



def cargar_tuplas_desocupadas(desocupadas):
	"""Esta funcion inicializa la lista 'desocupadas', que almacena las tuplas correspondientes a las keys de los casilleros del tablero que están desocupados."""
	for i in range(15):
		for j in range(15):
			desocupadas.append((i,j))
	#print(desocupadas)

def eliminar_coord_en_pc(listaCoordenadas,desocupadas):
	"""Esta función elimina de la lista 'desocupadas' las tuplas correspondientes a lask keys de los casilleros que se van ocupando en el tablero."""
	print('listacoord ', listaCoordenadas)
	for coord in listaCoordenadas:
		desocupadas.remove(coord)
	print('desocupadas ',desocupadas)
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

def busca_pos(desocupadas):
	if (7,7) in desocupadas:
		x=7
		y=7
	else:
		x=random.randint(0,14)
		y=random.randint(0,14)
	return x,y

def cuenta_espacios_libres(x,y,direccion,desocupadas):
	espacios_libres = 0
	while (x,y) in desocupadas and x<=14 and espacios_libres<7:
		espacios_libres = espacios_libres + 1
		if direccion=="horizontal":
			x = x + 1
		else:
			y = y + 1
	return espacios_libres
	
def analizo_casillero(x,y,desocupadas):
	direccion = {0: "horizontal", 1:"vertical"}
	dir_azar = random.randint(0,1)
	dir1 = direccion[dir_azar]
	esp1 = cuenta_espacios_libres(x,y, dir1,desocupadas)
	if dir1 =="horizontal":
		dir2 = "vertical"
	else:
		dir2 = "horizontal"
	esp2 = cuenta_espacios_libres(x,y, dir2,desocupadas)
	if esp1<esp2:
		return esp2,dir2
	else:
		return esp1, dir1

def calcular_puntos_letras(p, coord, nivel,duplica,triplica,casillas_azules,casillas_rojas,casillas_naranja,*args):
	#p=puntos.get(letra)	
	#print("letra",letra,"puntos",p)
	print("args",args)
	if coord in casillas_azules: 
		p=p*3
		#print("letra",letra,"x",coord_x,"y",coord_y,"triplica")
	if nivel == "F" and coord in args[0]: 
		p=p*2
		#print("letra",letra,"x",coord_x,"y",coord_y,"triplica")
	if nivel == "D" and coord in args[0]:
		p=(-1)*p
		#print("letra",letra,"x",coord_x,"y",coord_y,"descuenta")
	if coord in casillas_rojas:
		triplica = True
	if coord in casillas_naranja:
		duplica = True
	return p,duplica,triplica
		

def programa_principal(turno_computadora,validez,window,puntos,jugadorC,letras,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada):
	"""Esta función es la que se lleva a cabo cuando es el turno de la computadora. Primero elige posición en el tablero al azar (excepto si es el primer turno), luego elige al azar si va a jugar horizonal o verticalmente, cuanta los espacios vacíos, y elige una palabra de tamaño adecuado para jugar."""
	atrilC=jugadorC.get_atril()
	matriz=jugada.get_matriz()
	desocupadas = jugada.get_desocupadas()
	#print(desocupadas)
#	window["turno"].Update("COMPUTADORA")
	if turno_computadora == True:		
		#compu_pensando(jugada.get_nivel(), window)
		
		#creo diccionario con las palabras validas
		dicc = lista_a_diccionario(combinaciones(atrilC),validez)  ######******######******######******#######****
		
		#si el diccionario está vacío, no puede formar ninguna palabra --> termina la partida
		if len(dicc) == 0:
			#------------------------------------------------------------------------------------
			window.close()
			#----------SE TERMINÓ LA PARTIDA porque no puede formar ninguna palabra--------------
			pantalla_final.programa_principal(jugada.get_jugadorJ(), jugada.get_jugadorC(),jugada.get_puntos())
			#------------------------------------------------------------------------------------
		
		#veo cuál es el tamaño de la palabra más corta que puede formar para sabar el mímino de espacios que necesita
		tam_pal_mas_corta = list(dicc.keys())[0]
	
		#busca una posicion en el tablero al azar
		x,y = busca_pos(desocupadas)
		#print('x= ', x, 'y=', y)  #control

		#guardo los valores x e y de la key del casillero inicial
		coord_x, coord_y = x, y  

######-------------------------------------------------------------------------------------------
		#veo si puedo poner una palabra en ese casillero
		espacios_libres, direc = analizo_casillero(x,y,desocupadas)
		
		#si no tiene espacio, entra en el if y empieza a buscar otro lugar (intenta 20 veces)
		if espacios_libres < tam_pal_mas_corta:
			#print("estoy en espacion libre menor a tam pal mas corta")
			intentos = 20
			#creo una copia de desocupadas para evitar que en los 20 intentos vuelva a elegir el mismo casillero
			des = desocupadas.copy()
			print("soy des ",des)
			des.remove((coord_x,coord_y))
			while espacios_libres <tam_pal_mas_corta and intentos>0:
				x,y = busca_pos(des)
				coord_x, coord_y = x,y
				espacios_libres, direc = analizo_casillero(x,y)
				des.remove(coord_x,coord_y)
				intentos = intentos - 1
			#si intentó 20 veces y no encontró lugar, se termina la partida
			if intentos == 0:
				window.close()
				#SE TERMINÓ LA PARTIDA porque no encontró lugar en el tablero
				pantalla_final.programa_principal(jugada.get_jugadorJ(), jugada.get_jugadorC(),jugada.get_puntos())
		
		#si enocntró lugar, busca una palabra en su diccionario
		#pack_palabra_encontrada tiene una tupla (string, [lista de fichas])
		pack_palabra_encontrada = palabra_compu_FM(espacios_libres, dicc, atrilC)
		#palabra_encontrada tiene la lista con las fichas	
		palabra_encontrada = pack_palabra_encontrada[1]
		#print(palabra_encontrada) #control
		ptos=jugadorC.get_puntaje()
		
		#reseteo puntaje, triplica y duplica
		puntaje = 0
		triplica = False
		duplica = False

		#calcula el puntaje la palabra	
		for letra in palabra_encontrada:
			window[(coord_x, coord_y)].Update(letra)
			window[(coord_x,coord_y)].Update(disabled = True)
			window.FindElement((coord_x,coord_y)).Update(button_color=("white","black"))
			matriz[coord_x][coord_y] = letra
				
			pos=atrilC.index(letra)
				
			atrilC[pos]=0
					
			if jugada.get_nivel() == "F":
				p,duplica,triplica=calcular_puntos_letras(puntos.get(letra),(coord_x,coord_y),jugada.get_nivel(),duplica,triplica,casillas_azules,casillas_rojas,casillas_naranja,casillas_celeste)
			if jugada.get_nivel() == "M":
				p,duplica,triplica=calcular_puntos_letras(puntos.get(letra),(coord_x,coord_y),jugada.get_nivel(),duplica,triplica,casillas_azules,casillas_rojas,casillas_naranja)
			if jugada.get_nivel() == "D":	
				p,duplica,triplica=calcular_puntos_letras(puntos.get(letra),(coord_x,coord_y),jugada.get_nivel(),duplica,triplica,casillas_azules,casillas_rojas,casillas_naranja,casillas_descuento)
					
			puntaje=puntaje+p
					
			#print((coord_x,coord_y))
			desocupadas.remove((coord_x, coord_y))
			jugada.set_desocupadas(desocupadas)
			
			#print(" desocupadas en jugada pc ", desocupadas)
			
			if direc == "horizontal":
				coord_x = coord_x + 1
			else:
				coord_y = coord_y + 1
					
		if triplica:
			puntaje = puntaje*3
		if duplica:
			puntaje = puntaje*2
					
		ptos = ptos + puntaje
		
		#window["puntosPC"].Update(ptos)
		#informa 
		if pack_palabra_encontrada[0] != "":
			window["info"].Update("La computadora jugó la palabra {} y sumó {} puntos.".format(pack_palabra_encontrada[0], puntaje))
			
		jugadorC.set_puntaje(ptos)
#		else:
#			window["info"].Update("La computadora pasó su turno")

					
					
	#se actualizan los datos y se termina el turno de la computadora
	turno_computadora = False
	rellenar_atrilC(window,atrilC,letras)
	#print("atrilC",atrilC) 
	window["tot_letras"].Update(len(letras))
	jugadorC.set_atril(atrilC)
	jugadorC.set_dejarJugar()
#	window["turno"].Update("")
	return turno_computadora
