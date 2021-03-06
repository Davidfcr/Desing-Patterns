import abc

class AbsObserver(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def update(self, value):
		pass

class AbsSubject(object):
	
	__metaclass__ = abc.ABCMeta
	_observers = set()

	def attach(self, observer):
		if not isinstance(observer, AbsObserver):
			raise TypeError('Observer no se deriva de AbsObserver')
		self._observers |= {observer}

	def detach(self, observer):
		self._observers -= {observer}
	
	def notify(self, value=None):
		for observer in self._observers:
			if value is None:
				observer.update()
			else:
				observer.update(value)
