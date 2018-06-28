from fabricas.fabrica_ford import FabricaFord
from fabricas.fabrica_gm import FabricaGM


for fabrica in FabricaFord, FabricaGM:
    carro = fabrica.crear_economico()
    carro.encender()
    carro.apagar()
    carro = fabrica.crear_deportivo()
    carro.encender()
    carro.apagar()
    carro = fabrica.crear_lujoso()
    carro.encender()
    carro.apagar()
