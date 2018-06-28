from observer import AbsSubject

class KPIs(AbsSubject):
	_tickets_abiertos = -1
	_tickets_cerrados = -1
	_tickets_nuevos = -1

	@property
	def tickets_abiertos(self):
		return self._tickets_abiertos

	@property
	def tickets_cerrados(self):
		return self._tickets_cerrados

	@property
	def tickets_nuevos(self):
		return self._tickets_nuevos

	def set_kpis(self, tickets_abiertos, tickets_cerrados, tickets_nuevos):
		self._tickets_abiertos = tickets_abiertos
		self._tickets_cerrados = tickets_cerrados
		self._tickets_nuevos = tickets_nuevos
		self.notify()
