import PySimpleGUI as sg
import scrabble
import datetime
import pickle
import copy
from jugada_computadora import cargar_tuplas_desocupadas, desocupadas

from jugador import jugador
from jugadas import jugadas

nom=""
layout=[[sg.Text('Jugador')],[sg.InputText(key='nom',size=(29,3))],
  [sg.Text('Nivel')],[sg.InputText(key='nivel',size=(3,2)),sg.Text('F=Facil M=Medio D=Dificil')],
  [sg.Button("Comenzar",size=(10,2)), sg.Button("Configurar", size=(10,2))]]
window = sg.Window('Ingreso Juego').Layout(layout)

#Cantidad de letras 
letras=["A","A","A","A","A","A","A","A","A","A","A","B","B","B","C","C","C","C",
  "D","D","D","D","E","E","E","E","E","E","E","E","E","E","E","F","F","G","G","H","H",
  "I","I","J","J","K","L","L","L","L","LL","M","M","M","N","N","N","N","N",
  "O","O","O","O","O","O","O","O","P","P","Q","R","R","R","R","RR","S","S","S","S","S","S","S",
  "T","T","T","T","U","U","U","U","U","U","V","V","W","X","Y","Z"]

#DICCIONARIO QUE RELACIONA LETRA CON SU VALOR 
puntos={"A":1,"B":3,"C":2,"D":2,"E":1,"F": 4,"G":2,"H":4,"I":1,"J":6,"K":8,"L":1,"LL":8,"M":3,
  "N":1,"Ñ":8,"O":1,"P":3,"Q":8,"R":1,"RR":8,"S":1,"T":1,"U":1,"V":4,"W":8,"X":8,"Y":4,"Z":10}
  
letrasD = { "A": {"cant":11,"puntos":1},"B":{"cant":3,"puntos":3},"C":{"cant":4,"puntos":2},"D":{"cant":4,"puntos":2},"E":{"cant":11,"puntos":1},"F":{"cant":2,"puntos":4},"G":{"cant":2,"puntos":2},
  "H":{"cant":2,"puntos":4},"I":{"cant":2,"puntos":1},"J":{"cant":2,"puntos":6},"K":{"cant":1,"puntos":8},"L":{"cant":4,"puntos":1},"LL":{"cant":1,"puntos":8},"M":{"cant":3,"puntos":3},"N":{"cant":5,"puntos":1},"Ñ":{"cant":1,"puntos":8},
  "O":{"cant":4,"puntos":1},"P":{"cant":2,"puntos":3},"Q":{"cant":1,"puntos":8},"R":{"cant":4,"puntos":1},"RR":{"cant":1,"puntos":8},"S":{"cant":7,"puntos":1},"T":{"cant":4,"puntos":1},"U":{"cant":6,"puntos":4},"V":{"cant":2,"puntos":4},
  "W":{"cant":1,"puntos":8},"X":{"cant":1,"puntos":8},"Y":{"cant":1,"puntos":4},"Z":{"cant":1,"puntos":10}}

letras_backup = copy.deepcopy(letrasD)
  
while True: 
  event, values=window.Read() 
  
  if event == None:
	  break 
  if event == "Comenzar":  
    if values["nom"] == "":
      sg.Popup("Debe ingresar un nombre")
    else:
      if not (values["nivel"].upper() == "F" or values["nivel"].upper() == "M" or values["nivel"].upper() == "D"):
        sg.Popup("Nivel F=Facil M=Medio D=Dificil")
      else:  
        window.close()   
        jugadorJ = jugador(values["nom"])
        jugadorC = jugador('Computadora')
        cargar_tuplas_desocupadas(desocupadas)	
        
        if values["nivel"].upper() == "F":
          jugada=jugadas(datetime.datetime.now(),"F",120,jugadorJ,jugadorC,"J",letras,puntos)  
        if values["nivel"].upper() == "M":
          jugada=jugadas(datetime.datetime.now(),"M",60,jugadorJ,jugadorC,"J",letras,puntos)  
        if values["nivel"].upper() == "D":
          jugada=jugadas(datetime.datetime.now(),"D",30,jugadorJ,jugadorC,"J",letras,puntos)  
  
        
        jugadorJ.elijoL(letras)
        jugadorC.elijoL(letras)
        try: 
          with open('topten.pkl', 'rb') as f:
            topten=dict(pickle.load(f))
        except:
          topten={}  
          print(topten) 
        jugada.set_topten(topten)
        scrabble.main(jugada)
        break
        
  if event == "Configurar":
	  columna1 = [
				[sg.Text("Letra", size=(4,1)), sg.Text("Puntos", size=(5,1)), sg.Text("Cantidad", size=(6,1))], 
				[sg.Text("A", size=(4,1)), sg.Input(letrasD["A"]["puntos"], size=(6,1), key=("A","p")), sg.Input(letrasD["A"]["cant"], size=(6,1), key=("A","c"))],
				[sg.Text("B", size=(4,1)), sg.Input(letrasD["B"]["puntos"], size=(6,1), key=("B","p")), sg.Input(letrasD["B"]["cant"], size=(6,1), key=("B","c"))],
				[sg.Text("C", size=(4,1)), sg.Input(letrasD["C"]["puntos"], size=(6,1), key=("C","p")), sg.Input(letrasD["C"]["cant"], size=(6,1), key=("C","c"))],
				[sg.Text("D", size=(4,1)), sg.Input(letrasD["D"]["puntos"], size=(6,1), key=("D","p")), sg.Input(letrasD["D"]["cant"], size=(6,1), key=("D","c"))],
				[sg.Text("E", size=(4,1)), sg.Input(letrasD["E"]["puntos"], size=(6,1), key=("E","p")), sg.Input(letrasD["E"]["cant"], size=(6,1), key=("E","c"))],
				[sg.Text("F", size=(4,1)), sg.Input(letrasD["F"]["puntos"], size=(6,1), key=("F","p")), sg.Input(letrasD["F"]["cant"], size=(6,1), key=("F","c"))],
				[sg.Text("G", size=(4,1)), sg.Input(letrasD["G"]["puntos"], size=(6,1), key=("G","p")), sg.Input(letrasD["G"]["cant"], size=(6,1), key=("G","c"))],
				[sg.Text("H", size=(4,1)), sg.Input(letrasD["H"]["puntos"], size=(6,1), key=("H","p")), sg.Input(letrasD["H"]["cant"], size=(6,1), key=("H","c"))]
	               ]
	               
	  columna2 = [
				[sg.Text("Letra", size=(4,1)), sg.Text("Puntos", size=(5,1)), sg.Text("Cantidad", size=(6,1))], 
				[sg.Text("I", size=(4,1)), sg.Input(letrasD["I"]["puntos"], size=(6,1), key=("I","p")), sg.Input(letrasD["I"]["cant"], size=(6,1), key=("I","c"))],
				[sg.Text("J", size=(4,1)), sg.Input(letrasD["J"]["puntos"], size=(6,1), key=("J","p")), sg.Input(letrasD["J"]["cant"], size=(6,1), key=("J","c"))],
				[sg.Text("K", size=(4,1)), sg.Input(letrasD["K"]["puntos"], size=(6,1), key=("K","p")), sg.Input(letrasD["K"]["cant"], size=(6,1), key=("K","c"))],
				[sg.Text("L", size=(4,1)), sg.Input(letrasD["L"]["puntos"], size=(6,1), key=("L","p")), sg.Input(letrasD["L"]["cant"], size=(6,1), key=("L","c"))],
				[sg.Text("LL", size=(4,1)), sg.Input(letrasD["LL"]["puntos"], size=(6,1), key=("LL","p")), sg.Input(letrasD["LL"]["cant"], size=(6,1), key=("LL","c"))],
				[sg.Text("M", size=(4,1)), sg.Input(letrasD["M"]["puntos"], size=(6,1), key=("M","p")), sg.Input(letrasD["M"]["cant"], size=(6,1), key=("M","c"))],
				[sg.Text("N", size=(4,1)), sg.Input(letrasD["N"]["puntos"], size=(6,1), key=("N","p")), sg.Input(letrasD["N"]["cant"], size=(6,1), key=("N","c"))],
				[sg.Text("Ñ", size=(4,1)), sg.Input(letrasD["Ñ"]["puntos"], size=(6,1), key=("Ñ","p")), sg.Input(letrasD["Ñ"]["cant"], size=(6,1), key=("Ñ","c"))]
	               ]
	               
	  columna3 = [
				[sg.Text("Letra", size=(4,1)), sg.Text("Puntos", size=(5,1)), sg.Text("Cantidad", size=(6,1))], 
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
				[sg.Text("Letra", size=(4,1)), sg.Text("Puntos", size=(5,1)), sg.Text("Cantidad", size=(6,1))], 
				[sg.Text("V", size=(4,1)), sg.Input(letrasD["V"]["puntos"], size=(6,1), key=("V","p")), sg.Input(letrasD["V"]["cant"], size=(6,1), key=("V","c"))],
				[sg.Text("W", size=(4,1)), sg.Input(letrasD["W"]["puntos"], size=(6,1), key=("W","p")), sg.Input(letrasD["W"]["cant"], size=(6,1), key=("W","c"))],
				[sg.Text("X", size=(4,1)), sg.Input(letrasD["X"]["puntos"], size=(6,1), key=("X","p")), sg.Input(letrasD["X"]["cant"], size=(6,1), key=("X","c"))],
				[sg.Text("Y", size=(4,1)), sg.Input(letrasD["Y"]["puntos"], size=(6,1), key=("Y","p")), sg.Input(letrasD["Y"]["cant"], size=(6,1), key=("Y","c"))],
				[sg.Text("Z", size=(4,1)), sg.Input(letrasD["Z"]["puntos"], size=(6,1), key=("Z","p")), sg.Input(letrasD["Z"]["cant"], size=(6,1), key=("Z","c"))]
				  ] 
	               
	  columnas_config = [[sg.Column(columna1), sg.Column(columna2), sg.Column(columna3), sg.Column(columna4)],
				[sg.Button("Guardar"), sg.Button("Reset")]
	             ]
	  
	  window2 = sg.Window("Configuración").Layout(columnas_config)
	  
	  config = True
	  
	  while config:
		  event2, values2 = window2.Read()
		  
		  if event2=="Guardar":
			  sin_errores = True
			  for let in letrasD:
				  try:
					  letrasD[let]["cant"] = int(values2[(let,"c")])
				  except:
					  letrasD[let]["cant"] = letras_backup[let]["cant"]
					  sin_errores=False
				  try:
					  letrasD[let]["puntos"] = int(values2[(let,"p")])
				  except:
					  letrasD[let]["puntos"] = letras_backup[let]["puntos"]
					  sin_errores=False
			  if sin_errores==False:
				  sg.popup("Algunos de los valores no se modificaron porque no se ingresaron números enteros")
			  #la parte encerrada en las lineas se va a sacar después--------------------------------------------
			  #Actualizo la lista letras y el diccionario puntos
			  letras = []
			  for lett in letrasD:
				  for cant in range(letrasD[lett]["cant"]):
					  letras.append(lett)
			  print(letras)
			  for i in puntos:
				  puntos[i]=letrasD[i]["puntos"]
			  print(puntos)
			  #--------------------------------------------------------------------------------------------------
			  config=False
			  window2.close()
			  
		  if event2=="Reset":
			  letrasD = copy.deepcopy(letras_backup)
			  for let in letrasD:
				  window2[(let,"c")].Update(letrasD[let]["cant"])
				  window2[(let,"p")].Update(letrasD[let]["puntos"])       

