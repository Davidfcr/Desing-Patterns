from .abs_fabrica import AbsFabrica
from carros.gm.cadillac import ChevyCadillacCTS
from carros.gm.camaro import ChevyCamaro
from carros.gm.spark import ChevySpark


class FabricaGM(AbsFabrica):

    @staticmethod
    def crear_economico():
        return ChevySpark()

    @staticmethod
    def crear_deportivo():
        return ChevyCamaro()

    @staticmethod
    def crear_lujoso():
        return ChevyCadillacCTS()
