from afterstrategy import Calculadora
from afterstrategy import SumaStrategy
from afterstrategy import RestaStrategy
from afterstrategy import MultiplicacionStrategy
from afterstrategy import DivisionStrategy
from afterstrategy import RaizStrategy

# Prueba de Suma
estrategia = SumaStrategy()
calculadora = Calculadora(estrategia)
resultado = calculadora.operacion_matematica()
assert resultado == 6

# Prueba de Resta
estrategia = RestaStrategy()
calculadora = Calculadora(estrategia)
resultado = calculadora.operacion_matematica()
assert resultado == 2

# Prueba de Multiplicacion
estrategia = MultiplicacionStrategy()
calculadora = Calculadora(estrategia)
resultado = calculadora.operacion_matematica()
assert resultado == 8

# Prueba de Division
estrategia = DivisionStrategy()
calculadora = Calculadora(estrategia)
resultado = calculadora.operacion_matematica()
assert resultado == 2


# Prueba de Division
estrategia = RaizStrategy()
calculadora = Calculadora(estrategia)
resultado = calculadora.operacion_matematica()
assert resultado == 2

print('Pruebas existosas !!')