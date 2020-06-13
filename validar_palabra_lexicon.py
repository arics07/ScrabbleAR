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
	if not palabra in spelling:
		if not palabra in lexicon:
			print('No se encuentra en pattern.es')
			esValida=False
			return esValida  #0
		else:
			print('La encontró en lexicon')
			esValida = clasificar(palabra)
			print(esValida)
			return esValida #1
	else:
		print('La encontró en spelling')
		esValida= clasificar(palabra)
		print(esValida)
		return esValida #1
