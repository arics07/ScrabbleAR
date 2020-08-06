import PySimpleGUI as sg
import copy

def programa_principal(nivel,letrasD,duracionJugada,duracionEleccionPalabra,letras_backup,duracionJugada_backup,duracionEleccionPalabra_backup):
	
	interv_cant = list(range(1,51))
	interv_punt = list(range(1,21))
	
	if nivel == "F":
		num = 0
	else:
		num = 1
	
	columna1 = [
				[sg.Text("Letra", size=(4,1)), sg.Text("Puntos", size=(6,1)), sg.Text("Cantidad", size=(7,1))], 
				[sg.Text("A", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["A"]["puntos"], size=(4,1), key=("A","p")), sg.Combo(interv_punt, default_value=letrasD["A"]["cant"], size=(4,1), key=("A","c"))],
				[sg.Text("B", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["B"]["puntos"], size=(4,1), key=("B","p")), sg.Combo(interv_punt, default_value=letrasD["B"]["cant"], size=(4,1), key=("B","c"))],
				[sg.Text("C", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["C"]["puntos"], size=(4,1), key=("C","p")), sg.Combo(interv_punt, default_value=letrasD["C"]["cant"], size=(4,1), key=("C","c"))],
				[sg.Text("D", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["D"]["puntos"], size=(4,1), key=("D","p")), sg.Combo(interv_punt, default_value=letrasD["D"]["cant"], size=(4,1), key=("D","c"))],
				[sg.Text("E", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["E"]["puntos"], size=(4,1), key=("E","p")), sg.Combo(interv_punt, default_value=letrasD["E"]["cant"], size=(4,1), key=("E","c"))],
				[sg.Text("F", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["F"]["puntos"], size=(4,1), key=("F","p")), sg.Combo(interv_punt, default_value=letrasD["F"]["cant"], size=(4,1), key=("F","c"))],
				[sg.Text("G", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["G"]["puntos"], size=(4,1), key=("G","p")), sg.Combo(interv_punt, default_value=letrasD["G"]["cant"], size=(4,1), key=("G","c"))],
				[sg.Text("H", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["H"]["puntos"], size=(4,1), key=("H","p")), sg.Combo(interv_punt, default_value=letrasD["H"]["cant"], size=(4,1), key=("H","c"))],
				[sg.Text("")],
				[sg.Text("Duración jugada")],
				[sg.Combo(["Horas", "Minutos","Segundos"],default_value=(list(duracionJugada[nivel].keys())[num]).capitalize(), key="combo",enable_events=True)],
				[sg.Slider(range=(duracionJugada[nivel][list(duracionJugada[nivel].keys())[num]]["rango"]),default_value=duracionJugada[nivel][list(duracionJugada[nivel].keys())[num]]["cant"],size=(20,15),orientation='horizontal',key="slider",enable_events=True)]
				]
	               
	columna2 = [
				[sg.Text("Letra", size=(4,1)), sg.Text("Puntos", size=(6,1)), sg.Text("Cantidad", size=(7,1))], 
				[sg.Text("I", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["I"]["puntos"], size=(4,1), key=("I","p")), sg.Combo(interv_punt, default_value=letrasD["I"]["cant"], size=(4,1), key=("I","c"))],
				[sg.Text("J", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["J"]["puntos"], size=(4,1), key=("J","p")), sg.Combo(interv_punt, default_value=letrasD["J"]["cant"], size=(4,1), key=("J","c"))],
				[sg.Text("K", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["K"]["puntos"], size=(4,1), key=("K","p")), sg.Combo(interv_punt, default_value=letrasD["K"]["cant"], size=(4,1), key=("K","c"))],
				[sg.Text("L", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["L"]["puntos"], size=(4,1), key=("L","p")), sg.Combo(interv_punt, default_value=letrasD["L"]["cant"], size=(4,1), key=("L","c"))],
				[sg.Text("LL", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["LL"]["puntos"], size=(4,1), key=("LL","p")), sg.Combo(interv_punt, default_value=letrasD["LL"]["cant"], size=(4,1), key=("LL","c"))],
				[sg.Text("M", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["M"]["puntos"], size=(4,1), key=("M","p")), sg.Combo(interv_punt, default_value=letrasD["M"]["cant"], size=(4,1), key=("M","c"))],
				[sg.Text("N", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["N"]["puntos"], size=(4,1), key=("N","p")), sg.Combo(interv_punt, default_value=letrasD["N"]["cant"], size=(4,1), key=("N","c"))],
				[sg.Text("Ñ", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["Ñ"]["puntos"], size=(4,1), key=("Ñ","p")), sg.Combo(interv_punt, default_value=letrasD["Ñ"]["cant"], size=(4,1), key=("Ñ","c"))],
				[sg.Text("")],
				[sg.Text("Duración elección palabra")],
				[sg.Combo(["Minutos","Segundos"],default_value=(list(duracionEleccionPalabra[nivel].keys())[0]).capitalize(), key="combo2",enable_events=True)],
				[sg.Slider(range=(duracionEleccionPalabra[nivel]["minutos"]["rango"]),default_value=duracionEleccionPalabra[nivel]["minutos"]["cant"],size=(20,15),orientation='horizontal',key="slider2",enable_events=True)]
				]
	               
	columna3 = [
				[sg.Text("Letra", size=(4,1)), sg.Text("Puntos", size=(6,1)), sg.Text("Cantidad", size=(7,1))], 
				[sg.Text("O", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["O"]["puntos"], size=(4,1), key=("O","p")), sg.Combo(interv_punt, default_value=letrasD["O"]["cant"], size=(4,1), key=("O","c"))],
				[sg.Text("P", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["P"]["puntos"], size=(4,1), key=("P","p")), sg.Combo(interv_punt, default_value=letrasD["P"]["cant"], size=(4,1), key=("P","c"))],
				[sg.Text("Q", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["Q"]["puntos"], size=(4,1), key=("Q","p")), sg.Combo(interv_punt, default_value=letrasD["Q"]["cant"], size=(4,1), key=("Q","c"))],
				[sg.Text("R", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["R"]["puntos"], size=(4,1), key=("R","p")), sg.Combo(interv_punt, default_value=letrasD["R"]["cant"], size=(4,1), key=("R","c"))],
				[sg.Text("RR", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["RR"]["puntos"], size=(4,1), key=("RR","p")), sg.Combo(interv_punt, default_value=letrasD["RR"]["cant"], size=(4,1), key=("RR","c"))],
				[sg.Text("S", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["S"]["puntos"], size=(4,1), key=("S","p")), sg.Combo(interv_punt, default_value=letrasD["S"]["cant"], size=(4,1), key=("S","c"))],
				[sg.Text("T", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["T"]["puntos"], size=(4,1), key=("T","p")), sg.Combo(interv_punt, default_value=letrasD["T"]["cant"], size=(4,1), key=("T","c"))],
				[sg.Text("U", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["U"]["puntos"], size=(4,1), key=("U","p")), sg.Combo(interv_punt, default_value=letrasD["U"]["cant"], size=(4,1), key=("U","c"))]
				]
	               
	columna4 = [
				[sg.Text("Letra", size=(4,1)), sg.Text("Puntos", size=(6,1)), sg.Text("Cantidad", size=(7,1))], 
				[sg.Text("V", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["V"]["puntos"], size=(4,1), key=("V","p")), sg.Combo(interv_punt, default_value=letrasD["V"]["cant"], size=(4,1), key=("V","c"))],
				[sg.Text("W", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["W"]["puntos"], size=(4,1), key=("W","p")), sg.Combo(interv_punt, default_value=letrasD["W"]["cant"], size=(4,1), key=("W","c"))],
				[sg.Text("X", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["X"]["puntos"], size=(4,1), key=("X","p")), sg.Combo(interv_punt, default_value=letrasD["X"]["cant"], size=(4,1), key=("X","c"))],
				[sg.Text("Y", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["Y"]["puntos"], size=(4,1), key=("Y","p")), sg.Combo(interv_punt, default_value=letrasD["Y"]["cant"], size=(4,1), key=("Y","c"))],
				[sg.Text("Z", size=(4,1)), sg.Combo(interv_cant, default_value=letrasD["Z"]["puntos"], size=(4,1), key=("Z","p")), sg.Combo(interv_punt, default_value=letrasD["Z"]["cant"], size=(4,1), key=("Z","c"))]
				  ] 
	               
	columnas_config = [[sg.Text("Puede haber hasta 20 fichas de cada letra. Los puntos pueden tomar valores entre 0 y 50.", text_color="blue")],
				[sg.Column(columna1), sg.Column(columna2), sg.Column(columna3), sg.Column(columna4)],
				[sg.Button("Guardar"), sg.Button("Reset")]
				]
	  
	window = sg.Window("Configuración").Layout(columnas_config)
	  
	config = True
	
	  
	while config:
		event, values = window.Read()
		#pos = list(duracionJugada[nivel].keys())
		
		#print ("combooo1  ", values["combo"], "  combooo2  ", values["combo2"],"  pooos ", pos[0])
	
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
				try:
					if int(values[(let,"c")])>0 and int(values[(let,"c")])<=20:
						letrasD[let]["cant"] = int(values[(let,"c")])
					else:
						sin_errores=False
				except:
					letrasD[let]["cant"] = letras_backup[let]["cant"]
					sin_errores=False
				
				try:
					if int(values[(let,"p")])>0 and int(values[(let,"p")])<=50:
						letrasD[let]["puntos"] = int(values[(let,"p")])
					else:
						sin_errores=False
				except:
					letrasD[let]["puntos"] = letras_backup[let]["puntos"]
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
			
			if nivel == "F":
				window["slider"].Update(duracionJugada[nivel]["horas"]["cant"])
				window["slider2"].Update(duracionEleccionPalabra[nivel]["minutos"]["cant"])
				window["slider"].Update(duracionJugada[nivel]["horas"]["rango"])
				window["slider2"].Update(duracionEleccionPalabra[nivel]["minutos"]["rango"])
				window["combo"].Update((list(duracionJugada[nivel].keys())[num]).capitalize())
				window["combo2"].Update((list(duracionEleccionPalabra[nivel].keys())[num]).capitalize())
			
			if nivel == "M" or nivel == "D":
				window["slider"].Update(duracionJugada[nivel]["minutos"]["cant"])
				window["slider2"].Update(duracionEleccionPalabra[nivel]["minutos"]["cant"])
				window["slider"].Update(duracionJugada[nivel]["minutos"]["rango"])
				window["slider2"].Update(duracionEleccionPalabra[nivel]["minutos"]["rango"])
				window["combo"].Update((list(duracionJugada[nivel].keys())[1]).capitalize())
				window["combo2"].Update((list(duracionEleccionPalabra[nivel].keys())[0]).capitalize())
			
			for let in letrasD:
				window[(let,"c")].Update(letrasD[let]["cant"])
				window[(let,"p")].Update(letrasD[let]["puntos"]) 
			      



