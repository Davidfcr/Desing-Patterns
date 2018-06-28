class Logs(object):
	ans = None
	
	@staticmethod
	def instance():
		if '_instance' not in Logs.__dict__:
			Logs._instance = Logs()
		return Logs._instance


log1 = Logs.instance()
log2 = Logs.instance()

assert log1 is log2
log1.ans = 42

assert log2.ans == log1.ans

print('Test pasaron.')
