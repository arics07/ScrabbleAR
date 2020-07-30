import PySimpleGUI as sg
import copy

def programa_principal(valorDefCombo,datosSlierRango,datosSliderValorDefault,nivel,letrasD,duracionJugada,duracionEleccionPalabra,letras_backup,duracionJugada_backup,duracionEleccionPalabra_backup,datosSlierRango2,datosSliderValorDefault2,valorDefCombo2):
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
				[sg.Combo(["Horas", "Minutos","Segundos"],default_value=valorDefCombo, key="combo",enable_events=True)],
				[sg.Slider(range=(datosSlierRango),default_value=datosSliderValorDefault,size=(20,15),orientation='horizontal',key="slider",enable_events=True)]
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
				[sg.Combo(["Minutos","Segundos"],default_value=valorDefCombo2, key="combo2",enable_events=True)],
				[sg.Slider(range=(datosSlierRango2),default_value=datosSliderValorDefault2,size=(20,15),orientation='horizontal',key="slider2",enable_events=True)]
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
	  
	window = sg.Window("Configuración").Layout(columnas_config)
	  
	config = True
	
	  
	while config:
		event, values = window.Read()
	
		if values["combo"] == "Horas":
			window.FindElement("slider").Update(range = duracionJugada[nivel]["horas"]["rango"])
				
		if values["combo"] == "Minutos":
			window.FindElement("slider").Update(range = duracionJugada[nivel]["minutos"]["rango"])
			
		if values["combo2"] == "Minutos":
			window.FindElement("slider2").Update(range = duracionEleccionPalabra[nivel]["minutos"]["rango"])
				
		if values["combo"] == "Segundos":
			window.FindElement("slider").Update(range = duracionJugada[nivel]["segundos"]["rango"])
			
		if values["combo2"] == "Segundos":
			window.FindElement("slider2").Update(range = duracionEleccionPalabra[nivel]["segundos"]["rango"])
				
		  
		if event is None:
			return nivel,letrasD,duracionJugada,duracionEleccionPalabra
			break
			  
		if event=="Guardar":
			sin_errores = True
			
			try:
				if values["combo"] == "Horas":
					duracionJugada[nivel]["horas"]["cant"] = int(values["slider"])
					duracionJugada[nivel]["minutos"]["cant"] = 0
					duracionJugada[nivel]["segundos"]["cant"] = 0
					
				if values["combo"] == "Minutos":
					duracionJugada[nivel]["minutos"]["cant"] = int(values["slider"])
					duracionJugada[nivel]["horas"]["cant"] = 0
					duracionJugada[nivel]["segundos"]["cant"] = 0
					
				if values["combo"] == "Segundos":
					duracionJugada[nivel]["segundos"]["cant"] = int(values["slider"])
					duracionJugada[nivel]["horas"]["cant"] = 0
					duracionJugada[nivel]["minutos"]["cant"] = 0
			except:
				duracionJugada[nivel]["horas"]["cant"] = duracionJugada_backup[nivel]["horas"]["cant"]
				duracionJugada[nivel]["minutos"]["cant"] = duracionJugada_backup[nivel]["minutos"]["cant"]
				duracionJugada[nivel]["segundos"]["cant"] = duracionJugada_backup[nivel]["segundos"]["cant"]
			#------------------------------------------------------------------------------------------------------
				
			try:
				if values["combo2"] == "Minutos":
					duracionEleccionPalabra[nivel]["minutos"]["cant"] = int(values["slider2"])
					duracionEleccionPalabra[nivel]["segundos"]["cant"] = 0
					
				if values["combo2"] == "Segundos":
					duracionEleccionPalabra[nivel]["segundos"]["cant"] = int(values["slider2"])
					duracionEleccionPalabra[nivel]["minutos"]["cant"] = 0
				
			except:
				duracionEleccionPalabra[nivel]["minutos"]["cant"] = duracionEleccionPalabra_backup[nivel]["minutos"]["cant"]
				duracionEleccionPalabra[nivel]["segundos"]["cant"] = duracionEleccionPalabra_backup[nivel]["segundos"]["cant"]
			
			#--------------------------------------------------------------------------------------------------------------------
			
			for let in letrasD:
				if int(values[(let,"c")])>=0 and int(values[(let,"c")])<=20:
					try:
						letrasD[let]["cant"] = int(values[(let,"c")])
					except:
						letrasD[let]["cant"] = letras_backup[let]["cant"]
						sin_errores=False
				else:
					sin_errores=False
					  
				if int(values[(let,"p")])>=0 and int(values[(let,"p")])<=50:
					try:
						letrasD[let]["puntos"] = int(values[(let,"p")])
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
			print(duracionEleccionPalabra,duracionJugada)
			config=False
			window.close()
			return nivel,letrasD,duracionJugada,duracionEleccionPalabra
			  
		if event=="Reset":
			letrasD = copy.deepcopy(letras_backup)
			duracionJugada = copy.deepcopy(duracionJugada_backup)
			duracionEleccionPalabra =copy.deepcopy(duracionEleccionPalabra_backup)
			
			window.FindElement("slider").Update(range = duracionJugada[nivel]["horas"]["rango"])
			window.FindElement("slider2").Update(range = duracionEleccionPalabra[nivel]["minutos"]["rango"])
			
			#if nivel == "F":
				#valorDefCombo = "Horas"
				#window["combo"].Update(default_value=valorDefCombo)
				
			#if nivel == "M":
				#valorDefCombo2 = "Minutos"
				#window["combo2"].Update(default_value=valorDefCombo2)
				#valorDefCombo = "Minutos"
				#window["combo"].Update(default_value=valorDefCombo)
			
			#if nivel == "D":
				#valorDefCombo2 = "Minutos"
				#window["combo2"].Update(default_value=valorDefCombo2)
				#valorDefCombo = "Minutos"
				#window["combo"].Update(default_value=valorDefCombo)

			
			for let in letrasD:
				window[(let,"c")].Update(letrasD[let]["cant"])
				window[(let,"p")].Update(letrasD[let]["puntos"]) 
			      



