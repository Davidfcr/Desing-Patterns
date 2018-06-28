import abc


class AbsCarros(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def encender(self):
        pass

    @abc.abstractmethod
    def apagar(self):
        pass
