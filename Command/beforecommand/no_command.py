from command_abc import AbsCommand

class NoCommand(AbsCommand):

	def __init__(self, args):
		self._command = args[0]

	def ejecutar(self):
		print('No existen comandos con el nombre {0}'.format(self._command))