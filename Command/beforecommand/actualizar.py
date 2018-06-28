from command_abc import AbsCommand
from orden_command_abc import AbsOrdenCommand

class ActualizarOrden(AbsCommand, AbsOrdenCommand):
	
	nombre = 'ActualizarOrden'
	descripcion = 'numero de ActualizarOrden'
	
	def __init__(self, args):
		self.nuevacantidad = args[1]

	def ejecutar(self):
		antiguacantidad = 5
		print('Datos actualizados')
		print('Log actualizado de cantidad {0} a {1}'.format(antiguacantidad, self.nuevacantidad))

		