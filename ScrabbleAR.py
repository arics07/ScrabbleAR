import PySimpleGUI as sg
import scrabble
import datetime
import pickle
import copy
from random import randint
from jugada_computadora import cargar_tuplas_desocupadas, desocupadas

from jugador import jugador
from jugadas import jugadas


sg.theme("GreenTan")

nom=""
nivel=""
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
  [sg.Text("",size=(1,1)), sg.Button("Comenzar",size=(20,2))]
  ]
window = sg.Window('Ingreso Juego').Layout(layout)

  
letrasD = { "A": {"cant":11,"puntos":1},"B":{"cant":3,"puntos":3},"C":{"cant":4,"puntos":2},"D":{"cant":4,"puntos":2},"E":{"cant":11,"puntos":1},"F":{"cant":2,"puntos":4},"G":{"cant":2,"puntos":2},
  "H":{"cant":2,"puntos":4},"I":{"cant":2,"puntos":1},"J":{"cant":2,"puntos":6},"K":{"cant":1,"puntos":8},"L":{"cant":4,"puntos":1},"LL":{"cant":1,"puntos":8},"M":{"cant":3,"puntos":3},"N":{"cant":5,"puntos":1},"Ñ":{"cant":1,"puntos":8},
  "O":{"cant":4,"puntos":1},"P":{"cant":2,"puntos":3},"Q":{"cant":1,"puntos":8},"R":{"cant":4,"puntos":1},"RR":{"cant":1,"puntos":8},"S":{"cant":7,"puntos":1},"T":{"cant":4,"puntos":1},"U":{"cant":6,"puntos":4},"V":{"cant":2,"puntos":4},
  "W":{"cant":1,"puntos":8},"X":{"cant":1,"puntos":8},"Y":{"cant":1,"puntos":4},"Z":{"cant":1,"puntos":10}}

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

duracionJugada = {"F": {"horas":1,"minutos":0,"segundos":0}, "M": {"horas":0,"minutos":45,"segundos":0},"D":{"horas":0,"minutos":30,"segundos":0}}

duracionEleccionPalabra = {"F": {"horas":0,"minutos":3,"segundos":0}, "M": {"horas":0,"minutos":2,"segundos":0},"D":{"horas":0,"minutos":1,"segundos":0}}

letras_backup = copy.deepcopy(letrasD)
duracionJugada_backup = copy.deepcopy(duracionJugada)
duracionEleccionPalabra_backup = copy.deepcopy(duracionEleccionPalabra)

def seteo_tiempo(duracionJugada,nivel):
	minu = hor =seg = 0
	if duracionJugada[nivel]["horas"] != 0:
		hor =duracionJugada[nivel]["horas"]*360000
	if duracionJugada[nivel]["minutos"] != 0:
		minu = duracionJugada[nivel]["minutos"]*6000
	if duracionJugada[nivel]["segundos"] != 0:
		seg = duracionJugada[nivel]["segundos"]*100
	return (hor + minu + seg)
  
while True: 
	event, values=window.Read() 
  
	if event == None:
		break
		 
	if event == "Reanudar":
		tiempoCorriendo = True
		with open('scrabble.pkl', 'rb') as input:
			jugada = pickle.load(input)
		if not values["nom"] == jugada.get_jugadorJ().get_nombre():
			sg.Popup("No puede reanudar ..es otro jugador")
		else:			
			window.close()  	
			scrabble.main(jugada,"R")
			break
        
	if event == "Fácil":
		nivel="F"
		window["niv"].Update(nivel)
		window["Configurar"].Update(disabled=False)
	  
	if event == "Medio":
		nivel="M"
		window["niv"].Update(nivel)
		window["Configurar"].Update(disabled=False)
	  
	if event == "Difícil":
		nivel="D"
		window["niv"].Update(nivel)
		window["Configurar"].Update(disabled=False)
  
	if event == "Comenzar":  
		if values["nom"] == "":
			sg.Popup("Debe ingresar un nombre")
		else:  
			window.close()   
			jugadorJ = jugador(values["nom"])
			jugadorC = jugador('Computadora')
			letras = inicializar_letras(letrasD)
			puntos = inicializar_puntos(letrasD)
      
<<<<<<< HEAD
			cargar_tuplas_desocupadas(desocupadas)
      
			decide_primer_turno = {0:"jugador", 1:"computadora"}
			decide = randint(0,1)	
			primerTurno = decide_primer_turno[decide]
=======
      decide_primer_turno = {0:"jugador", 1:"computadora"}
      decide = randint(0,1)	
      primerTurno = decide_primer_turno[decide]
      print("empieza ", primerTurno)
        
#      if nivel == "F":
      tiempoJugada = seteo_tiempo(duracionJugada,nivel)
      tiempoEleccionPalabra = seteo_tiempo(duracionEleccionPalabra,nivel)
      jugada=jugadas(datetime.datetime.now(),nivel,tiempoJugada,tiempoEleccionPalabra,jugadorJ,jugadorC,"J",letras,puntos,primerTurno)  
#     if nivel == "M":
#        tiempoJugada = seteo_tiempo(duracionJugada,"M")
#        tiempoEleccionPalabra = seteo_tiempo(duracionEleccionPalabra,"M") 
#        jugada=jugadas(datetime.datetime.now(),"M",tiempoJugada,tiempoEleccionPalabra,jugadorJ,jugadorC,"J",letras,puntos,primerTurno) 
#      if nivel == "D":
#        tiempoJugada = seteo_tiempo(duracionJugada,"D")
#        tiempoEleccionPalabra = seteo_tiempo(duracionEleccionPalabra,"D")
#        jugada=jugadas(datetime.datetime.now(),"D",tiempoJugada,tiempoEleccionPalabra,jugadorJ,jugadorC,"J",letras,puntos,primerTurno)  
  
>>>>>>> 9e329d15e0253c844af04678c8d4268283e81361
        
			tiempoJugada = seteo_tiempo(duracionJugada,nivel)
			tiempoEleccionPalabra = seteo_tiempo(duracionEleccionPalabra,nivel)
			jugada=jugadas(datetime.datetime.now(),nivel,tiempoJugada,tiempoEleccionPalabra,jugadorJ,jugadorC,"J",letras,puntos,primerTurno,[],[])
       
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
		columna1 = [
				[sg.Text("Letra", size=(4,1)), sg.Text("Puntos", size=(6,1)), sg.Text("Cantidad", size=(7,1))], 
				[sg.Text("A", size=(4,1)), sg.Input(letrasD["A"]["puntos"], size=(6,1), key=("A","p")), sg.Input(letrasD["A"]["cant"], size=(6,1), key=("A","c"))],
				[sg.Text("B", size=(4,1)), sg.Input(letrasD["B"]["puntos"], size=(6,1), key=("B","p")), sg.Input(letrasD["B"]["cant"], size=(6,1), key=("B","c"))],
				[sg.Text("C", size=(4,1)), sg.Input(letrasD["C"]["puntos"], size=(6,1), key=("C","p")), sg.Input(letrasD["C"]["cant"], size=(6,1), key=("C","c"))],
				[sg.Text("D", size=(4,1)), sg.Input(letrasD["D"]["puntos"], size=(6,1), key=("D","p")), sg.Input(letrasD["D"]["cant"], size=(6,1), key=("D","c"))],
				[sg.Text("E", size=(4,1)), sg.Input(letrasD["E"]["puntos"], size=(6,1), key=("E","p")), sg.Input(letrasD["E"]["cant"], size=(6,1), key=("E","c"))],
				[sg.Text("F", size=(4,1)), sg.Input(letrasD["F"]["puntos"], size=(6,1), key=("F","p")), sg.Input(letrasD["F"]["cant"], size=(6,1), key=("F","c"))],
				[sg.Text("G", size=(4,1)), sg.Input(letrasD["G"]["puntos"], size=(6,1), key=("G","p")), sg.Input(letrasD["G"]["cant"], size=(6,1), key=("G","c"))],
				[sg.Text("H", size=(4,1)), sg.Input(letrasD["H"]["puntos"], size=(6,1), key=("H","p")), sg.Input(letrasD["H"]["cant"], size=(6,1), key=("H","c"))],
				[sg.Text("")],
				[sg.Text("Duración jugada")],
				[sg.Text("Hs",size=(4,1)), sg.Text("Min",size=(3,1)),sg.Text("Seg",size=(4,1))],
				[sg.Input(duracionJugada[nivel]["horas"],key="hor",size=(4,5)),sg.Input(duracionJugada[nivel]["minutos"],key="min",size=(4,5)), sg.Input(duracionJugada[nivel]["segundos"],key="seg",size=(4,5))]
	               ]
	               
		columna2 = [
				[sg.Text("Letra", size=(4,1)), sg.Text("Puntos", size=(6,1)), sg.Text("Cantidad", size=(7,1))], 
				[sg.Text("I", size=(4,1)), sg.Input(letrasD["I"]["puntos"], size=(6,1), key=("I","p")), sg.Input(letrasD["I"]["cant"], size=(6,1), key=("I","c"))],
				[sg.Text("J", size=(4,1)), sg.Input(letrasD["J"]["puntos"], size=(6,1), key=("J","p")), sg.Input(letrasD["J"]["cant"], size=(6,1), key=("J","c"))],
				[sg.Text("K", size=(4,1)), sg.Input(letrasD["K"]["puntos"], size=(6,1), key=("K","p")), sg.Input(letrasD["K"]["cant"], size=(6,1), key=("K","c"))],
				[sg.Text("L", size=(4,1)), sg.Input(letrasD["L"]["puntos"], size=(6,1), key=("L","p")), sg.Input(letrasD["L"]["cant"], size=(6,1), key=("L","c"))],
				[sg.Text("LL", size=(4,1)), sg.Input(letrasD["LL"]["puntos"], size=(6,1), key=("LL","p")), sg.Input(letrasD["LL"]["cant"], size=(6,1), key=("LL","c"))],
				[sg.Text("M", size=(4,1)), sg.Input(letrasD["M"]["puntos"], size=(6,1), key=("M","p")), sg.Input(letrasD["M"]["cant"], size=(6,1), key=("M","c"))],
				[sg.Text("N", size=(4,1)), sg.Input(letrasD["N"]["puntos"], size=(6,1), key=("N","p")), sg.Input(letrasD["N"]["cant"], size=(6,1), key=("N","c"))],
				[sg.Text("Ñ", size=(4,1)), sg.Input(letrasD["Ñ"]["puntos"], size=(6,1), key=("Ñ","p")), sg.Input(letrasD["Ñ"]["cant"], size=(6,1), key=("Ñ","c"))],
				[sg.Text("")],
				[sg.Text("Duración elección palabra")],
				[sg.Text("Hs",size=(4,1)), sg.Text("Min",size=(3,1)),sg.Text("Seg",size=(4,1))],
				[sg.Input(duracionEleccionPalabra[nivel]["horas"],key="ho",size=(4,5)),sg.Input(duracionEleccionPalabra[nivel]["minutos"],key="mi",size=(4,5)), sg.Input(duracionEleccionPalabra[nivel]["segundos"],key="se",size=(4,5))]
	               ]
	               
		columna3 = [
				[sg.Text("Letra", size=(4,1)), sg.Text("Puntos", size=(6,1)), sg.Text("Cantidad", size=(7,1))], 
				[sg.Text("O", size=(4,1)), sg.Input(letrasD["O"]["puntos"], size=(6,1), key=("O","p")), sg.Input(letrasD["O"]["cant"], size=(6,1), key=("O","c"))],
				[sg.Text("P", size=(4,1)), sg.Input(letrasD["P"]["puntos"], size=(6,1), key=("P","p")), sg.Input(letrasD["P"]["cant"], size=(6,1), key=("P","c"))],
				[sg.Text("Q", size=(4,1)), sg.Input(letrasD["Q"]["puntos"], size=(6,1), key=("Q","p")), sg.Input(letrasD["Q"]["cant"], size=(6,1), key=("Q","c"))],
				[sg.Text("R", size=(4,1)), sg.Input(letrasD["R"]["puntos"], size=(6,1), key=("R","p")), sg.Input(letrasD["R"]["cant"], size=(6,1), key=("R","c"))],
				[sg.Text("RR", size=(4,1)), sg.Input(letrasD["RR"]["puntos"], size=(6,1), key=("RR","p")), sg.Input(letrasD["RR"]["cant"], size=(6,1), key=("RR","c"))],
				[sg.Text("S", size=(4,1)), sg.Input(letrasD["S"]["puntos"], size=(6,1), key=("S","p")), sg.Input(letrasD["S"]["cant"], size=(6,1), key=("S","c"))],
				[sg.Text("T", size=(4,1)), sg.Input(letrasD["T"]["puntos"], size=(6,1), key=("T","p")), sg.Input(letrasD["T"]["cant"], size=(6,1), key=("T","c"))],
				[sg.Text("U", size=(4,1)), sg.Input(letrasD["U"]["puntos"], size=(6,1), key=("U","p")), sg.Input(letrasD["U"]["cant"], size=(6,1), key=("U","c"))]
	               ]
	               
		columna4 = [
				[sg.Text("Letra", size=(4,1)), sg.Text("Puntos", size=(6,1)), sg.Text("Cantidad", size=(7,1))], 
				[sg.Text("V", size=(4,1)), sg.Input(letrasD["V"]["puntos"], size=(6,1), key=("V","p")), sg.Input(letrasD["V"]["cant"], size=(6,1), key=("V","c"))],
				[sg.Text("W", size=(4,1)), sg.Input(letrasD["W"]["puntos"], size=(6,1), key=("W","p")), sg.Input(letrasD["W"]["cant"], size=(6,1), key=("W","c"))],
				[sg.Text("X", size=(4,1)), sg.Input(letrasD["X"]["puntos"], size=(6,1), key=("X","p")), sg.Input(letrasD["X"]["cant"], size=(6,1), key=("X","c"))],
				[sg.Text("Y", size=(4,1)), sg.Input(letrasD["Y"]["puntos"], size=(6,1), key=("Y","p")), sg.Input(letrasD["Y"]["cant"], size=(6,1), key=("Y","c"))],
				[sg.Text("Z", size=(4,1)), sg.Input(letrasD["Z"]["puntos"], size=(6,1), key=("Z","p")), sg.Input(letrasD["Z"]["cant"], size=(6,1), key=("Z","c"))]
				  ] 
	               
		columnas_config = [[sg.Text("Puede haber hasta 20 fichas de cada letra. Los puntos pueden tomar valores entre 0 y 50.", text_color="blue")],
				[sg.Column(columna1), sg.Column(columna2), sg.Column(columna3), sg.Column(columna4)],
				[sg.Button("Guardar"), sg.Button("Reset")]
	             ]
	  
		window2 = sg.Window("Configuración").Layout(columnas_config)
	  
		config = True
	  
		while config:
			event2, values2 = window2.Read()
		  
			if event2 is None:
				break
			  
			if event2=="Guardar":
				sin_errores = True
				try:
					duracionJugada["F"]["horas"] = int(values2["hor"])
					duracionJugada["F"]["minutos"] = int(values2["min"])
					duracionJugada["F"]["segundos"] = int(values2["seg"])
				except:
					duracionJugada["F"]["horas"] = duracionJugada_backup["F"]["horas"]
					duracionJugada["F"]["minutos"] = duracionJugada_backup["F"]["minutos"]
					duracionJugada["F"]["segundos"] = duracionJugada_backup["F"]["segundos"]
				try:
					duracionEleccionPalabra["F"]["horas"] = int(values2["ho"])
					duracionEleccionPalabra["F"]["minutos"] = int(values2["mi"])
					duracionEleccionPalabra["F"]["segundos"] = int(values2["se"])
				except:
					duracionEleccionPalabra["F"]["horas"] = duracionEleccionPalabra_backup["F"]["horas"]
					duracionEleccionPalabra["F"]["minutos"] = duracionEleccionPalabra_backup["F"]["minutos"]
					duracionEleccionPalabra["F"]["segundos"] = duracionEleccionPalabra_backup["F"]["segundos"]
				for let in letrasD:
					if int(values2[(let,"c")])>=0 and int(values2[(let,"c")])<=20:
						try:
							letrasD[let]["cant"] = int(values2[(let,"c")])
						except:
							letrasD[let]["cant"] = letras_backup[let]["cant"]
							sin_errores=False
					else:
						sin_errores=False
					  
					if int(values2[(let,"p")])>=0 and int(values2[(let,"p")])<=50:
						try:
							letrasD[let]["puntos"] = int(values2[(let,"p")])
						except:
							letrasD[let]["puntos"] = letras_backup[let]["puntos"]
							sin_errores=False
					else:
						sin_errores=False
				if sin_errores==False:
					sg.popup("Algunos de los valores no se modificaron porque no se ingresaron valores correctos")
			  #-------------------------------------------------------------------------------
			  #Actualizo la lista letras y el diccionario puntos
			  #letras = inicializar_letras(letrasD)
			  #puntos = inicializar_puntos(letrasD)
			  #for i in puntos:
			  #	  puntos[i]=letrasD[i]["puntos"]
			  #print(puntos)
			  #--------------------------------------------------------------------------------------------------
				config=False
				window2.close()
			  
			if event2=="Reset":
				letrasD = copy.deepcopy(letras_backup)
				for let in letrasD:
					window2[(let,"c")].Update(letrasD[let]["cant"])
					window2[(let,"p")].Update(letrasD[let]["puntos"])       

