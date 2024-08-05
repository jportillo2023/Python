import re
import sys

# Cabecera - repo remoto origin/main.

class complejo:
	""" Representa a un numero complejo """
	def __init__(self, rI, jI):
		self.r = rI
		self.j = jI
	def __add__(self, C):
        	return complejo(self.r + C.r, self.j + C.j)
	def __sub__(self, C):
		return complejo(self.r - C.r, self.j - C.j)
	def __neg__(self):
		return complejo((-1)*self.r, (-1)*self.j)
	def __str__(self):
		return "{:.2f}+{:.2f}j".format(self.r, self.j)
	def __repl__(self):
		return self

def main():
	""" Funcion principal del programa """
	if len(sys.argv) < 2:
		print("Error: debe indicar dos valores complejos (a+bj) (c+dj)")
		sys.exit(1)
	else:
		try:
			# Expresion regular de un complejo expresado como (x.x+y.yj)
			patron = r"([0-9]{1,}\.[0-9]{1,})\+([0-9]{1,}\.[0-9]{1,})j"
			p = re.search(patron, sys.argv[1])   # Parte real.
			q = re.search(patron, sys.argv[2])   # Parte imaginaria.
			a, b, c, d = float(p[1]), float(p[2]), float(q[1]), float(q[2])
			A = complejo(a, b)
			B = complejo(c, d)
			print("{} + {} = {}".format(A, B, A+B))
		except:
			print("Ocurrio un error")
			sys.exit(1)
	sys.exit(0)

if __name__ == "__main__":
	main()
