import sys
from ejecutor_command import EjecutorCommand

if len(sys.argv) < 2:
	print(' Usando c:\Python34\python -m Command <command>')
	print(' Comandos:')
	print(' 	CrearOrden')
	print(' 	ActualizarOrden')
	print(' 	EnviarOrden')
	exit()

ejecutor = EjecutorCommand()
ejecutor.ejecuta_command(sys.argv[1:])

# Ejecuta en terminal con:
# python aftercommand.py ActualizarOrden 3.1415