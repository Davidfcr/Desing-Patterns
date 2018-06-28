import abc

class AbsCommand(object):
	
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def ejecutar(self):
		pass
