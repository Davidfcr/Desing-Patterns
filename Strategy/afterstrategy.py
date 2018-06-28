from abc import ABCMeta, abstractmethod
import math

class Calculadora(object):
	num1 = 4
	num2 = 2

	def __init__(self, strategy):
		self._strategy = strategy
	
	def operacion_matematica(self):
		return self._strategy.calcular(self.num1, self.num2)


class AbsStrategy(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def calcular(self, num1, num2):
		""" Calcula el resultado de la operacion asignada """


class SumaStrategy(AbsStrategy):
	
	def calcular(self, num1, num2):
		return num1 + num2


class RestaStrategy(AbsStrategy):
	
	def calcular(self, num1, num2):
		return num1 - num2


class MultiplicacionStrategy(AbsStrategy):
	
	def calcular(self, num1, num2):
		return num1 * num2


class DivisionStrategy(AbsStrategy):
	
	def calcular(self, num1, num2):
		return num1 / num2


class RaizStrategy(AbsStrategy):
	
	def calcular(self, num1, num2):
		return math.sqrt(num1)