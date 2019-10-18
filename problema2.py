"""
	@naludena1
"""
# Laboratorio 1
#
"""
	Dada la siguiente lista:
	notas = [(5, 5, 10), (10, 2, 4), (10, 1, 9), (10, 2, 3)]
	En contrar una lista como sigue:
	[20, 16, 20, 15]
"""

notas = [(5, 5, 10), (10, 2, 4), (10, 1, 9), (10, 2, 3)]

suma0 = lambda x: x[0]
suma1 = lambda x: x[1]
suma2 = lambda x: x[2]

resultado = lambda x: (suma0(x) + suma1(x) + suma2(x)) 
print(list(map(resultado, notas)))