import validar_palabra_lexicon as ppattern
import random

lista_atril = []



def list_to_dict(lista_atril):
    hand_as_dict = {}
    for letra in lista_atril:
        hand_as_dict[letra] = hand_as_dict.get(letra, 0) + 1
    return hand_as_dict

#validas = ['NN', 'NNS', 'VB', 'JJ']

#def clasificar(palabra):
   # pal = parse(palabra).split()
    #print para control
    #print(pal)
  #  if pal[0][0][1] in validas:
  #      devuelve =  True
  #  else:
   #     devuelve = False
  #  return devuelve
	
	
#def analizar_palabra_pat(palabra):
	#pal = palabra.lower()
	#if not pal in verbs:
		#if pal in lexicon:
			#if pal in spelling:
			#print('Esta en spelling y lexicon')
				#return clasificar(pal)
		#else:
			#print('No está ni en verbs ni en lexicon')
			#return False
	#else:
		#print('La encontró en verbs')
		#return clasificar(pal)
	
#lista_atril es una lista con las letras
def build_words(lista_atril):
    atril = list_to_dict(lista_atril)
    todas_las_palabras = [""]
    i = 0
    ew = ""
    while len(ew) < len(lista_atril):
        ew = todas_las_palabras[i]
        tempEW = []
        for w in range(len(ew)):
            tempEW.append(ew[w])
        temp_hand_dict = dict(atril)
        j = 0
        while j < len(lista_atril):
            if lista_atril[j] not in tempEW:
                nueva_palabra = ew + (lista_atril[j])
                todas_las_palabras.append(nueva_palabra)
                j = j + temp_hand_dict[lista_atril[j]]
            else:
                tempEW.remove(lista_atril[j])
                num = temp_hand_dict[lista_atril[j]] - 1
                temp_hand_dict[lista_atril[j]] = num
                j = j + 1
        i = i + 1
    return todas_las_palabras
    
def lista_a_diccionario(todas_las_palabras,validez):
	''' Devuelve un diccionario cuya clave es el tamaño de la palabra y el valor es una palabra válida'''
	set_palabras = {}
	for palabra in todas_las_palabras:
		validez = ppattern.analizar_palabra_pat(palabra,validez)
		if validez==True:
			tamanio = len(palabra)
			if tamanio in set_palabras:
				set_palabras[tamanio].append(palabra)
			else:
				set_palabras[tamanio] = [palabra]
	return set_palabras


def palabra_compu(longitud, set_palabras):	
	palabra_encontrada = ''
	if longitud in set_palabras:
		#elegida = random.randint(0, len(set_palabras[longitud])-1)
		#palabra_encontrada = set_palabras[longitud][elegida]
		palabra_encontrada = set_palabras[longitud][0]	
	else:
		longitud = longitud - 1
		encontre=False
		while longitud>1 and encontre==False:
			if longitud in set_palabras:
				#elegida = random.randint(0, len(set_palabras[longitud])-1)
				#palabra_encontrada = set_palabras[longitud][elegida]
				palabra_encontrada = set_palabras[longitud][0]
				encontre=True
			else:
				longitud = longitud - 1
	return palabra_encontrada

#porque elige al az	ar si va a jugar la palabra en forma horizontal o vertical
direccion_palabra = {0:'horizontal', 1:'vertical'}

#guarda las keys de las casillas vacías en el tablero
desocupadas = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10),(0,11),(0,12),(0,13),(0,14), (1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(1,11),(1,12),(1,13),(1,14),
(2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(2,10),(2,11),(2,12),(2,13),(2,14),(3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(3,9),(3,10),(3,11),(3,12),(3,13),(3,14),
(4,0),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7),(4,8),(4,9),(4,10),(4,11),(4,12),(4,13),(4,14),(5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(5,10),(5,11),(5,12),(5,13),(5,14),
(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(6,8),(6,9),(6,10),(6,11),(6,12),(6,13),(6,14),(7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7),(7,8),(7,9),(7,10),(7,11),(7,12),(7,13),(7,14),
(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8),(8,9),(8,10),(8,11),(8,12),(8,13),(8,14),(9,0),(9,1),(9,2),(9,3),(9,4),(9,5),(9,6),(9,7),(9,8),(9,9),(9,10),(9,11),(9,12),(9,13),(9,14),
(10,0),(10,1),(10,2),(10,3),(10,4),(10,5),(10,6),(10,7),(10,8),(10,9),(10,10),(10,11),(10,12),(10,13),(10,14),(11,0),(11,1),(11,2),(11,3),(11,4),(11,5),(11,6),(11,7),(11,8),(11,9),(11,10),(11,11),(11,12),(11,13),(11,14),
(12,0),(12,1),(12,2),(12,3),(12,4),(12,5),(12,6),(12,7),(12,8),(12,9),(12,10),(12,11),(12,12),(12,13),(12,14),(13,0),(13,1),(13,2),(13,3),(13,4),(13,5),(13,6),(13,7),(13,8),(13,9),(13,10),(13,11),(13,12),(13,13),(13,14),
(14,0),(14,1),(14,2),(14,3),(14,4),(14,5),(14,6),(14,7),(14,8),(14,9),(14,10),(14,11),(14,12),(14,13),(14,14)]

def eliminar_coord_en_pc(listaCoordenadas):
	
	print('listacoord ', listaCoordenadas)
	for coord in listaCoordenadas:
		desocupadas.remove(coord)
	print('desocupadas ',desocupadas)
	return desocupadas


def programaPrincipal(turno_computadora,atrilC,validez,window):
	print(turno_computadora)
	print(atrilC)
	
	while turno_computadora == True:
		#va a buscar una posicion en el tablero al azar
		if (7,7) in desocupadas:
			x=7
			y=7
		else:
			x=random.randint(0,14)
			y=random.randint(0,14)
		print('x= ', x, 'y=', y)  #control
		#va a elegir horizontal o vertical al azar (1:horiz
		hv = random.randint(0,1)
		print(direccion_palabra[hv])  #control
		coord_x, coord_y = x, y  #guardo los valores x e y de la key del casillero inicial
		#dependiendo de lo que haya salido va a contar los casilleron libres desde la posicion elegida
		espacios_libres = 0
		#creo diccionario con las palabras validas
		dicc = lista_a_diccionario(build_words(atrilC),validez)
		print(dicc) #control
		if direccion_palabra[hv]=='horizontal':
			print('entre a horizontal')  #control
			while (x,y) in desocupadas and x<=14 and espacios_libres<7:
				espacios_libres = espacios_libres + 1
				x = x + 1
			print('ESPACIOS LIBRES: ', espacios_libres)   #control
			if espacios_libres > 1:
				#busco una palabra que tenga una longitud igual o menor
				#print('entre!!')
				#print(pal(espacios_libres, dicc))
				palabra_encontrada = palabra_compu(espacios_libres, dicc)
				print(palabra_encontrada) #control
				#la pasa al tablero
				for letra in palabra_encontrada:
					window[(coord_x, coord_y)].Update(letra)
					window.FindElement((coord_x,coord_y)).Update(disabled = True)
					#elimino del atril
					#window[datos_atril[letra]].Update('')
					#elimino de la lista
					atrilC.remove(letra)
					coord_x = coord_x + 1
				turno_computadora = False
				return turno_computadora 
					##-------------------------------------------------#
		else:
			print('entre a vertical')  #control
			while (x,y) in desocupadas and y<=14 and espacios_libres<7:
				espacios_libres = espacios_libres + 1
				y = y + 1
			print('ESPACIOS LIBRES: ', espacios_libres)   #control
			if espacios_libres > 1:
				#print('entreee')
				#print(pal(espacios_libres, dicc))  #control
				#busco una palabra que tenga una longitud igual o menor	
				palabra_encontrada = palabra_compu(espacios_libres, dicc)
				print(palabra_encontrada)
				#la pasa al tablero
				for letra in palabra_encontrada:
					window[(coord_x, coord_y)].Update(letra)
					print('voy a deshabilitar')
					window.FindElement((coord_x,coord_y)).Update(disabled = True)
					#elimino del atril
					#window[datos_atril[letra]].Update('')
					#elimino de la lista
					atrilC.remove(letra)
					coord_y = coord_y + 1
				turno_computadora = False
				return turno_computadora
