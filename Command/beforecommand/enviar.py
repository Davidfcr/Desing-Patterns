from command_abc import AbsCommand
from orden_command_abc import AbsOrdenCommand

class EnviarOrden(AbsCommand, AbsOrdenCommand):

	def ejecutar(self):
		pass