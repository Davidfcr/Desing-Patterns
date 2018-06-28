import abc


class AbsFabrica(metaclass=abc.ABCMeta):

    @abc.abstractstaticmethod
    def crear_economico(self):
        pass

    @abc.abstractstaticmethod
    def crear_deportivo(self):
        pass

    @abc.abstractstaticmethod
    def crear_lujoso(self):
        pass

