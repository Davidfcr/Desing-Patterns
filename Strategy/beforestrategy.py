class Operador(object):
	suma = 1
	resta = 2
	multiplicacion = 3
	division = 4
		

class Calculadora(object):
	num1 = 4
	num2 = 2

	def operacion_metematica(self, accion):
		if accion.operador == Operador.suma:
			return self.num1 + self.num2
		elif accion.operador == Operador.resta:
			return self.num1 - self.num2
		elif accion.operador == Operador.multiplicacion:
			return self.num1 * self.num2
		elif accion.operador == Operador.division:
			return self.num1 / self.num2
		else:
			raise ValueError('Operacion Invalida {0}'.format(accion.operador))

		
class Accion(object):
	
	def __init__(self, operador):
		self._operador = operador

	@property
	def operador(self):
		return self._operador


