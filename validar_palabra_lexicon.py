from pattern.es import parse
from pattern.es import lexicon, spelling

validas = ['NN', 'NNS', 'VB', 'JJ']

def clasificar(palabra):
    pal = parse(palabra).split()
    #print para control
    #print(pal)
    if pal[0][0][1] in validas:
        devuelve =  1
    else:
        devuelve = 0
    return devuelve
	
	
def analizar_palabra_pat(palabra):
	if not palabra in spelling:
		if not palabra in lexicon:
			#print('No se encuentra en pattern.es')
			return 0
		else:
			#print('La encontró en lexicon')
			clasificar(palabra)
			return 1
	else:
		#print('La encontró en spelling')
		clasificar(palabra)
		return 1
