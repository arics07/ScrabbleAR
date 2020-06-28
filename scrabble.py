import PySimpleGUI as sg
import validar_palabra_lexicon as ppattern
import random
import pickle
from datetime import date
#import build_words_pattern_nom as juegaCompu
  
def muestro_l(window,atril): 
    for indice in range(len(atril)):
        letra = atril[indice] 
        window.FindElement("Letra" + str(indice)).Update(letra)

def muestro_lc(window,atril): 
    for indice in range(len(atril)):
        letra = atril[indice] 
        window.FindElement("LetraC" + str(indice)).Update("*")
   
def accion_atril (window,atrilJ,pos,textBoton):
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
	
def devolver_letras_atril(window,listaCoordenadas,matriz,atrilJ):
	guardoLetrasTemporal = []
	for lcoord in listaCoordenadas:
		x=lcoord[0]
		y=lcoord[1]
		
		letra = matriz[x][y]
		guardoLetrasTemporal.append(letra)
		window.FindElement(lcoord).Update("")
	for indice in range(len(atrilJ)):
		if atrilJ[indice]== 0:
			valor = random.choice(guardoLetrasTemporal)
			atrilJ[indice]= valor
			guardoLetrasTemporal.remove(valor)
			window.FindElement("Letra" + str(indice)).Update(valor)
	unionLetras = []
	listaCoordenadas = []
	#print(listaCoordenadas)
	return listaCoordenadas#atrilJ	

def colores_tablero(window, casillas_azules, casillas_rojas, casillas_naranja):
    window[(7, 7)].update(button_color=("white", "gray"))
    for cas in casillas_azules:
        window[cas].update("TL", button_color=("white", "blue"))
    for cas in casillas_rojas:
        window[cas].update("TP", button_color=("white", "red"))
    for cas in casillas_naranja:
        window[cas].update("DL", button_color=("white", "orange"))


def main(args):  
	jugada=args
	puntos=jugada.get_puntos()
	letras = jugada.get_letras()
	jugada.get_nivel()
	jugada.set_fecha(date.today())

	sg.theme("GreenTan")

	max_col = max_rows = 15

	casillas_azules = [(1, 5), (1, 9), (5, 1), (5, 5), (5, 9),(5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9)]
	casillas_rojas = [(0, 0), (0, 7), (0, 14), (7, 0),(7, 14), (14, 0), (14, 7), (14, 14)]
	casillas_naranja = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (
        13, 13), (13, 1), (12, 2), (11, 3), (10, 4), (9, 5), (8, 6), (6, 8), (5, 9), (4, 10), (3, 11), (2, 12), (1, 13)]
  
	letrasEnTablero = [] 
	columna_1 = [
        [sg.Text("Jugador"),sg.Input(size=(15, 1), key="nombre")],
        [sg.Text("Nivel"),sg.Input(size=(2,3), key="nivel")],
        [sg.Button("Posponer", key="posponer"), sg.Button("Reanudar", key="reanudar")],
        [sg.Button("Finalizar", button_color=(
            "white", "red"), key="finalizo")],
        [sg.Text("Puntos Jugador")], [
            sg.Input(size=(15, 1), key="puntosJug")],
        [sg.Text("Puntos Compu")], [
            sg.Input(size=(15, 1), key="puntosPc")],
        [sg.Text("Tiempo", justification="center")], [sg.Text(
            size=(5, 2), font=('Helvetica', 20), justification='center', key='tiempo')],
        [sg.Text("Computadora")],
        [sg.Text(" ", size=(1, 1)), sg.Button("", size=(2, 1), key="LetraC0"), sg.Button("", size=(2, 1), key="LetraC1"), sg.Button("", size=(2, 1), key="LetraC2"), sg.Button(
            "", size=(2, 1), key="LetraC3"), sg.Button("", size=(2, 1), key="LetraC4"), sg.Button("", size=(2, 1), key="LetraC5"), sg.Button("", size=(2, 1), key="LetraC6")],
        [sg.Text(" ", size=(1, 1))],
        [sg.Text("Jugador")],
        [sg.Text(" ", size=(1, 1)), sg.Button("", size=(2, 1), key="Letra0"), sg.Button("", size=(2, 1), key="Letra1"), sg.Button("", size=(2, 1), key="Letra2"), sg.Button(
            "", size=(2, 1), key="Letra3"), sg.Button("", size=(2, 1), key="Letra4"), sg.Button("", size=(2, 1), key="Letra5"), sg.Button("", size=(2, 1), key="Letra6")],
        [sg.Text(" ", size=(4, 1)), sg.Button(
            "Cambio letras", size=(12, 2), key="cambio")]
    ]

	columna_tablero = [[sg.Button("", size=(2, 1), key=(i, j), pad=(0, 0), button_color=(
        "white", "tan")) for j in range(max_col)] for i in range(max_rows)]

	layout = [
        [sg.Column(columna_tablero), sg.Column(columna_1)],
        [sg.Button('Insertar Palabra', size=(9, 2), key="insertar"),
         sg.Button('Pasar', size=(9, 2), key="pasar")]
    ]

	window = sg.Window("::::::::: SCRABBLE AR :::::::::", layout)
	window.Finalize()

	tiempoCorriendo = False
	contador = 0
	jugadorJ=jugada.get_jugadorJ()
	jugadorC=jugada.get_jugadorC()
	listaCoordenadas = []
	matriz=[]
	esValida = False
	
	#unionLetras = []
	atrilJ = jugadorJ._atril
  
	for i in range (15):
		matriz.append([0]*15)  
		
	window["nivel"].update(jugada.get_nivel())	
	window["nombre"].update(jugadorJ.get_nombre())
	window["puntosJug"].update(jugadorJ.get_puntaje())
	# colores
	colores_tablero(window, casillas_azules,
	casillas_rojas, casillas_naranja)
  
	muestro_l(window,jugadorJ.get_atril())
	muestro_lc(window,jugadorC.get_atril())
	jugadorJ.set_turno = True
	tiempoCorriendo = True 
	while tiempoCorriendo == True:
		event, values = window.Read(timeout=10)
  
		if event == 'Letra0':
			letraElegida = accion_atril(window,atrilJ,0,event)
  
		if event == 'Letra1':
			letraElegida = accion_atril(window,atrilJ,1,event)
  
		if event == 'Letra2':
			letraElegida = accion_atril(window,atrilJ,2,event)
	  
		if event == 'Letra3':
			letraElegida = accion_atril(window,atrilJ,3,event)
	  
		if event == 'Letra4':
			letraElegida = accion_atril(window,atrilJ,4,event)
	  
		if event == 'Letra5':
			letraElegida = accion_atril(window,atrilJ,5,event)
	  
		if event == 'Letra6':
			letraElegida = accion_atril(window,atrilJ,6,event)
	  
		if type(event) is tuple:
			print('tamaño lista coordenadas ', len(listaCoordenadas))
			if len(listaCoordenadas) == 0:
				listaCoordenadas = accion_tablero(window,event,listaCoordenadas,letraElegida,matriz)
			else:
				coordx=listaCoordenadas[0][0]
				coordy=listaCoordenadas[0][1]
				listaCoordenadas = accion_tablero(window,event,listaCoordenadas,letraElegida,matriz)
				for i in listaCoordenadas:
					if i[1] == coordy+1:
						print('va por horizontal', listaCoordenadas)
					elif i[0] == coordx+1:
						print('va por vertcal',listaCoordenadas)	
		  
		if event == 'insertar':
			palabra = armar_palabra(listaCoordenadas,matriz)
			print('palabra ',palabra)
			print('voy a analizar la palabra')
			esValida = ppattern.analizar_palabra_pat(palabra, esValida)
			palabra = palabra.upper()
			print('volvi de analizar la palabra',palabra)
			print('palabra analizada es: ', esValida)
			esValida=True
			if esValida:
				rellenar_atril(window,atrilJ,letras)
				listaCoordenadas = []
				print(listaCoordenadas)
				
				ptos=int(values["puntosJug"])
				for j in palabra:
					ptos=ptos+puntos.get(j)
				window["puntosJug"].update(ptos)
				jugadorJ.set_puntaje(ptos)
				
			else:
				listaCoordenadas = devolver_letras_atril(window,listaCoordenadas,matriz,atrilJ)
				print('lista coord ', listaCoordenadas)
											
		if event == "finalizo":
			tiempoCorriendo = False
			topten=jugada.get_topten()
			topten.setdefault(jugadorJ.get_nombre(),{'nivel': jugada.get_nivel() , 'puntaje': jugadorJ.get_puntaje(), 'fecha': jugada.get_fecha()})
			print("top ten",topten)
			#print('topten items',topten.items())
			
			#topten=dict(sorted(topten.items(), key = lambda x:x[1].values()))
			
			with open('topten.pkl', 'wb') as f:
				
				pickle.dump(topten, f, pickle.HIGHEST_PROTOCOL)
				f.close()
		    
			break
	  
		if event ==  "posponer":
			tiempoCorriendo = False
			with open('scrabble.pkl', 'wb') as output:
				pickle.dump(jugada, output, pickle.HIGHEST_PROTOCOL)
				output.close()
			topten=jugada.get_topten()	
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
			window["tiempo"].update("{:02d}:{:02d}".format((contador // 100) // 60, (contador // 100) % 60))
			contador += 1
	  
		if event == "cambio":
			if jugadorJ.verificoatrilcompleto(jugadorJ.get_atril()):
				if jugada.get_cantCambios()<3:
					jugadorJ.cambioL(letras,jugadorJ.get_atril(),window)
					print(jugadorJ.get_atril())
					jugada.sumarCambio()
				else:
					sg.Popup("ya hizo los 3 cambios permitidos")				 
			else:
				sg.Popup("el atril no esta completo")				 	
	window.close() 	 
 
