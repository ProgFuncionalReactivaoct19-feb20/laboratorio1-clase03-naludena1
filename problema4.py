"""
	@naludena1
"""
# Laboratorio 1
#
"""
	Dado el siguiente listado:
	notas = [(5, 5, 10, "Regular"), (10, 2, 4, "Bueno"),
	(10, 1, 9, "Muy Bueno"), (7, 2, 3, "Sobresaliente")]
	Filtrar aquellos que tiene la calificación cualitativa "Regular o Bueno"
"""
datos = [(5, 5, 10, "Regular"), (10, 2, 4, "Bueno"), (10, 1, 9, "Muy Bueno"),
	(7, 2, 3, "Sobresaliente")]

resultado = filter(lambda x: x[3] == "Regular" or x[3] == "Bueno", datos)

print(list(resultado))
