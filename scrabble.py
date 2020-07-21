import PySimpleGUI as sg
import validar_palabra_lexicon as ppattern
import jugada_computadora as jugadaPC
import random
import pickle
from datetime import date
#import build_words_pattern_nom as juegaCompu
 
def verTopTen(topt):
	lista=[]
	for key,value in topt.items():
		lista.append((key,value["nivel"],value["puntaje"],value["fecha"]))
	orden=[]
	norden=1
	for i in lista:
		orden.append("{:^2}{:^30}{:^10}{:^20}{:^20}".format(str(norden),i[0],i[1],str(i[2]),str(i[3])))
		norden = norden + 1
	return orden

def muestro_l(window,atril): 
    for indice in range(len(atril)):
        letra = atril[indice] 
        window.FindElement("Letra" + str(indice)).Update(letra)

def muestro_lc(window,atril): 
    for indice in range(len(atril)):
        letra = atril[indice] 
        window.FindElement("LetraC" + str(indice)).Update("*")
   
def accion_atril (window,atrilJ,pos,textBoton,datosEleccion):
	datosEleccion[pos] = atrilJ[pos]
	letraElegida = atrilJ[pos]  
	window.FindElement(textBoton).Update("")
	atrilJ[pos] = 0
	return letraElegida
	
def accion_tablero(window,event,listaCoordenadas,letraElegida,matriz):
	posicionCasilleroTablero = event  #me da que boton del tablero toque
	listaCoordenadas.append(posicionCasilleroTablero)
	
	x=posicionCasilleroTablero[0]
	y=posicionCasilleroTablero[1]
	
	window[posicionCasilleroTablero].update(letraElegida)
	matriz[x][y] = letraElegida
	window.FindElement((x,y)).Update(disabled = True)
	return listaCoordenadas
	
def armar_palabra(listaCoordenadas,matriz):
	unionLetras = []
	listaCoordenadas.sort()
	for lcoord in listaCoordenadas:
		x= lcoord[0]
		y= lcoord[1]
		unionLetras.append(matriz[x][y])
	pal=(''.join(unionLetras)).lower()
	return pal
	
def rellenar_atril(window,atrilJ,letras):
	for indice in range(len(atrilJ)):
		if atrilJ[indice] == 0:
			letra=random.choice(letras)
			atrilJ[indice] = letra
			window.FindElement("Letra" + str(indice)).Update(letra)
			letras.remove(letra)
		#print(atrilJ)
	return atrilJ
	
def devolver_letras_atril(window,listaCoordenadas,matriz,atrilJ,datosEleccion,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada):
	for lcoord in listaCoordenadas:
		x=lcoord[0]
		y=lcoord[1]
		
		letra = matriz[x][y]
		window.FindElement(lcoord).Update("")
		if (x,y) in casillas_naranja:
			window.FindElement(lcoord).Update("DL", button_color=("black", "#F4963E"))
		if (x,y) in casillas_azules:
			window.FindElement(lcoord).Update("TL", button_color=("black", "#1A4C86"))
		if (x,y) in casillas_rojas:
			window.FindElement(lcoord).Update("TP", button_color=("black", "#C91A4F"))
		if jugada.get_nivel() == "D" and (x,y) in casillas_descuento:
			window.FindElement(lcoord).Update("x", button_color=("black", "#F00F0F"))
		if jugada.get_nivel() == "F" and (x,y) in casillas_celeste:
			window.FindElement(lcoord).Update("TL", button_color=("black", "#4893E9"))
			
		matriz[x][y] = 0
		window.FindElement((x,y)).Update(disabled = False)
		
	for pos,val in datosEleccion.items() :
		atrilJ[pos] = val
		window.FindElement("Letra" + str(pos)).Update(val)
	
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
    window[(7, 7)].update(button_color=("black", "gray"))
    for cas in casillas_azules:
        window[cas].update("TL", button_color=("black", "#1A4C86"))
    for cas in casillas_rojas:
        window[cas].update("TP", button_color=("black", "#C91A4F"))
    for cas in casillas_naranja:
        window[cas].update("DL", button_color=("black", "#F4963E"))

        
def tablero_facil(window, casillas_azules, casillas_rojas, casillas_naranja, casillas_celeste):
    tablero_medio(window, casillas_azules, casillas_rojas, casillas_naranja)
    for cas in casillas_celeste:
        window[cas].update("TL", button_color=("black", "#4893E9"))
        
def tablero_dificil(window, casillas_azules, casillas_rojas, casillas_naranja, casillas_descuento):
	tablero_medio(window, casillas_azules, casillas_rojas, casillas_naranja)
	for cas in casillas_descuento:
		window[cas].update("x", button_color=("black", "#F00F0F"))
	
def no_es_horizontal_o_vertical(window,event,atrilJ,datosEleccion,letraElegida,listaCoordenadas):
	print('entre a event es distinto de coordx')
	sg.Popup('debes seguir horizontal!')
	window.FindElement(event).Update("")
	listaCoordenadas.remove(event)
	atrilJ[datosEleccion[letraElegida]]= letraElegida
	window.FindElement("Letra" + str(datosEleccion[letraElegida])).Update(letraElegida)
	datosEleccion.pop(letraElegida)
	return datosEleccion


def main(args):  
	jugada=args
	puntos=jugada.get_puntos()
	letras = jugada.get_letras()
	#jugada.get_nivel()
	jugada.set_fecha(date.today())
	#turno = jugada.get_turno()
	
	sg.theme("GreenTan")

	max_col = max_rows = 15
    
    
	casillas_azules = [(1,5), (1,9), (5,1), (5,5), (5,9),(5,13), (9,1), (9,5), (9,9), (9,13), (13,5), (13,9)]
	casillas_rojas = [(0,0), (0,7), (0,14), (7,0),(7,14), (14,0), (14,7), (14,14)]
	casillas_celeste = [(0,3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8,12), (11,0), (11,7), (11,14), (12,6), (12,8), (14,3), (14,11)]
	casillas_naranja = [(1,1), (2,2), (3,3), (4,4), (6,6), (8,8), (10,10), (11,11), (12,12), (13,13), (13,1), (12,2), (11,3), (10,4), (8,6), (6,8), (4,10), (3,11), (2,12), (1,13)]
	casillas_descuento = [(2,4), (2,10), (4,6), (10,6), (10,8), (12,4), (12,10), (7,1), (7,13), (1,7), (13,7), (4,2), (10,2), (4,12), (10,12), (6,4), (8,4), (6,10), (8,10), (4,8)]

  
	letrasEnTablero = [] 
	columna_1 = [
        [sg.Text("Jugador"),sg.Input(size=(15, 1), key="nombre")],
        [sg.Text("Nivel"),sg.Input(size=(2,3), key="nivel")],
        [sg.Button("Posponer", size=(10,1), key="posponer"), sg.Button("Reanudar", size=(10,1), key="reanudar"), sg.Button("Finalizar", button_color=("white", "red"), size=(10,1), key="finalizo")],
        [sg.Button("Ver TopTen", size=(10,1))],
        [sg.Text("Puntos Jugador", size=(16,1)), sg.Text("Puntos Compu")], 
        [sg.Input(size=(15, 1), key="puntosJug"), sg.Text("", size=(1,1)), sg.Input(size=(15, 1), key="puntosPc")],
        [sg.Text("Tiempo", justification="center")], [sg.Text(
            size=(10, 2), font=('Helvetica', 20), justification='center', key='tiempo')],
        [sg.Text("Computadora")],
        [sg.Text(" ", size=(3, 1)), sg.Button("", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="LetraC0"), sg.Button("", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="LetraC1"), sg.Button("", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="LetraC2"), sg.Button(
            "", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="LetraC3"), sg.Button("", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="LetraC4"), sg.Button("", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="LetraC5"), sg.Button("", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="LetraC6")],
        [sg.Text(" ", size=(1, 1))],
        [sg.Text("Jugador")],
        [sg.Text(" ", size=(3, 1)), sg.Button("", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="Letra0"), sg.Button("", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="Letra1"), sg.Button("", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="Letra2"), sg.Button(
            "", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="Letra3"), sg.Button("", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="Letra4"), sg.Button("", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="Letra5"), sg.Button("", size=(2, 1),disabled = False,disabled_button_color = ( "white" , "tan" ), key="Letra6")],
        [sg.Text("", size=(1,1))],
        [sg.Button('Insertar Palabra', size=(12, 1), key="insertar"), sg.Button("Cambio letras", size=(12, 1), key="cambio"), sg.Button('Pasar', size=(9, 1), key="pasar")],
        [sg.Text("", size=(1,1))]
    ]

	columna_tablero = [[sg.Button("", size=(2, 1),disabled = False, key=(i, j), pad=(0, 0), disabled_button_color = ( "white" , "tan" ), 
		button_color=("black", "tan")) for j in range(max_col)] for i in range(max_rows)]
		
	columna_2 = [[sg.Text("TURNO"),sg.Input(size=(15, 1), key="turno")]]
		
				   
	layout = [
        [sg.Column(columna_tablero), sg.Column(columna_2), sg.Column(columna_1)]
		]

	window = sg.Window("::::::::: SCRABBLE AR :::::::::", layout)
	window.Finalize()

	tiempoCorriendo = False
	contador = 0
	tiempoEleccionPalbara = False
	contadorEleccionPalabra =0
	jugadorJ=jugada.get_jugadorJ()
	jugadorC=jugada.get_jugadorC()
	duracion_jugada=jugada.get_tiempo()
	duracion_elecc_palabra = jugada.get_tiempoEleccionP()
	listaCoordenadas = []
	matriz=[]
	datosEleccion = {}
	datosEleccionC = {}
	esValida = False
	esHorizontal = False
	esVertical = False
	triplica = False
#	niv = jugada.get_nivel()
	
	#unionLetras = []
	atrilJ = jugadorJ._atril
	atrilC = jugadorC._atril
  
	for i in range (15):
		matriz.append([0]*15)  
		
	window["nivel"].update(jugada.get_nivel())	
	window["nombre"].update(jugadorJ.get_nombre())
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
  
	muestro_l(window,jugadorJ.get_atril())
	muestro_lc(window,jugadorC.get_atril())
	#jugadorJ.set_turno = True
	jugadorJ.set_jugar()
	tiempoCorriendo = True 
	esPrimerJugada = True
	validez = False
	
	while tiempoCorriendo == True:
		event, values = window.Read(timeout=10)
		
		if event == None:
			break
			
		tiempoEleccionPalabra = True
		#print(duracion_jugada, duracion_elecc_palabra)
		
		if jugadorC.get_turno() == False:
			#print(atrilC)
			window["turno"].update(jugadorJ.get_nombre())
			for i in range(len(atrilC)):
				window.FindElement("LetraC" + str(i)).Update(disabled = True)
				
		if contadorEleccionPalabra == duracion_elecc_palabra: #equivale a 3 min
			tiempoEleccionPalabra = False
			contadorEleccionPalabra = 0
			window["turno"].update("COMPUTADORA")
			jugadorJ.set_dejarJugar()
			#print(jugadorJ.get_turno())
			jugadorC.set_jugar()
			turno_computadora = jugadorC.get_turno()
			turno_computadora = jugadaPC.programaPrincipal(turno_computadora,validez,window,puntos,jugadorC,letras,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada)
			#print('turno despues de que volvi de jugada pc ', turno_computadora)
			window["puntosPc"].update(jugadorC.get_puntaje())
			window["turno"].update(jugadorJ.get_nombre())
			jugadorJ.set_jugar()
  
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
			
			if len(listaCoordenadas) == 0:
				listaCoordenadas = accion_tablero(window,event,listaCoordenadas,letraElegida,matriz)
				
				coordx = listaCoordenadas[0][0]
				coordy = listaCoordenadas[0][1]
			elif len(listaCoordenadas) == 1:
				
				if event[0] == coordx:
					esHorizontal = True
					esvertical = False
				else:
					esVertical = True
					esHorizontal = False
				
				listaCoordenadas = accion_tablero(window,event,listaCoordenadas,letraElegida,matriz)

			elif len(listaCoordenadas) > 1:
				
				if esHorizontal:
					listaCoordenadas = accion_tablero(window,event,listaCoordenadas,letraElegida,matriz)
					if event[0] != coordx:
						datosEleccion= no_es_horizontal_o_vertical(window,event,atrilJ,datosEleccion,letraElegida,listaCoordenadas)
						#print('listacoord ',listaCoordenadas)
				
				if esVertical:
					listaCoordenadas = accion_tablero(window,event,listaCoordenadas,letraElegida,matriz)
					if event[1] != coordy:
						datosEleccion= no_es_horizontal_o_vertical(window,event,atrilJ,datosEleccion,letraElegida,listaCoordenadas)
						#print('listacoord ',listaCoordenadas)
			
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
						jugadaPC.eliminar_coord_en_pc(listaCoordenadas)
						print(listaCoordenadas)

						ptos=int(values["puntosJug"])
						
						for lcoord in listaCoordenadas:
							x=lcoord[0]
							y=lcoord[1]
							letra = matriz[x][y]	
							p=puntos.get(letra)	
							print("letra",letra,"puntos",p)
							if (x,y) in casillas_naranja:
								p=p*2
								print("letra",letra,"x",x,"y",y,"duplica")  
							if (x,y) in casillas_azules: 
								p=p*3						
								print("letra",letra,"x",x,"y",y,"triplica")
							if jugada.get_nivel() == "F" and (x,y) in casillas_celeste: 
								p=p*3
								print("letra",letra,"x",x,"y",y,"triplica")
							if jugada.get_nivel() == "D" and (x,y) in casillas_descuento:
								p=(-1)*p
								print("letra",letra,"x",x,"y",y,"descuenta")
							if (x,y) in casillas_rojas:
								triplica = True
								
							ptos=ptos+p	
							
						if triplica:
							ptos = ptos*3					    
							
						listaCoordenadas = []

						#for j in palabra:
						#	ptos=ptos+puntos.get(j)
									
						window["puntosJug"].update(ptos)
						
						jugadorJ.set_puntaje(ptos)
						jugadorJ.set_dejarJugar()
						esPrimerJugada = False
						window["turno"].update("COMPUTADORA")
						jugadorC.set_jugar()
						#print(jugadorC.get_turno())
						turno_computadora = jugadorC.get_turno()
						turno_computadora = jugadaPC.programaPrincipal(turno_computadora,validez,window,puntos,jugadorC,letras,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada)
			#-----------------------------------------------
						esPrimeraJugada = False
			#-----------------------------------------------
						window["puntosPc"].update(jugadorC.get_puntaje())
						#print('turno despues de que volvi de jugada pc ', turno_computadora)
						window["turno"].update(jugadorJ.get_nombre())
						jugadorJ.set_jugar()
					else:
						listaCoordenadas = devolver_letras_atril(window,listaCoordenadas,matriz,atrilJ,datosEleccion,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada)
						datosEleccion = {}
						#print('lista coord ', listaCoordenadas)
						#print('datos eleccion ', datosEleccion)
						#print(atrilJ)
						esPrimerJugada =False
						
						sg.Popup('La palabra no es válida, turno de la computadora')
						jugadorJ.set_dejarJugar()
						#print(jugadorJ.get_turno())
						jugadorC.set_jugar()
						window["turno"].update("COMPUTADORA")
						turno_computadora = jugadorC.get_turno()
						turno_computadora = jugadaPC.programaPrincipal(turno_computadora,validez,window,puntos,jugadorC,letras,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada)
						window["puntosPc"].update(jugadorC.get_puntaje())
						#print('turno despues de que volvi de jugada pc ', turno_computadora)
						window["turno"].update(jugadorJ.get_nombre())
						jugadorJ.set_jugar()
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
				print('palabra ',palabra)
				print('voy a analizar la palabra')
				esValida = ppattern.analizar_palabra_pat(palabra, esValida)
				palabra = palabra.upper()
				print('volvi de analizar la palabra',palabra)
				print('palabra analizada es: ', esValida)
				if esValida:
					rellenar_atril(window,atrilJ,letras)
					jugadaPC.eliminar_coord_en_pc(listaCoordenadas)
					
					print(listaCoordenadas)
					
					ptos=int(values["puntosJug"])
						
					for lcoord in listaCoordenadas:
						x=lcoord[0]
						y=lcoord[1]
						letra = matriz[x][y]	
						p=puntos.get(letra)	
						print("letra",letra,"puntos",p)
						if (x,y) in casillas_naranja:
							p=p*2
							print("letra",letra,"x",x,"y",y,"duplica")  
						if (x,y) in casillas_azules: 
							p=p*3						
							print("letra",letra,"x",x,"y",y,"triplica")
						if jugada.get_nivel() == "F" and (x,y) in casillas_celeste: 
							p=p*3
							print("letra",letra,"x",x,"y",y,"triplica")
						if jugada.get_nivel() == "D" and (x,y) in casillas_descuento:
							p=(-1)*p
							print("letra",letra,"x",x,"y",y,"descuenta")
						if (x,y) in casillas_rojas:
								triplica = True
						ptos=ptos+p	
					
					if triplica:
							ptos = ptos*3
							
					listaCoordenadas = []					    
						
					window["puntosJug"].update(ptos)
					jugadorJ.set_puntaje(ptos)
					jugadorJ.set_dejarJugar()
					window["turno"].update('COMPUTADORA')
					jugadorJ.get_nombre()
					jugadorJ.set_dejarJugar()
					#print(jugadorJ.get_turno())
					jugadorC.set_jugar()
					turno_computadora = jugadorC.get_turno()
					turno_computadora = jugadaPC.programaPrincipal(turno_computadora,validez,window,puntos,jugadorC,letras,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada)
					window["puntosPc"].update(jugadorC.get_puntaje())
					#print('turno despues de que volvi de jugada pc ', turno_computadora)
					window["turno"].update(jugadorJ.get_nombre())
					jugadorJ.set_jugar()
				else:
					listaCoordenadas = devolver_letras_atril(window,listaCoordenadas,matriz,atrilJ,datosEleccion,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada)
					datosEleccion = {}
					#print('lista coord ', listaCoordenadas)
					#print('datos eleccion ', datosEleccion)
					print(atrilJ)
					
					sg.Popup('La palabra no es válida, turno de la computadora')
					jugadorJ.set_dejarJugar()
					#print(jugadorJ.get_turno())
					jugadorC.set_jugar()
					window["turno"].update("COMPUTADORA")
			
					turno_computadora = jugadorC.get_turno()
					turno_computadora = jugadaPC.programaPrincipal(turno_computadora,validez,window,puntos,jugadorC,letras,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada)
					window["puntosPc"].update(jugadorC.get_puntaje())
					#print('turno despues de que volvi de jugada pc ', turno_computadora)
					window["turno"].update(jugadorJ.get_nombre())
					jugadorJ.set_jugar()
			print(esPrimerJugada)
			
		if event == 'pasar':
			jugadorJ.set_dejarJugar()
			#print(jugadorJ.get_turno())
			#abiri modulo compu
			jugadorC.set_jugar()
			turno_computadora = jugadorC.get_turno()
			#print('turno pc ', turno_computadora)
			window["turno"].update(jugadorC.get_nombre())
			turno_computadora = jugadaPC.programaPrincipal(turno_computadora,validez,window,puntos,jugadorC,letras,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada)
			#print("esprimer",esPrimerJugada)
			#print("puntaje",jugadorC.get_puntaje())
			esPrimerJugada=False
			#print("esprimer",esPrimerJugada)	
			window["puntosPc"].update(jugadorC.get_puntaje())
			#print('turno despues de que volvi de jugada pc ', turno_computadora)
			window["turno"].update(jugadorJ.get_nombre())
			jugadorJ.set_jugar()
											
		if event == "finalizo" or contador == duracion_jugada: #equivale a 2 hs 
			tiempoCorriendo = False
			topten=jugada.get_topten()
			topten.setdefault(jugadorJ.get_nombre(),{'nivel': jugada.get_nivel() , 'puntaje': jugadorJ.get_puntaje(), 'fecha': jugada.get_fecha()})
			topten=dict(sorted(topten.items(), key=lambda uno:uno[1]['puntaje'],reverse=True)[:10])
			with open('topten.pkl', 'wb') as f:
				pickle.dump(topten, f, pickle.HIGHEST_PROTOCOL)
				f.close()
			break
	    
		if event == "Ver TopTen":
			topten=jugada.get_topten()
			layout2=[[sg.Text('ORDEN'),sg.Text('JUGADOR'),sg.Text('NIVEL'),sg.Text('PUNTAJE'),sg.Text('FECHA')],
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
			with open('scrabble.pkl', 'wb') as output:
				pickle.dump(jugada, output, pickle.HIGHEST_PROTOCOL)
				output.close()
			topten=jugada.get_topten()
			print(topten)	
			with open('topten.pkl', 'wb') as f:
				pickle.dump(topten, f, pickle.HIGHEST_PROTOCOL)
			f.close()	
			break
			
		if event == "reanudar":
			tiempoCorriendo = True
			with open('scrabble.pkl', 'rb') as input:
				jugada = pickle.load(input)
			jugadorJ=jugada.get_jugadorJ()
			
			if not values["nombre"] == jugadorJ.get_nombre():
				sg.Popup("No puede reanudar ..es otro jugador")
			else:				
				jugadorC=jugada.get_jugadorC()
				window["nombre"].update(jugadorJ.get_nombre())
				window["puntosJug"].update(jugadorJ.get_puntaje())
		  
				muestro_l(window,jugadorJ.get_atril())
				muestro_lc(window,jugadorC.get_atril())
				topten=jugada.get_topten()
			
		if tiempoCorriendo: 
			window["tiempo"].update("{:02d}:{:02d}:{:02d}".format((contador // 1000) // 360,(contador // 100) // 60, (contador // 100) % 60))
			contador += 1
			
		if tiempoEleccionPalabra: 
			contadorEleccionPalabra += 1
	  
		if event == "cambio":
			if jugadorJ.verificoatrilcompleto(jugadorJ.get_atril()):
				if jugada.get_cantCambios()<3:
					jugadorJ.cambioL(letras,jugadorJ.get_atril(),window)
					print(jugadorJ.get_atril())
					jugada.sumarCambio()
				else:
					sg.Popup("ya hizo los 3 cambios permitidos")
					
					jugadorJ.set_dejarJugar()	
					print(jugadorJ.get_turno())	
					
					window["turno"].update("COMPUTADORA")
					jugadorJ.set_dejarJugar()
					print(jugadorJ.get_turno())
					jugadorC.set_jugar()
					turno_computadora = jugadorC.get_turno()
					turno_computadora = jugadaPC.programaPrincipal(turno_computadora,validez,window,puntos,jugadorC,letras,casillas_naranja,casillas_azules,casillas_rojas,casillas_celeste,casillas_descuento,jugada)
					print('turno despues de que volvi de jugada pc ', turno_computadora)
					window["turno"].update(jugadorJ.get_nombre())
					jugadorJ.set_jugar()					 
			else:
				sg.Popup("el atril no esta completo")				 	
	window.close() 	 
 
