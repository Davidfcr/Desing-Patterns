from .abs_fabrica import AbsFabrica
from carros.ford.fiesta import FordFiesta
from carros.ford.mustang import FordMustang
from carros.ford.lincoln import FordLincolnMKS


class FabricaFord(AbsFabrica):

    @staticmethod
    def crear_economico():
        return FordFiesta()

    @staticmethod
    def crear_deportivo():
        return FordMustang()

    @staticmethod
    def crear_lujoso():
        return FordLincolnMKS()
