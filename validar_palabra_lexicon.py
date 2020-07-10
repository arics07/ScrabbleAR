from pattern.es import parse
from pattern.es import lexicon, spelling, verbs

validas = ['NN', 'NNS', 'VB', 'JJ']

def clasificar(palabra):
	'''Esta función analiza la palabra que recibe como patametro. 
	Devuelve True si es sustantivo, verbo o adjetivo. Sino devuelve False. '''
	pal = parse(palabra).split()
	print() #para control
	print(pal)
	if pal[0][0][1] in validas:
		devuelve =  True
	else:
		devuelve = False
	return devuelve
	
	
def analizar_palabra_pat(palabra, esValida):
	'''Esta función usa las funciones del módulo pattern. Chequea si la palabra 
	está en verbs o simultaneamente en lexicon y spelling. Si está, analiza que 
	tipo de palabra es (sustantivo, verbo o adjetivo). Devuelve True si la palabra
	es válida y False si no lo es.'''
	pal = palabra.lower()
	if not pal in verbs:
		if pal in lexicon:
			if pal in spelling:
			#print('Esta en spelling y lexicon')
				return clasificar(pal)
		else:
			#print('No está ni en verbs ni en lexicon')
			return False
	else:
		#print('La encontró en verbs')
		return clasificar(pal)
