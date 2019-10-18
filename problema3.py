"""
	@naludena1
"""
# Laboratorio 1
#
"""
	Dada la siguiente frase:
	"No hay medicina que cure lo que no cura la felicidad"
	Encuentre el listado que sigue:
	["No", "hay", "que", "lo", "que", "no", "la"]
"""


def es_frase(x):
	palabras = ["No", "hay", "que", "lo", "que", "no", "la"]
	if x in datos:
		return True
	else:
		return False

datos = "No hay medicina que cure lo que no cura la felicidad"
result = datos.split()
resultado = filter(es_frase, datos)
print(list(result))