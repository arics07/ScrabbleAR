from pattern.es import parse
from pattern.es import lexicon, spelling

validas = ['NN', 'NNS', 'VB', 'JJ']
#palabra = input('ingresa palabra\n ')
#esValida = False

def clasificar(palabra):
    pal = parse(palabra).split()
    print() #para control
    print(pal)
    if pal[0][0][1] in validas:
        devuelve =  True  #1
    else:
        devuelve = False #0
    return devuelve
	
	
def analizar_palabra_pat(palabra, esValida):
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
