import PySimpleGUI as sg
import scrabble
import datetime
import pickle

from jugador import jugador
from jugadas import jugadas

nom=""
layout=[[sg.Text('Jugador')],[sg.InputText(key='nom',size=(29,3))],
  [sg.Text('Nivel')],[sg.InputText(key='nivel',size=(3,2)),sg.Text('F=Facil M=Medio D=Dificil')],
  [sg.Button("Comenzar",size=(10,2))]]
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
         
        

