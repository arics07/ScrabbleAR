import PySimpleGUI as sg
import scrabble

from jugador import jugador
from jugadas import jugadas

def main(args):

  nom=""
  layout=[[sg.Text('Jugador')],[sg.InputText(key='nom')],[sg.Button("Facil",size=(10,2))],[sg.Button("Medio",size=(10,2))],[sg.Button("Dificil",size=(10,2))]]
  window = sg.Window('Jugadas').Layout(layout)
  event, values=window.Read()
  window.finalize()
  jugadorJ = jugador(values["nom"])
  jugadorC = jugador('Computadora')
  window.close()

  #Cantidad de letras
  letras=["A","A","A","A","A","A","A","A","A","A","A","B","B","B","C","C","C","C",
    "D","D","D","D","E","E","E","E","E","E","E","E","E","E","E","F","F","G","G","H","H",
    "I","I","J","J","K","L","L","L","L","LL","M","M","M","N","N","N","N","N",
    "O","O","O","O","O","O","O","O","P","P","Q","R","R","R","R","RR","S","S","S","S","S","S","S",
    "T","T","T","T","U","U","U","U","U","U","V","V","W","X","Y","Z"]

  #DICCIONARIO QUE RELACIONA LETRA CON SU VALOR 
  puntos={"A":1,"B":3,"C":2,"D":2,"E":1,"F": 4,"G":2,"H":4,"I":1,"J":6,"K":8,"L":1,"LL":8,"M":3,
    "N":1,"Ñ":8,"O":1,"P":3,"Q":8,"R":1,"RR":8,"S":1,"T":1,"U":1,"V":4,"W":8,"X":8,"Y":4,"Z":10}
  
  if event == "Facil":
    jugada=jugadas("20-06-07","F",120,jugadorJ,jugadorC,"J",letras,puntos)  
    jugadorJ.elijoL(letras)
    jugadorC.elijoL(letras)
    scrabble.main(jugada)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
