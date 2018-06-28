from beforestrategy import Operador
from beforestrategy import Calculadora
from beforestrategy import Accion

# Prueba de Suma
tipo_operador = Accion(Operador.suma)
calculadora = Calculadora()
resultado = calculadora.operacion_metematica(tipo_operador)
assert resultado == 6

# Prueba de Resta
tipo_operador = Accion(Operador.resta)
calculadora = Calculadora()
resultado = calculadora.operacion_metematica(tipo_operador)
assert resultado == 2

# Prueba de Multiplicacion
tipo_operador = Accion(Operador.multiplicacion)
calculadora = Calculadora()
resultado = calculadora.operacion_metematica(tipo_operador)
assert resultado == 8

# Prueba de Division
tipo_operador = Accion(Operador.division)
calculadora = Calculadora()
resultado = calculadora.operacion_metematica(tipo_operador)
assert resultado == 2

print('Pruebas existosas !!')