class EjecutorCommand(object):
	
	def ejecuta_command(self, args):
		if args[0] == 'CrearOrden':
			self.crear_orden()
		elif args[0] == 'ActualizarOrden':
			self.actualizar_orden(args[1])
		elif args[0] == 'EnviarOrden':
			self.enviar_orden()
		else:
			print('Comando desconocido: '+ args[0])

	def crear_orden(self):
		pass

	def actualizar_orden(self, val):
		print(val)
		valor_antiguo = 5
		print('Datos actualizados')
		print('Log actualizado de cantidad {0} a {1}'.format(valor_antiguo, val))

	def enviar_orden(self):
		pass