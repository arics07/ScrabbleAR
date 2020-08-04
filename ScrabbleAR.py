import PySimpleGUI as sg
import scrabble
import datetime
import pickle
import copy
#import random
from random import randint
import jugada_computadora as jugadaPC
from jugador import jugador
from jugadas import jugadas

import Configuracion as conf

def inicializar_letras(letrasD):
	letras = []
	for lett in letrasD:
		for cant in range(letrasD[lett]["cant"]):
			letras.append(lett)
	#print(letras)
	return letras

def inicializar_puntos(letrasD):
	puntos = {}
	for lett in letrasD:
		puntos[lett]=letrasD[lett]["puntos"]
	#print(puntos)
	return puntos

def seteo_tiempo(duracion,nivel):
	"""Esta función convierte el tiempo obtenido en milisegundos"""
	minu = hor =seg = 0
	
	for clave,valor in duracion.items():
		print(clave,valor)
		if clave == "horas":
			hor = valor["cant"] * 360000
		if clave == "minutos":
			minu = valor["cant"] * 6000
		if clave == "segundos":
			print(valor["cant"])
			seg = valor["cant"] * 100
		print(hor, minu, seg)
	return (hor + minu + seg)


def main():
	
	sg.theme("GreenTan")
	
	desocupadas = []

	nom=""
	nivel=""
	tiempoPensandoPC=0
	layout=[[sg.Text('Jugador')],
	  [sg.InputText(key='nom',size=(29,3)),sg.Button("Reanudar",size=(20,1))],
	  [sg.Text("Elegir nivel:")],
	  [sg.Text("",size=(1,1)), sg.Button("Fácil",size=(20,1))],
	  [sg.Text("",size=(1,1)), sg.Button("Medio",size=(20,1))],
	  [sg.Text("",size=(1,1)), sg.Button("Difícil",size=(20,1))],
	  [sg.Text("",size=(1,1)), sg.Text("Nivel elegido: "), sg.Text(nivel, key="niv", font="bold")], 
	  [sg.Text("",size=(1,1)), sg.Button("Configurar", size=(10,1), disabled=True)],
	# [sg.Text('Nivel')],[sg.InputText(key='nivel',size=(3,2)),sg.Text('F=Facil M=Medio D=Dificil')],
	  [sg.Text("")],
	  [sg.Text("",size=(1,1)), sg.Button("Comenzar",size=(20,2),disabled=True)]
	  ]
	window = sg.Window('Ingreso Juego').Layout(layout)

	  
	letrasD = { "A": {"cant":11,"puntos":1},"B":{"cant":3,"puntos":3},"C":{"cant":4,"puntos":2},"D":{"cant":4,"puntos":2},"E":{"cant":11,"puntos":1},"F":{"cant":2,"puntos":4},"G":{"cant":2,"puntos":2},
	  "H":{"cant":2,"puntos":4},"I":{"cant":2,"puntos":1},"J":{"cant":2,"puntos":6},"K":{"cant":1,"puntos":8},"L":{"cant":4,"puntos":1},"LL":{"cant":1,"puntos":8},"M":{"cant":3,"puntos":3},"N":{"cant":5,"puntos":1},"Ñ":{"cant":1,"puntos":8},
	  "O":{"cant":4,"puntos":1},"P":{"cant":2,"puntos":3},"Q":{"cant":1,"puntos":8},"R":{"cant":4,"puntos":1},"RR":{"cant":1,"puntos":8},"S":{"cant":7,"puntos":1},"T":{"cant":4,"puntos":1},"U":{"cant":6,"puntos":4},"V":{"cant":2,"puntos":4},
	  "W":{"cant":1,"puntos":8},"X":{"cant":1,"puntos":8},"Y":{"cant":1,"puntos":4},"Z":{"cant":1,"puntos":10}}



	duracionJugada = {"F": {"horas":{"cant":1,"rango":(1,2)},"minutos":{"cant":0,"rango":(1,59)},"segundos":{"cant":0,"rango":(1,59)}}, "M": {"horas":{"cant":0,"rango":(1,2)},"minutos":{"cant":45,"rango":(1,59)},"segundos":{"cant":0,"rango":(1,59)}},"D":{"horas":{"cant":0,"rango":(1,2)},"minutos":{"cant":30,"rango":(1,59)},"segundos":{"cant":0,"rango":(1,59)}}}

	duracionEleccionPalabra = {"F": {"minutos":{"cant":3,"rango":(1,5)},"segundos":{"cant":0,"rango":(1,59)}}, "M": {"minutos":{"cant":2,"rango":(1,4)},"segundos":{"cant":0,"rango":(1,59)}},"D":{"minutos":{"cant":1,"rango":(1,3)},"segundos":{"cant":0,"rango":(1,59)}}}

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
			with open('scrabble.pkl', 'rb') as input:
				jugada = pickle.load(input)
				print(jugada)
			if not values["nom"] == jugada.get_jugadorJ().get_nombre():
				sg.Popup("No puede reanudar ..es otro jugador")
			else:			
				window.close()  	
				scrabble.main(jugada,"R")
				break
			
		if event == "Fácil":
			nivel="F"
			tiempoPensandoPC = randint(7,9)
			window["niv"].Update(nivel)
			window["Configurar"].Update(disabled=False)
			window["Comenzar"].Update(disabled=False)
			datosSlierRango = duracionJugada[nivel]["horas"]["rango"]
			datosSliderValorDefault= duracionJugada[nivel]["horas"]["cant"]
			datosSlierRango2 = duracionEleccionPalabra[nivel]["minutos"]["rango"]
			datosSliderValorDefault2 = duracionEleccionPalabra[nivel]["minutos"]["cant"]
			
			valorDefCombo = "Horas"
			valorDefCombo2 = "Minutos"
		  
		if event == "Medio":
			nivel="M"
			tiempoPensandoPC = randint(5,7)
			window["niv"].Update(nivel)
			window["Configurar"].Update(disabled=False)
			window["Comenzar"].Update(disabled=False)
			datosSlierRango = duracionJugada[nivel]["minutos"]["rango"]
			datosSliderValorDefault= duracionJugada[nivel]["minutos"]["cant"]
			datosSlierRango2 = duracionEleccionPalabra[nivel]["minutos"]["rango"]
			datosSliderValorDefault2 = duracionEleccionPalabra[nivel]["minutos"]["cant"]
			
			valorDefCombo = "Minutos"
			valorDefCombo2 = "Minutos"
		  
		if event == "Difícil":
			nivel="D"
			tiempoPensandoPC = randint(1,3)
			window["niv"].Update(nivel)
			window["Configurar"].Update(disabled=False)
			window["Comenzar"].Update(disabled=False)
			datosSlierRango = duracionJugada[nivel]["minutos"]["rango"]
			datosSliderValorDefault= duracionJugada[nivel]["minutos"]["cant"]
			datosSlierRango2 = duracionEleccionPalabra[nivel]["minutos"]["rango"]
			datosSliderValorDefault2 = duracionEleccionPalabra[nivel]["minutos"]["cant"]
			
			valorDefCombo = "Minutos"
			valorDefCombo2 = "Minutos"
	  
		if event == "Comenzar":  
			if values["nom"] == "":
				sg.Popup("Debe ingresar un nombre")
			else:  
				window.close()   
				jugadorJ = jugador(values["nom"])
				jugadorC = jugador('Computadora')
				letras = inicializar_letras(letrasD)
				puntos = inicializar_puntos(letrasD)
		  
				despcupadas = jugadaPC.cargar_tuplas_desocupadas(desocupadas)

				decide_primer_turno = {0:"jugador", 1:"computadora"}
				decide = randint(0,1)	
				primerTurno = decide_primer_turno[decide]
				print("empieza ", primerTurno)
			
				tiempoJugada = seteo_tiempo(duracionJugada[nivel],nivel)
				tiempoEleccionPalabra = seteo_tiempo(duracionEleccionPalabra[nivel],nivel)
				print("tiempoPensandoPC ",tiempoPensandoPC, tiempoJugada,tiempoEleccionPalabra)
				jugada=jugadas(datetime.datetime.now(),nivel,tiempoJugada,tiempoEleccionPalabra,tiempoPensandoPC,jugadorJ,jugadorC,"J",letras,puntos,primerTurno,desocupadas,[])
		   
				jugadorJ.elijoL(letras)
				jugadorC.elijoL(letras)
				try: 
					with open('topten.pkl', 'rb') as f:
						topten=dict(pickle.load(f))
				except:
					topten={}  
				jugada.set_topten(topten)
				scrabble.main(jugada,"C")
				break
		  
		if event == "Configurar":
			nivel,letrasD,duracionJugada,duracionEleccionPalabra= conf.programa_principal(valorDefCombo,datosSlierRango,datosSliderValorDefault,nivel,letrasD,duracionJugada,duracionEleccionPalabra,letras_backup,duracionJugada_backup,duracionEleccionPalabra_backup,datosSlierRango2,datosSliderValorDefault2,valorDefCombo2)
			print(duracionJugada)

if __name__ == '__main__':
	main()	
