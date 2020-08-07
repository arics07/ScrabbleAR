import PySimpleGUI as sg
import math 
import ScrabbleAR as menu

def programa_principal(jugadorJ,jugadorC,puntosLetras):
	puntosLetrasCompu=0
	puntosLetrasJugador=0
	nombreGanador=""
	compu=(jugadorC.get_nombre()).upper()
	jugador=(jugadorJ.get_nombre()).upper()
	atrilCompu=jugadorC.get_atril()
	atrilJugador=jugadorJ.get_atril()
	
	for letra in atrilCompu:
		puntosLetrasCompu = puntosLetrasCompu + puntosLetras.get(letra)
	
	for letra in atrilJugador:
		puntosLetrasJugador = puntosLetrasJugador + puntosLetras.get(letra)
	
	atrilJugador = str(','.join(jugadorJ.get_atril()))
	atrilCompu = str(','.join(jugadorC.get_atril()))
	

	
	puntosFinalesCompu = jugadorC.get_puntaje() - puntosLetrasCompu
	puntosFinalesJugador = jugadorJ.get_puntaje() - puntosLetrasJugador
	
	if puntosFinalesCompu > puntosFinalesJugador:
		nombreGanador = compu
	else:
		nombreGanador = jugador
	
	
	#columna5=[
	        # [sg.Graph(canvas_size=(300, 10), graph_bottom_left=(0,0), graph_top_right=(300, 10), key='graph2')]
	         #]
	#columna6=[
	        # [sg.Graph(canvas_size=(300, 10), graph_bottom_left=(0,0), graph_top_right=(300, 10), key='graph3')]
	        # ]
	columna1=[
	         [sg.Text("")],
	         [sg.Text("FICHAS SIN JUGAR:",justification="center",size=(30,1))],
	         [sg.Text(atrilJugador,justification="center",size=(30,1))],
	         [sg.Text("")],
	         [sg.Text("PUNTOS ACTUALES:",justification="center",size=(30,1)), sg.Text(jugadorJ.get_puntaje(),background_color="#FFFFFF")], 
	         [sg.Text("         -",justification="left")],
	         [sg.Text("PUNTOS FICHAS:",justification="center",size=(30,1)), sg.Text(puntosLetrasJugador,background_color="#FFFFFF")],
	         [sg.Text("              ________________________________")],
	         [sg.Text("PUNTOS FINALES:",justification="center",size=(30,1)), sg.Text(puntosFinalesJugador,background_color="#FFFFFF")], 
			 ]
	columna2=[
	         [sg.Text("")],
	         [sg.Text("FICHAS SIN JUGAR:",justification="center",size=(30,1))],
	         [sg.Text(atrilCompu,justification="center",size=(30,1))],
	         [sg.Text("")],
	         [sg.Text("PUNTOS ACTUALES:",justification="center",size=(30,1)), sg.Text(jugadorC.get_puntaje(),background_color="#FFFFFF")], 
	         [sg.Text("         -",justification="left")],
	         [sg.Text("PUNTOS FICHAS:",justification="center",size=(30,1)), sg.Text(puntosLetrasCompu,background_color="#FFFFFF")],
	         [sg.Text("              ________________________________")],
	         [sg.Text("PUNTOS FINALES:",justification="center",size=(30,1)), sg.Text(puntosFinalesCompu,background_color="#FFFFFF")],
			 ]
	columna3=[
	         #[sg.Text("GANADOR/GANADORA", justification="center",text_color="white", size=(75,1),font=(30))],
	         [sg.Text("",size=(1,1)),sg.Text("",size=(1,1)),sg.Text("",size=(1,1)),sg.Text("",size=(1,1)),sg.Text("",size=(1,1)),sg.Text("",size=(1,1)),sg.Text("",size=(1,1)),sg.Text("",size=(1,1)),sg.Image("img/ganar.png")],
	         [sg.Text(nombreGanador,justification="center",text_color="black", size=(75,1),key="nomJugador",font=(30))]
	         ]
	columna4=[
	         [sg.Graph(canvas_size=(10, 250), graph_bottom_left=(0,0), graph_top_right=(10, 250), key='graph')]
	         ]
	layout=[
	       [sg.Column(columna3)],
	       [sg.Text("")],
	       #[sg.Text("RESULTADOS",size=(75,1), justification="center",font=(20))],
	       [sg.Text("",size=(1,1)),sg.Text("",size=(1,1)),sg.Text("",size=(1,1)),sg.Text("",size=(1,1)),sg.Text("",size=(1,1)),sg.Text("",size=(1,1)),sg.Image("img/resultados.png")],
	       [sg.Text("")],
	       [sg.Text("",size=(1,1)),sg.Text("",size=(1,1)),sg.Text(jugador,justification="center",size=(30,1),background_color ="#AA6391", text_color="white"),sg.Text("",size=(1,1)),sg.Text("",size=(1,1)),sg.Text("",size=(1,1)),sg.Text("",size=(1,1)),sg.Text("",size=(1,1)), sg.Text(compu,justification="center",size=(30,1),background_color ="#AA6391", text_color="white")],
	       [sg.Text(" ", size=(1, 1)),sg.Column(columna1),sg.Text(""),sg.Text(""),sg.Column(columna4),sg.Column(columna2),sg.Text("")],
	       [sg.Text("")],
	       [sg.Button("Volver al menú",button_color=("white","#7C766E"), key="volver"), sg.Button("Salir",button_color=("white","#7C766E"), key="salir")]
	       ]
	window = sg.Window("::::::::: FIN DEL JUEGO :::::::::", layout)
	window.Finalize()
	
	graph = window['graph']
	#graph2 = window['graph2']
	#graph3 = window['graph3']
	
	
	graph.DrawLine((5,0),(5,300), color='black')
	#graph2.DrawLine((0,5),(300,5), color='black')
	#graph3.DrawLine((0,5),(300,5), color='black')

	
	while True:
		event, values = window.read()
	
		if event == "salir":
			break
		
		if event == "volver":
			window.close()
			menu.main()
		
		window.close()


