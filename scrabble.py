import PySimpleGUI as sg
import validar_palabra_lexicon as ppattern
import jugada_computadora as jugadaPC
import random
import pickle
import fin_del_juego as pantalla_final
from datetime import date
import ventana_ayuda

 
def verTopTen(topt):
	"""Esta función retorna la informacion de topTen para visualizar cuando se clickea el botón."""
	lista=[]
	for key,value in topt.items():
		lista.append((key,value["puntaje"],value["fecha"]))
	orden=[]
	norden=1
	for i in lista:
		orden.append("{:^2}{:^30}{:^20}{:^20}".format(str(norden),i[0],str(i[1]),str(i[2])))
		norden = norden + 1
	return orden

def muestro_matriz(matriz,window):
	"""Esta función completa el tablero con la información de la partida que fue pospuesta."""
	print(matriz)
	for x in range(15):
		for y in range(15):
			if not matriz[x][y] == 0:
				window.FindElement((x,y)).Update(matriz[x][y],disabled = True)

def muestro_l(window,atril): 
	"""Esta función visualiza la letra sobre el boton del atril del jugador."""
	for indice in range(len(atril)):
		letra = atril[indice] 
		window.FindElement("Letra" + str(indice)).Update(letra)

def muestro_lc(window,atril): 
	"""Esta función visualiza un * sobre el atril de la computadora."""
	for indice in range(len(atril)):
		letra = atril[indice] 
		window.FindElement("LetraC" + str(indice)).Update("*")
   
	
def accion_atril (window,atrilJ,pos,textBoton,datosEleccion):
	"""Esta función devuelve la letra seleccionada del atril y pone en 0 la posición que ocupaba dicha letra en el mismo."""
	datosEleccion[pos] = atrilJ[pos]
	letraElegida = atrilJ[pos]  
	window.FindElement(textBoton).Update("")
	atrilJ[pos] = 0
	return letraElegida
	
def accion_tablero(window,event,listaCoordenadas,letraElegida,matriz):
	"""Esta función guarda, en la matriz de datos, el valor de la letra colocada en cada casillero.Retorna la lista de coordenadas de las casillas que se ocuparon para formar la palabra."""
	posicionCasilleroTablero = event  
	
	listaCoordenadas.append(posicionCasilleroTablero)
	
	x=posicionCasilleroTablero[0]
	y=posicionCasilleroTablero[1]
	
	window[posicionCasilleroTablero].update(letraElegida)
	matriz[x][y] = letraElegida
	window.FindElement((x,y)).Update(disabled = True)
	window.FindElement((x,y)).Update(button_color=("white","black"))
	return listaCoordenadas
	
	
	
def armar_palabra(listaCoordenadas,matriz):
	"""Esta función ordena la lista de coordenadas para poder unir cada letra ubicada en el tablero de manera correcta. Retorna la palabra."""
	unionLetras = []
	listaCoordenadas.sort()
	for lcoord in listaCoordenadas:
		x= lcoord[0]
		y= lcoord[1]
		unionLetras.append(matriz[x][y])
	pal=(''.join(unionLetras)).lower()
	return pal
	
def rellenar_atril(window,atrilJ,letras):
	"""Esta función rellena los espacios vacios del atril después de haber colocado una palabra en el tablero y corroborar que es válida.Retorna el atril modificado"""
	for indice in range(len(atrilJ)):
		if atrilJ[indice] == 0:
			letra=random.choice(letras)
			atrilJ[indice] = letra
			window.FindElement("Letra" + str(indice)).Update(letra)
			letras.remove(letra)
	return atrilJ
	
def devolver_letras_atril(window,listaCoordenadas,matriz,atrilJ,datosEleccion,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada):
	"""Esta función devuelve las letras al atril si la palabra no es válida o, si es primer jugada y no coloco la palabra en el centro. Limpia el tablero y renueva el string de los casilleros especiales la palabra pasó por uno de ellos.Retorna la lista de coordenadas vacía """
	for lcoord in listaCoordenadas:
		x=lcoord[0]
		y=lcoord[1]
		
		letra = matriz[x][y]
		window.FindElement(lcoord).Update("")
		window.FindElement((x,y)).Update(button_color=("white","tan"))
		
		if (x,y) == (7,7):
			window.FindElement(lcoord).Update(button_color=("black", "gray"))
		if (x,y) in casillas_naranja:
			window.FindElement(lcoord).Update("DP", button_color=("black", "#F4963E"))
		if (x,y) in casillas_azules:
			window.FindElement(lcoord).Update("TL", button_color=("black", "#1A4C86"))
		if (x,y) in casillas_rojas:
			window.FindElement(lcoord).Update("TP", button_color=("black", "#C91A4F"))
		if jugada.get_nivel() == "D" and (x,y) in casillas_descuento:
			window.FindElement(lcoord).Update("x", button_color=("black", "#F00F0F"))
		if jugada.get_nivel() == "F" and (x,y) in casillas_celeste:
			window.FindElement(lcoord).Update("DL", button_color=("black", "#4893E9"))
			
		matriz[x][y] = 0
		window.FindElement((x,y)).Update(disabled = False)
		
	for pos,val in datosEleccion.items() :
		atrilJ[pos] = val
		window.FindElement("Letra" + str(pos)).Update(val)
		window.FindElement("Letra" + str(pos)).Update(disabled = False)
	
	listaCoordenadas = []
		
	#for indice in range(len(atrilJ)):
		#if atrilJ[indice]== 0:
			#valor = random.choice(guardoLetrasTemporal)
			#atrilJ[indice]= valor
			#guardoLetrasTemporal.remove(valor)
			#window.FindElement("Letra" + str(indice)).Update(valor)
	#unionLetras = []
	#listaCoordenadas = []
	#print(listaCoordenadas)
	return listaCoordenadas

def tablero_medio(window, casillas_azules, casillas_rojas, casillas_naranja):
	"""Esta función inicializa el tablero del nivel medio (M)"""
	window[(7, 7)].update(button_color=("black", "gray"))
	for cas in casillas_azules:
		window[cas].update("TL", button_color=("black", "#1A4C86"))
	for cas in casillas_rojas:
		window[cas].update("TP", button_color=("black", "#C91A4F"))
	for cas in casillas_naranja:
		window[cas].update("DP", button_color=("black", "#F4963E"))

        
def tablero_facil(window, casillas_azules, casillas_rojas, casillas_naranja, casillas_celeste):
	"""Esta función inicializa el tablero del nivel fácil (F)"""
	tablero_medio(window, casillas_azules, casillas_rojas, casillas_naranja)
	for cas in casillas_celeste:
		window[cas].update("DL", button_color=("black", "#4893E9"))
        
def tablero_dificil(window, casillas_azules, casillas_rojas, casillas_naranja, casillas_descuento):
	"""Esta función inicializa el tablero del nivel difícil (D)"""
	tablero_medio(window, casillas_azules, casillas_rojas, casillas_naranja)
	for cas in casillas_descuento:
		window[cas].update("x", button_color=("black", "#F00F0F"))
	
def no_es_horizontal_o_vertical(window,event,atrilJ,datosEleccion,letraElegida,listaCoordenadas,casillas_naranja,casillas_azules,casillas_rojas,casillas_descuento,casillas_celeste,jugada):
	"""Esta función devuelve la letra al atril si cambia de direccion (horizontal/vertical) mientras arma la palabra"""
	posKeys = len(datosEleccion)
	pos = list(datosEleccion.keys())[posKeys-1]
	window.FindElement(event).Update("")
	
	window.FindElement(event).Update(button_color=("black","tan"))
	
	if (x,y) == (7,7):
		window.FindElement(lcoord).Update(button_color=("black", "gray"))
	if event in casillas_naranja:
		window.FindElement(event).Update("DP", button_color=("black", "#F4963E"))
	if event in casillas_azules:
		window.FindElement(event).Update("TL", button_color=("black", "#1A4C86"))
	if event in casillas_rojas:
		window.FindElement(event).Update("TP", button_color=("black", "#C91A4F"))
	if jugada.get_nivel() == "D" and event in casillas_descuento:
		window.FindElement(event).Update("x", button_color=("black", "#F00F0F"))
	if jugada.get_nivel() == "F" and event in casillas_celeste:
		window.FindElement(event).Update("DL", button_color=("black", "#4893E9"))
	
	listaCoordenadas.remove(event)
	atrilJ[pos]= letraElegida
	window.FindElement("Letra" + str(pos)).Update(letraElegida)
	window.FindElement("Letra" + str(pos)).Update(disabled = False)
	datosEleccion.pop(pos)
	print(datosEleccion, letraElegida)
	return datosEleccion

#def inicializar_casillas_azules():
#	"""Esta función devuelve una lista que contiene las tuplas correspondientes a las key de los botones del tablero que se verán de color azul"""
#	casillas = []
#	num = [1,5,9,13]
#	for i in num:
#		for j in num:
#			if not ((i==1 and j ==1) or (i==13 and j==13)):
#				casillas.append((i,j))
#	return casillas
	
#def inicializar_casillas_rojas():
#	"""Esta función devuelve una lista que contiene las tuplas correspondientes a las key de los botones del tablero que se verán de color rojo"""
#	casillas = []
#	num = [0,7,14]
#	for i in num:
#		for j in num:
#			if not (i==7 and j==7):
#				casillas.append((i,j))
#	return casillas

#def inicializar_casillas_celeste():
#	"""Esta función devuelve una lista que contiene las tuplas correspondientes a las key de los botones del tablero que se verán de color celeste"""
#	casillas = []
#	num_1 = [2,6,8,12]
#	num_2 = [4,10]
#	for n in num_1:
#		for m in num_2:
#			casillas.append((m,n))
#			casillas.append((n,m))
#	num_3 = [1,13]
#	for n in num_3:
#		casillas.append((7,n))
#		casillas.append((n,7))
#	return casillas
	
	
#def inicializar_casillas_naranja():
#	"""Esta función devuelve una lista que contiene las tuplas correspondientes a las key de los botones del tablero que se verán de color celeste"""
#	casillas = []
#	num = [1,2,3,4,6,8,10,11,12,13]
#	n=-1
#	for i in num:
#		 casillas.append((i,i))
#		 casillas.append((i,num[n]))
#		 n = n-1			 
#	return casillas
	
#def inicializar_casillas_descuento():
#	"""Esta función devuelve una lista que contiene las tuplas correspondientes a las key de los botones del tablero que se verán de color rojo y descontarán puntos"""
#	casillas = []
#	num_1 = [2,6,8,12]
#	num_2 = [4,10]
#	for i in num_1:
#		for n in num_2:
#			casillas.append((i,n))
#			casillas.append((n,i))
#	num_3 = [1,3,11,13]
#	for i in num_3:
#		casillas.append((i,7))
#		casillas.append((7,i))			
#	return casillas

def compu_pensando(duracion_compu_pensando,contadorPC,tiempoPensandoPC,turno_computadora,esPrimerJugada,window,jugadorC,validez,puntos,letras,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada,jugadorJ):
	"""Esta función ejecuta el módulo de a computadora una vez terminado el tiempo para pensar. Retorna los valores reiniciados de tiempoPensandoPC, contadorPC y esPrimerJugada."""
	if contadorPC == (duracion_compu_pensando *100):
		tiempoPensandoPC = False
		contadorPC = 0
		turno_computadora = jugadaPC.programa_principal(turno_computadora,validez,window,puntos,jugadorC,letras,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada)
		esPrimerJugada=False
		window["puntosPc"].update(jugadorC.get_puntaje())
		window["turno"].update((jugadorJ.get_nombre()).upper())
		jugadorJ.set_jugar()
		esPrimerJugada=False
	return (tiempoPensandoPC, contadorPC,esPrimerJugada)

def main(args,tipoj):  
	jugada=args
	
	puntos=jugada.get_puntos()
	letras = jugada.get_letras()
	#jugada.get_nivel()
	#jugada.set_fecha(date.today())
	#turno = jugada.get_turno()
	
	sg.theme("GreenTan")

	max_col = max_rows = 15
	
#	casillas_azules = inicializar_casillas_azules()
#	casillas_rojas = inicializar_casillas_rojas()
#	casillas_celeste = inicializar_casillas_celeste()
#	casillas_naranja = inicializar_casillas_naranja()
#	casillas_descuento = inicializar_casillas_descuento()
	
#	casillas_azules = [(1,5), (1,9), (5,1), (5,5), (5,9),(5,13), (9,1), (9,5), (9,9), (9,13), (13,5), (13,9)]
#	casillas_rojas = [(0,0), (0,7), (0,14), (7,0),(7,14), (14,0), (14,7), (14,14)]
#	casillas_celeste = [(0,3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8,12), (11,0), (11,7), (11,14), (12,6), (12,8), (14,3), (14,11)]
#	casillas_naranja = [(1,1), (2,2), (3,3), (4,4), (6,6), (8,8), (10,10), (11,11), (12,12), (13,13), (13,1), (12,2), (11,3), (10,4), (8,6), (6,8), (4,10), (3,11), (2,12), (1,13)]
#	casillas_descuento = [(2,4), (2,10), (4,6), (10,6), (10,8), (12,4), (12,10), (7,1), (7,13), (1,7), (13,7), (4,2), (10,2), (4,12), (10,12), (6,4), (8,4), (6,10), (8,10), (4,8), (0,2), (2,0), (3,7), (7,3), (11,7), (7,11), (0,12), (12,0), (14,12), (12,14), (2,14)]

	try:
		with open('confi.pkl', 'rb') as f:
			confi=dict(pickle.load(f))
			f.close()
	except:
		sg.Popup("No se encontró el archivo confi.pkl")
		
	casillas_azules = confi["casilleros_especiales"]["casillas_azules"]
	casillas_rojas = confi["casilleros_especiales"]["casillas_rojas"]
	casillas_naranja = confi["casilleros_especiales"]["casillas_naranja"]
	casillas_celeste = confi["casilleros_especiales"]["casillas_celeste"]
	casillas_descuento = confi["casilleros_especiales"]["casillas_descuento"]

	letrasEnTablero = [] 
	
	columna_tablero = [[sg.Button("", size=(2, 1),disabled = False,enable_events=True, key=(i, j), pad=(0, 0), disabled_button_color = ( "white" , "black" ), 
		button_color=("white", "tan")) for i in range(max_col)] for j in range(max_rows)]
	
	columna_5 = [
	            [sg.Text("Puntos Compu")],
	            [sg.Text(size=(10, 1), key="puntosPc", background_color="white")]
	            ]
	
	columna_4 = [
	            [sg.Text("Puntos Jugador", size=(12,1))],
	            [sg.Text(size=(10, 1), key="puntosJug", background_color="white")]
	            ]
	
	columna_3 = [
	            [sg.Text("              Tiempo", justification="center")],
	            [sg.Text("", size=(1,1)),sg.Text(size=(10, 1), font=('Helvetica', 15), justification='center', key='tiempo')]
	            ]
	
	columna_2 = [
	            [sg.Text("", size=(1,1)),sg.Column(columna_3)],
	            [sg.Column(columna_4),sg.Column(columna_5)],
	            [sg.Text("", size=(1,1))],
	            [sg.Text("TURNO"),sg.Text(size=(18, 1), key="turno",background_color="#FFFFFF")],
	            [sg.Text("Nivel:   "),sg.Text(size=(3,1), key="nivel",background_color="#FFFFFF")],
				[sg.Text("Letras restantes:"), sg.Text(len(letras), size=(7,1), key="tot_letras",background_color="#FFFFFF")],
				[sg.Text("", size=(1,1))],
				[sg.Text("Información de la computadora:")],
				[sg.Text("", size=(26,5), background_color="#EFE5C4", key="info")],
				[sg.Text("Información del jugador:")],
				[sg.Text("", size=(26,5), background_color="#DCFBCB", key="infoJ")],
				[sg.Text(" ", size=(1, 1))],
				[sg.Button("Posponer", size=(10,1), disabled=False, key="posponer",disabled_button_color =( "white" , "tan" )),sg.Text("", size=(1,1)),sg.Button("Ver TopTen",disabled=False,disabled_button_color =( "white" , "tan" ), size=(10,1))],
				[sg.Text(" ", size=(1, 1))],
				[sg.Button("Finalizar", button_color=("white", "red"), size=(10,1),disabled=False,disabled_button_color =("white", "red"), key="finalizo"), sg.Button("Ayuda", size=(10,1))],
				]
		
	columna_1 = [
                [sg.Text("", size=(3,1)),sg.Text("Computadora")],
                [sg.Text("", size=(3,1)),sg.Text(" ", size=(3, 1)), sg.Button("", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="LetraC0"), sg.Button("", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="LetraC1"), sg.Button("", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="LetraC2"), sg.Button(
                 "", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="LetraC3"), sg.Button("", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="LetraC4"), sg.Button("", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="LetraC5"), sg.Button("", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="LetraC6")],
	            [sg.Text("", size=(3,1)),sg.Column(columna_tablero),sg.Text("", size=(3,1))],
	            [sg.Text("", size=(3,1)),sg.Text("Jugador: ", size=(6,1)),sg.Text(size=(15, 1), key="nombre",background_color="#FFFFFF")],
	            [sg.Text("", size=(3,1)),sg.Text(" ", size=(3, 1)), sg.Button("", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="Letra0"), sg.Button("", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="Letra1"), sg.Button("", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="Letra2"), sg.Button("", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="Letra3"), sg.Button("", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="Letra4"), sg.Button("", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="Letra5"), sg.Button("", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="Letra6"),sg.Text(" ", size=(1, 1)), sg.Button("Cambio\nletras", size=(6, 2), disabled=False,disabled_button_color =( "white" , "tan" ), key="cambio")],
	            [sg.Text("", size=(1,1))],
	            [sg.Text("", size=(8,1)),sg.Button('Insertar Palabra', size=(12, 1),disabled=False,disabled_button_color =( "white" , "tan" ), key="insertar"),sg.Text(" ", size=(1, 1)), sg.Button('Pasar', size=(9, 1),disabled=False,disabled_button_color =( "white" , "tan" ), key="pasar")],
	            [sg.Text("", size=(1,1))]
	            ]
				   
	layout = [
        [sg.Column(columna_1),sg.Column(columna_2) ]
		]

	window = sg.Window("::::::::: SCRABBLE AR :::::::::", layout)
	window.Finalize()

	tiempoCorriendo = False
	#contador = 0
	tiempoEleccionPalabra = False
	contadorEleccionPalabra =0
	tiempoPensandoPC = False
	contadorPC = 0
	
	contador = jugada.get_contador()
	jugadorJ=jugada.get_jugadorJ()
	jugadorC=jugada.get_jugadorC()
	duracion_jugada=jugada.get_tiempo()
	duracion_elecc_palabra = jugada.get_tiempoEleccionP()
	duracion_compu_pensando = jugada.get_tiempoPensandoPC()
	matriz=jugada.get_matriz()
	primerTurno = jugada.get_primerTurno()
	desocupadas = jugada.get_desocupadas()
	
	listaCoordenadas = []
	#matriz=[]
	
	datosEleccion = {}
	datosEleccionC = {}
	esValida = False
	esHorizontal = False
	esVertical = False
#	primerTurno = jugada.get_primerTurno()
#	triplica = False
#	niv = jugada.get_nivel()
	
	#unionLetras = []
	atrilJ = jugadorJ._atril
	atrilC = jugadorC._atril
 
	window["nivel"].update(jugada.get_nivel())	
	window["nombre"].update((jugadorJ.get_nombre()).upper())
	window["puntosJug"].update(jugadorJ.get_puntaje())
	window["puntosPc"].update(jugadorC.get_puntaje())
	
	# colores
	if jugada.get_nivel() == "F" or jugada.get_nivel() == "f":
		tablero_facil(window, casillas_azules, casillas_rojas, casillas_naranja, casillas_celeste)
	elif jugada.get_nivel() == "M" or jugada.get_nivel() == "m":
		tablero_medio(window, casillas_azules, casillas_rojas, casillas_naranja)
	else:
		tablero_dificil(window, casillas_azules, casillas_rojas, casillas_naranja, casillas_descuento)
		
#	colores_tablero(window, casillas_azules,casillas_rojas, casillas_naranja, casillas_celeste)
  
	if tipoj == "C":
		for i in range (15):
			matriz.append([0]*15) 
		esPrimerJugada = True
	else:
		muestro_matriz(matriz,window)
		esPrimerJugada = False
		
	muestro_l(window,jugadorJ.get_atril())
	muestro_lc(window,jugadorC.get_atril())
	#jugadorJ.set_turno = True
	jugadorJ.set_jugar()
	tiempoCorriendo = True 
	#esPrimerJugada = True
	validez = False
	nombreGanador = ''
	
	while tiempoCorriendo == True:
		event, values = window.Read(timeout=10)
		
		if event == None:
			break
		#print("primer jugada ", esPrimerJugada)
			
		tiempoEleccionPalabra = True
		
		if jugadorC.get_turno() == False:
			window["turno"].update((jugadorJ.get_nombre()).upper())
			for i in range(len(atrilC)):
				window.FindElement("LetraC" + str(i)).Update(disabled = True)
			
			window["finalizo"].update(disabled = False)
			window["cambio"].update(disabled = False)
			window["posponer"].update(disabled = False)
			window["pasar"].update(disabled = False)
			window["insertar"].update(disabled = False)
			
		elif jugadorC.get_turno():
			window["finalizo"].update(disabled = True)
			window["cambio"].update(disabled = True)
			window["posponer"].update(disabled = True)
			window["pasar"].update(disabled = True)
			window["insertar"].update(disabled = True)
		
		if jugadorJ.get_turno():
			for i in range(len(atrilJ)):
				window.FindElement("Letra" + str(i)).Update(disabled = False)
		elif jugadorJ.get_turno() == False:
			for i in range(len(atrilJ)):
				window.FindElement("Letra" + str(i)).Update(disabled = True)
			
			
				
		if contadorEleccionPalabra == duracion_elecc_palabra: 
			tiempoEleccionPalabra = False
			contadorEleccionPalabra = 0
			window["turno"].update("COMPUTADORA")
			jugadorJ.set_dejarJugar()
			#print(jugadorJ.get_turno())
			jugadorC.set_jugar()
			turno_computadora = jugadorC.get_turno()
			tiempoPensandoPC = True
			#turno_computadora = jugadaPC.programaPrincipal(turno_computadora,validez,window,puntos,jugadorC,letras,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada)
			#print('turno despues de que volvi de jugada pc ', turno_computadora)
			#window["puntosPc"].update(jugadorC.get_puntaje())
			#window["turno"].update(jugadorJ.get_nombre())
			#jugadorJ.set_jugar()
			
		if primerTurno=="computadora" and esPrimerJugada==True:
			#for i in range(len(atrilJ)):
				#window.FindElement("Letra" + str(i)).Update(disabled = True)
			window["turno"].update("COMPUTADORA")
			jugadorC.set_jugar()
			#print(jugadorC.get_turno())
			turno_computadora = jugadorC.get_turno()
			tiempoPensandoPC = True
			#turno_computadora = jugadaPC.programaPrincipal(turno_computadora,validez,window,puntos,jugadorC,letras,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada)
			#window["puntosPc"].update(jugadorC.get_puntaje())
			#esPrimerJugada=False
  
		if event == 'Letra0':
			letraElegida = accion_atril(window,atrilJ,0,event,datosEleccion)
			for i in range(len(atrilJ)):
				if i != 0:
					window.FindElement("Letra" + str(i)).Update(disabled = True)
  
		if event == 'Letra1':
			letraElegida = accion_atril(window,atrilJ,1,event,datosEleccion)
			for i in range(len(atrilJ)):
				if i != 1:
					window.FindElement("Letra" + str(i)).Update(disabled = True)
  
		if event == 'Letra2':
			letraElegida = accion_atril(window,atrilJ,2,event,datosEleccion)
			for i in range(len(atrilJ)):
				if i != 2:
					window.FindElement("Letra" + str(i)).Update(disabled = True)
	  
		if event == 'Letra3':
			letraElegida = accion_atril(window,atrilJ,3,event,datosEleccion)
			for i in range(len(atrilJ)):
				if i != 3:
					window.FindElement("Letra" + str(i)).Update(disabled = True)
	  
		if event == 'Letra4':
			letraElegida = accion_atril(window,atrilJ,4,event,datosEleccion)
			for i in range(len(atrilJ)):
				if i != 4:
					window.FindElement("Letra" + str(i)).Update(disabled = True)
	  
		if event == 'Letra5':
			letraElegida = accion_atril(window,atrilJ,5,event,datosEleccion)
			for i in range(len(atrilJ)):
				if i != 5:
					window.FindElement("Letra" + str(i)).Update(disabled = True)
	  
		if event == 'Letra6':
			letraElegida = accion_atril(window,atrilJ,6,event,datosEleccion)
			for i in range(len(atrilJ)):
				if i != 6:
					window.FindElement("Letra" + str(i)).Update(disabled = True)
	  
		if type(event) is tuple:
			
			for i in range(len(atrilJ)):
				window.FindElement("Letra" + str(i)).Update(disabled = False)
				if atrilJ[i] == 0:
					window.FindElement("Letra" + str(i)).Update(disabled = True)
			
			if len(listaCoordenadas) == 0:
				try:
					listaCoordenadas = accion_tablero(window,event,listaCoordenadas,letraElegida,matriz)
					coordx = listaCoordenadas[0][0]
					coordy = listaCoordenadas[0][1]
				except:
					pass
					
			elif len(listaCoordenadas) == 1:
				
				if event[0] == coordx:
					esHorizontal = False
					esVertical = True
				else:
					esVertical = False
					esHorizontal = True
				
				listaCoordenadas = accion_tablero(window,event,listaCoordenadas,letraElegida,matriz)

			elif len(listaCoordenadas) > 1:
				
				if esHorizontal:
					listaCoordenadas = accion_tablero(window,event,listaCoordenadas,letraElegida,matriz)
					if event[1] != coordy:
						sg.Popup('debes seguir horizontal!')
						datosEleccion= no_es_horizontal_o_vertical(window,event,atrilJ,datosEleccion,letraElegida,listaCoordenadas,casillas_naranja,casillas_azules,casillas_rojas,casillas_descuento,casillas_celeste,jugada)
				
				if esVertical:
					listaCoordenadas = accion_tablero(window,event,listaCoordenadas,letraElegida,matriz)
					if event[0] != coordx:
						sg.Popup('debes seguir vertical!')
						datosEleccion= no_es_horizontal_o_vertical(window,event,atrilJ,datosEleccion,letraElegida,listaCoordenadas,casillas_naranja,casillas_azules,casillas_rojas,casillas_descuento,casillas_celeste,jugada)
			
		if event == 'insertar':
			print(esPrimerJugada)
			if esPrimerJugada:
				if (7,7) in listaCoordenadas:
					esHorizontal = False
					esVertical = False
					palabra = armar_palabra(listaCoordenadas,matriz)
					#print('palabra ',palabra)
					#print('voy a analizar la palabra')
					esValida = ppattern.analizar_palabra_pat(palabra, esValida)
					palabra = palabra.upper()
					#print('volvi de analizar la palabra',palabra)
					#print('palabra analizada es: ', esValida)
					if esValida:
						rellenar_atril(window,atrilJ,letras)
						desocupadas = jugadaPC.eliminar_coord_en_pc(listaCoordenadas,desocupadas)
						jugada.set_desocupadas(desocupadas)

						#ptos=int(values["puntosJug"])
						ptos = jugadorJ.get_puntaje()
						puntaje = 0
						duplica = False
						triplica = False
						for lcoord in listaCoordenadas:
							x=lcoord[0]
							y=lcoord[1]
							letra = matriz[x][y]	
							p=puntos.get(letra)	
							#print("letra",letra,"puntos",p)
#							if (x,y) in casillas_naranja:
#								p=p*2
#								print("letra",letra,"x",x,"y",y,"duplica")  
							if (x,y) in casillas_azules: 
								p=p*3						
								print("letra",letra,"x",x,"y",y,"triplica")
							if jugada.get_nivel() == "F" and (x,y) in casillas_celeste: 
								p=p*2
								print("letra",letra,"x",x,"y",y,"triplica")
							if jugada.get_nivel() == "D" and (x,y) in casillas_descuento:
								p=(-1)*p
								print("letra",letra,"x",x,"y",y,"descuenta")
							if (x,y) in casillas_rojas:
								triplica = True
							if (x,y) in casillas_naranja:
								duplica = True
								
							puntaje=puntaje+p	
							
						if triplica:
							puntaje=puntaje*3	
						if duplica:
							puntaje=puntaje*2
								    
						ptos = ptos + puntaje	
						listaCoordenadas = []
						window["tot_letras"].Update(len(letras))

						#for j in palabra:
						#	ptos=ptos+puntos.get(j)
									
						window["puntosJug"].update(ptos)
						window["infoJ"].Update("{} jugó la palabra {} y sumó {} puntos.".format((jugadorJ.get_nombre()).upper(),palabra, puntaje))
						
						jugadorJ.set_puntaje(ptos)
						jugadorJ.set_dejarJugar()
						esPrimerJugada = False
						window["turno"].update("COMPUTADORA")
						jugadorC.set_jugar()
						#print(jugadorC.get_turno())
						turno_computadora = jugadorC.get_turno()
						tiempoPensandoPC = True
						#turno_computadora = jugadaPC.programaPrincipal(turno_computadora,validez,window,puntos,jugadorC,letras,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada)
						#window["puntosPc"].update(jugadorC.get_puntaje())
						#print('turno despues de que volvi de jugada pc ', turno_computadora)
						#jugadorJ.set_jugar()
					else:
						listaCoordenadas = devolver_letras_atril(window,listaCoordenadas,matriz,atrilJ,datosEleccion,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada)
						datosEleccion = {}
						#print('lista coord ', listaCoordenadas)
						#print('datos eleccion ', datosEleccion)
						#print(atrilJ)
						esPrimerJugada =True
						
						window["infoJ"].Update("La palabra {} no es válida, intente de nuevo.".format(palabra))
						
						#--sg.Popup('La palabra no es válida, turno de la computadora')
						#--jugadorJ.set_dejarJugar()
						#print(jugadorJ.get_turno())
						##--jugadorC.set_jugar()
						##--window["turno"].update("COMPUTADORA")
						##--turno_computadora = jugadorC.get_turno()
						##--tiempoPensandoPC = True
						#turno_computadora = jugadaPC.programaPrincipal(turno_computadora,validez,window,puntos,jugadorC,letras,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada)
						#window["puntosPc"].update(jugadorC.get_puntaje())
						#print('turno despues de que volvi de jugada pc ', turno_computadora)
						#window["turno"].update(jugadorJ.get_nombre())
						#jugadorJ.set_jugar()
				else:
					sg.Popup('La palabra debe pasar por el botón del centro!')
					#print('estoy en el else de no esta en el centro')
					#print('datos eleccion ', datosEleccion)
					listaCoordenadas = devolver_letras_atril(window,listaCoordenadas,matriz,atrilJ,datosEleccion,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada)
					datosEleccion = {}
					#print('lista coord ', listaCoordenadas)
					#print('datos eleccion ', datosEleccion)
					#print("atrilJ",atrilJ)
					esPrimerJugada =True
			else:
				esHorizontal = False
				esVertical = False
				palabra = armar_palabra(listaCoordenadas,matriz)
				#print('palabra ',palabra)
				#print('voy a analizar la palabra')
				esValida = ppattern.analizar_palabra_pat(palabra, esValida)
				palabra = palabra.upper()
				#print('volvi de analizar la palabra',palabra)
				#print('palabra analizada es: ', esValida)
				if esValida:
					
					try:
						rellenar_atril(window,atrilJ,letras)
					except:
						sg.Popup("No hay más letras en la bolsa.Finalizó la partida")
						window.close()
						pantalla_final.programa_principal(jugadorJ,jugadorC,jugada.get_puntos())
						
					desocupadas = jugadaPC.eliminar_coord_en_pc(listaCoordenadas,desocupadas)
					jugada.set_desocupadas(desocupadas)
					
					#print(listaCoordenadas)
					
					#ptos=int(values["puntosJug"])
					ptos = jugadorJ.get_puntaje()	
					puntaje = 0	
					triplica = False
					duplica = False
					for lcoord in listaCoordenadas:
						x=lcoord[0]
						y=lcoord[1]
						letra = matriz[x][y]	
						p=puntos.get(letra)						
						
#						print("letra",letra,"puntos",p)
#						if (x,y) in casillas_naranja:
#								p=p*2
#							print("letra",letra,"x",x,"y",y,"duplica")  
						
						if (x,y) in casillas_azules: 
							p=p*3						
							print("letra",letra,"x",x,"y",y,"triplica")
						if jugada.get_nivel() == "F" and (x,y) in casillas_celeste: 
							p=p*2
							print("letra",letra,"x",x,"y",y,"triplica")
						if jugada.get_nivel() == "D" and (x,y) in casillas_descuento:
							p=(-1)*p
							print("letra",letra,"x",x,"y",y,"descuenta")
						
						if (x,y) in casillas_rojas:
								triplica = True
						if (x,y) in casillas_naranja:
								duplica = True
						puntaje=puntaje+p	
					
					if triplica:
							puntaje=puntaje*3
					if duplica:
						    puntaje=puntaje*2
					
					ptos = ptos + puntaje		
					listaCoordenadas = []	
					window["tot_letras"].Update(len(letras))				    
						
					window["puntosJug"].update(ptos)
					window["infoJ"].Update("{} jugó la palabra {} y sumó {} puntos.".format((jugadorJ.get_nombre()).upper(),palabra, puntaje))
					
					jugadorJ.set_puntaje(ptos)
					jugadorJ.set_dejarJugar()
					window["turno"].update('COMPUTADORA')
					jugadorJ.get_nombre()
					jugadorJ.set_dejarJugar()
					#print(jugadorJ.get_turno())
					jugadorC.set_jugar()
					turno_computadora = jugadorC.get_turno()
					tiempoPensandoPC = True
					#turno_computadora = jugadaPC.programaPrincipal(turno_computadora,validez,window,puntos,jugadorC,letras,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada)
					#window["puntosPc"].update(jugadorC.get_puntaje())
					#print('turno despues de que volvi de jugada pc ', turno_computadora)
					#window["turno"].update(jugadorJ.get_nombre())
					#jugadorJ.set_jugar()
				else:
					listaCoordenadas = devolver_letras_atril(window,listaCoordenadas,matriz,atrilJ,datosEleccion,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada)
					datosEleccion = {}
					#print('lista coord ', listaCoordenadas)
					#print('datos eleccion ', datosEleccion)
					print(atrilJ)
					
					window["infoJ"].Update("La palabra {} no es válida, intente de nuevo.".format(palabra))
					
					##--sg.Popup('La palabra no es válida, turno de la computadora')
					##--jugadorJ.set_dejarJugar()
					#print(jugadorJ.get_turno())
					##--jugadorC.set_jugar()
					##--window["turno"].update("COMPUTADORA")
			
					##--turno_computadora = jugadorC.get_turno()
					##--tiempoPensandoPC = True
					#turno_computadora = jugadaPC.programaPrincipal(turno_computadora,validez,window,puntos,jugadorC,letras,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada)
					#window["puntosPc"].update(jugadorC.get_puntaje())
					#print('turno despues de que volvi de jugada pc ', turno_computadora)
					#window["turno"].update(jugadorJ.get_nombre())
					#jugadorJ.set_jugar()
			print(esPrimerJugada)
			
		if event == 'pasar':
			jugadorJ.set_dejarJugar()
			#print(jugadorJ.get_turno())
			#abiri modulo compu
			window["infoJ"].Update("Pasaste el turno.")
			jugadorC.set_jugar()
			turno_computadora = jugadorC.get_turno()
			#print('turno pc ', turno_computadora)
			window["turno"].update(jugadorC.get_nombre())
			tiempoPensandoPC = True
			#turno_computadora = jugadaPC.programaPrincipal(turno_computadora,validez,window,puntos,jugadorC,letras,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada)
			#print("esprimer",esPrimerJugada)
			#print("puntaje",jugadorC.get_puntaje())
			#esPrimerJugada=False
			#print("esprimer",esPrimerJugada)	
			#window["puntosPc"].update(jugadorC.get_puntaje())
			#print('turno despues de que volvi de jugada pc ', turno_computadora)
			#window["turno"].update(jugadorJ.get_nombre())
			#jugadorJ.set_jugar()
											
		if event == "finalizo" or contador == duracion_jugada:
			window.close()
			tiempoCorriendo = False
			
			topten=jugada.get_topten()
			
			try:
				ntopten=topten[jugada.get_nivel()]
			except:
				ntopten={}
			
			njugada={'puntaje': jugadorJ.get_puntaje(), 'fecha': jugada.get_fecha()}
			ntopten.setdefault(jugadorJ.get_nombre(),njugada)
			ntopten.items()
			ntopten=dict(sorted(ntopten.items(), key=lambda uno:uno[1]['puntaje'],reverse=True)[:10])
			topten[jugada.get_nivel()]=ntopten

			with open('topten.pkl', 'wb') as f:
				pickle.dump(topten, f, pickle.HIGHEST_PROTOCOL)
				f.close()
				
			pantalla_final.programa_principal(jugadorJ,jugadorC,jugada.get_puntos())
	    
		if event == "Ver TopTen":
			topten=jugada.get_topten()
			try:
				topten=topten[jugada.get_nivel()]
			except:
				topten={}
			layout2=[[sg.Text('ORDEN'),sg.Text('JUGADOR'),sg.Text('PUNTAJE'),sg.Text('FECHA')],
			[sg.Listbox(values=verTopTen(topten),key='topten',size=(50,10))],
			[sg.Button("Cerrar",size=(10,2))]]
			window2 = sg.Window('TOP TEN').Layout(layout2)
			window2.finalize()
			while True: 
				event2, values2=window2.Read() 
				if event2 == None or event2 == "Cerrar":
					break 
			window2.close()
			
		if event ==  "posponer":
			tiempoCorriendo = False
	
			jugada.set_desocupadas(desocupadas)
			jugada.set_matriz(matriz)
			jugada.set_contador(contador)
			
			try:
				with open('scrabble.pkl', 'wb') as output:
					pickle.dump(jugada, output, pickle.HIGHEST_PROTOCOL)
					output.close()
				sg.Popup("Se guardó correctamente la partida")
				break
			except:
				sg.Popup("No se guardó correctamente la partida")
		
		if event == "Ayuda":
			ventana_ayuda.ayuda_al_jugador()
				
		if tiempoCorriendo: 
			window["tiempo"].update("{:02d}:{:02d}:{:02d}".format((contador // 1000) // 360,(contador // 100) // 60, (contador // 100) % 60))
			contador += 1
			
		if tiempoEleccionPalabra: 
			contadorEleccionPalabra += 1
		
		if tiempoPensandoPC:
			window["info"].Update("La computadora está pensando...")
			#letraElegida = ''
			contadorPC +=1
			tiempoPensandoPC,contadorPC,esPrimerJugada = compu_pensando(duracion_compu_pensando,contadorPC,tiempoPensandoPC,turno_computadora,esPrimerJugada,window,jugadorC,validez,puntos,letras,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada,jugadorJ)
	  
		if event == "cambio":
			if jugadorJ.verificoatrilcompleto(jugadorJ.get_atril()):
				if jugada.get_cantCambios()<3:
					jugadorJ.cambioL(letras,jugadorJ.get_atril(),window)
					#print(jugadorJ.get_atril())
					jugada.sumarCambio()
					window["infoJ"].Update("Cambiaste las letras de tu atril. Es turno de la computadora.")
					
				else:
					sg.Popup("ya hizo los 3 cambios permitidos")
					window["cambio"].update(disabled = True)
					
				jugadorJ.set_dejarJugar()	
				#print(jugadorJ.get_turno())	
					
				window["turno"].update("COMPUTADORA")
				#jugadorJ.set_dejarJugar()
				#print(jugadorJ.get_turno())
				jugadorC.set_jugar()
				turno_computadora = jugadorC.get_turno()
				tiempoPensandoPC = True
				
				#turno_computadora = jugadaPC.programaPrincipal(turno_computadora,validez,window,puntos,jugadorC,letras,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada)
				#print('turno despues de que volvi de jugada pc ', turno_computadora)
				#window["turno"].update(jugadorJ.get_nombre())
				#jugadorJ.set_jugar()					 
			else:
				sg.Popup("el atril no esta completo")	
				
#		if primerTurno=="computadora" and esPrimerJugada==True:
#			window["turno"].update("COMPUTADORA")
#			jugadorC.set_jugar()
			#print(jugadorC.get_turno())
#			turno_computadora = jugadorC.get_turno()
#			turno_computadora = jugadaPC.programaPrincipal(turno_computadora,validez,window,puntos,jugadorC,letras,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada)
#			window["puntosPc"].update(jugadorC.get_puntaje())
#			esPrimerJugada=False			 	
	
	window.close() 	 
	
 
