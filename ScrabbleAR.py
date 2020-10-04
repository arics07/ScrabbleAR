import PySimpleGUI as sg
import datetime
import pickle
import copy
from random import randint
import binn.jugada_computadora
from lib.jugadas import jugadas
from lib.jugador import jugador
import binn.scrabble
import binn.Configuracion as conf

def inicializar_letras(letrasD):
	"""Esta función agrupa todas las letras en una lista"""
	letras = []
	for lett in letrasD:
		for cant in range(letrasD[lett]["cant"]):
			letras.append(lett)
	return letras

def inicializar_puntos(letrasD):
	"""Esta función crea un objeto con el puntaje correspondiente a cada letra"""
	puntos = {}
	for lett in letrasD:
		puntos[lett]=letrasD[lett]["puntos"]
	return puntos

def seteo_tiempo(duracion,nivel):
	"""Esta función convierte el tiempo obtenido en milisegundos"""
	minu = hor =seg = 0
	
	for clave,valor in duracion.items():
		if clave == "horas":
			hor = valor["cant"] * 360000
		if clave == "minutos":
			minu = valor["cant"] * 6000
		if clave == "segundos":
			seg = valor["cant"] * 100
	return (hor + minu + seg)


def main():
	
	sg.theme("LightGrey2")
	
	desocupadas = []

	nom=""
	nivel=""
	tiempoPensandoPC=0
	
	imgScrabble = 'img/scrabble_2.png'
	imgBotonGris = "img/fondo_boton_6.png"
	imgBotonFucsia = "img/fondo_boton_1.png"
	imagenBotonVerde = "img/fondo_boton_5.png"
	imagenBotonCeleste = "img/fondo_boton_3.png"
	imagenBotonVioleta = "img/fondo_boton_4.png"
	
	columna_1=[[sg.Text('Jugador')],
	  [sg.InputText(key='nom',size=(29,3))],
	  [sg.Button("Reanudar",size=(20,1), image_filename=imgBotonGris,image_size=(118,30),image_subsample=2, button_color=("white","lightGrey"))],
	  [sg.Text("",size=(1,1))],
	  [sg.Text("Elegir nivel:")],
	  [sg.Text("",size=(1,1)), sg.Button("Fácil",size=(20,1),image_filename=imagenBotonCeleste,image_size=(118,30),image_subsample=2, button_color=("white","lightGrey"))],
	  [sg.Text("",size=(1,1)), sg.Button("Medio",size=(20,1),image_filename=imagenBotonVioleta,image_size=(118,30),image_subsample=2, button_color=("white","lightGrey"))],
	  [sg.Text("",size=(1,1)), sg.Button("Difícil",size=(20,1),image_filename=imgBotonFucsia,image_size=(118,30),image_subsample=2, button_color=("white","lightGrey"))],
	  [sg.Text("",size=(1,1)), sg.Text("Nivel elegido: "), sg.Text(nivel, key="niv", font="bold")], 
	  [sg.Text("",size=(1,1)), sg.Button("Configurar", size=(10,1), disabled=True,image_filename=imgBotonGris,image_size=(118,30),image_subsample=2,disabled_button_color = ( "white" , "lightGrey"), button_color=("white","lightGrey"))],
	  [sg.Text("")],
	  [sg.Text("",size=(1,1)), sg.Button("Comenzar",size=(20,2),disabled=True,image_filename=imagenBotonVerde,image_size=(118,30),image_subsample=2,disabled_button_color = ( "white" , "lightGrey"), button_color=("white","lightGrey"))]]
	
	layout=[[sg.Image(imgScrabble)],
	  [sg.Text("",size=(1,1)),sg.Text("",size=(1,1)),sg.Text("",size=(1,1)),sg.Text("",size=(1,1)),sg.Column(columna_1)]
	  ]
	window = sg.Window('Ingreso Juego').Layout(layout)

	try: 
		with open('confi.pkl', 'rb') as f:
			confi=dict(pickle.load(f))
			f.close()
	except:
		sg.Popup("No se encontró el archivo confi.pkl")
			
			
	letrasD=confi["letrasD"]
	duracionJugada=confi["duracionJugada"]
	duracionEleccionPalabra=confi["duracionEleccionPalabra"]
		
			
	letras_backup = copy.deepcopy(letrasD)
	duracionJugada_backup = copy.deepcopy(duracionJugada)
	duracionEleccionPalabra_backup = copy.deepcopy(duracionEleccionPalabra)

	while True: 
		event, values=window.Read() 
	  
		if event == None:
			break
			 
		if event == "Reanudar":
			tiempoCorriendo = True
			esPrimerJugada=False
			try: 
				with open('scrabble.pkl', 'rb') as input:
					jugada = pickle.load(input)
					input.close()
		
			except:
				sg.Popup("No hay jugada guardada")	
			else:	
				if not values["nom"] == jugada.get_jugadorJ().get_nombre():
					sg.Popup("No puede reanudar ..es otro jugador")
				else:			
					window.close()  	
					binn.scrabble.main(jugada,"R")
					break
			
		if event == "Fácil":
			nivel="F"
			tiempoPensandoPC = randint(7,9)
			window["niv"].Update(nivel)
			window["Configurar"].Update(disabled=False)
			window["Comenzar"].Update(disabled=False)
		  
		if event == "Medio":
			nivel="M"
			tiempoPensandoPC = randint(5,7)
			window["niv"].Update(nivel)
			window["Configurar"].Update(disabled=False)
			window["Comenzar"].Update(disabled=False)
		  
		if event == "Difícil":
			nivel="D"
			tiempoPensandoPC = randint(1,3)
			window["niv"].Update(nivel)
			window["Configurar"].Update(disabled=False)
			window["Comenzar"].Update(disabled=False)

	  
		if event == "Comenzar":  
			if values["nom"] == "":
				sg.Popup("Debe ingresar un nombre")
			else:  
				window.close()   
				jugadorJ = jugador(values["nom"])
				jugadorC = jugador('Computadora')
				letras = inicializar_letras(letrasD)
				puntos = inicializar_puntos(letrasD)
		  
				despcupadas = binn.jugada_computadora.cargar_tuplas_desocupadas(desocupadas)

				decide_primer_turno = {0:"jugador", 1:"computadora"}
				decide = randint(0,1)	
				primerTurno = decide_primer_turno[decide]
				
			
				tiempoJugada = seteo_tiempo(duracionJugada[nivel],nivel)
				tiempoEleccionPalabra = seteo_tiempo(duracionEleccionPalabra[nivel],nivel)
				
				jugada=jugadas(datetime.datetime.now(),nivel,tiempoJugada,tiempoEleccionPalabra,tiempoPensandoPC,jugadorJ,jugadorC,"J",letras,puntos,primerTurno,desocupadas,[])
		   
				jugadorJ.elijoL(letras)
				jugadorC.elijoL(letras)
				try: 
					with open('topten.pkl', 'rb') as f:
						topten=dict(pickle.load(f))
						f.close()
				except:
					sg.Popup("No hay datos de de TopTen")
					topten={}  
				jugada.set_topten(topten)
				binn.scrabble.main(jugada,"C")
				break
		  
		if event == "Configurar":
			nivel,letrasD,duracionJugada,duracionEleccionPalabra= conf.programa_principal(nivel,letrasD,duracionJugada,duracionEleccionPalabra,letras_backup,duracionJugada_backup,duracionEleccionPalabra_backup)
			

if __name__ == '__main__':
	main()	
