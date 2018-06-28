import abc

class AbsOrdenCommand(object):
	
	__metaclass__ = abc.ABCMeta

	@abc.abstractproperty
	def nombre(self):
		pass

	@abc.abstractproperty
	def descripcion(self):
		pass
