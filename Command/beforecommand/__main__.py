from crear import CrearOrden
from actualizar import ActualizarOrden
from enviar import EnviarOrden
from no_command import NoCommand
import sys

def obtener_comandos():
	comandos = (CrearOrden, ActualizarOrden, EnviarOrden)
	return dict([cls.nombre, cls] for cls in comandos)

def imprimir_uso(comandos):
	print('Uso: python -m Command NombreComando [arguments]')
	print('Comandos:')
	for comando in comandos.values():
		print('		{0}'.format(comando.descripcion))

def parse_comando(comandos, args):
	comando = comandos.setdefault(args[0], NoCommand)
	return comando(args)

comandos = obtener_comandos()
if len(sys.argv) < 2:
	imprimir_uso(comandos)
	exit()


comando = parse_comando(comandos, sys.argv[1:])
comando.ejecutar()

# Ejecuta en terminal con:
# python __main__.py ActualizarOrden 45