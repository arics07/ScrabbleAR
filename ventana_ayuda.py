import PySimpleGUI as sg

def ayuda_al_jugador():
	
	sg.theme("GreenTan")
	
	layout=[
			[sg.Text("Información del Tablero:", font=("Helvetica",14), background_color="#F0F553")],
			[sg.Button("TP", size=(2,1), button_color=("black", "#C91A4F")), sg.Text("Triplica Palabra", font=("Helvetica", 11)), sg.Text("", size=(2,1)), sg.Button("DP", size=(2,1), button_color=("black", "#F4963E")), sg.Text("Duplica Palabra", font=("Helvetica", 12)), sg.Text("", size=(2,1)), sg.Button("TL", size=(2,1), button_color=("black", "#1A4C86")), sg.Text("Triplica Letra", font=("Helvetica", 13)), sg.Text("", size=(2,1)), sg.Button("DL", size=(2,1), button_color=("black", "#4893E9")), sg.Text("Duplica Letra", font=("Helvetica", 13)), sg.Text("", size=(2,1)), sg.Button("x", size=(2,1), button_color=("black", "#F00F0F")), sg.Text("Descuenta*", font=("Helvetica", 13))],
			[sg.Text("* Cuando hay una letra en un casillero de descuento (x), se descuenta el valor de esa letra.", font=("Helvetica", 11))],
			[sg.Text("Poner una palabra en el Tablero:", font=("Helvetica",14), background_color="#F0F553")],
			[sg.Text("Clickear una letra del atril y luego clickear el casillero del tablero en donde se quiere ubicar esa letra.", font=("Helvetica",11))],
			[sg.Text("Para jugar una palabra en el tablero, se debe repetir este procedimiento con cada una de las letras que forman la palabra. La dirección ", font=("Helvetica",11))],
			[sg.Text("debe ser HORIZONTAL o VERTICAL. Una vez ubicadas todas las letras de la palabra, clickear el botón 'Insertar Palabra'.", font=("Helvetica",11)), sg.Button('Insertar Palabra', size=(12, 1))],
			[sg.Text("Cambiar las fichas del atril:", font=("Helvetica",14), background_color="#F0F553")],
			[sg.Text("Se pueden cambiar las 7 fichas de atril, hasta 3 veces durante la partida, clickeando el botón 'Cambio Letras'.", font=("Helvetica",11)), sg.Button("Cambio\nletras", size=(6, 2))],
			[sg.Text("Cada vez que el jugador cambia su atril, pierde su turno.", font=("Helvetica",11))],
			[sg.Text("Pasar el turno:", font=("Helvetica",15), background_color="#F0F553")],
			[sg.Text("El jugador puede elegir pasar su turno tantas veces como quiera durante la partida, clickeando el botón 'Pasar'.", font=("Helvetica",11)), sg.Button('Pasar', size=(9, 1))],
			[sg.Text("")],
			[sg.Button("Salir de Ayuda", button_color=("#FFFFFF","#000000"), font=("Helvetica", 11), size=(12,2), key="salir")]
		   ]
	   
	windowAyuda = sg.Window("Ayuda", layout)

	while True:
		
		event, values = windowAyuda.read()
	
		if event is None:
			break
			
		if event =="salir":
			windowAyuda.close()

ayuda_al_jugador()
