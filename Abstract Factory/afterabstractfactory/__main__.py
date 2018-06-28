from fabricas.gm import ChevySpark
from fabricas.gm import ChevyCamaro
from fabricas.gm import ChevyCadillacCTS
from fabricas.ford import FordFiesta
from fabricas.ford import FordMustang
from fabricas.ford import FordLincolnMKS
from random import randint

marcas = ('gm', 'ford')
ediciones = ('Economica', 'Deportiva', 'Lujo')

marca = marcas[randint(0, 1)]
edicion = ediciones[randint(0, 2)]

if marca == 'gm':
    if edicion == 'Economica':
        carro = ChevySpark()
    elif edicion == 'Deportiva':
        carro = ChevyCamaro()
    elif edicion == 'Lujo':
        carro = ChevyCadillacCTS()
    else:
        raise ValueError("Unkown Car")
elif marca == 'ford':
    if edicion == 'Economica':
        carro = FordFiesta()
    elif edicion == 'Deportiva':
        carro = FordMustang()
    elif edicion == 'Lujo':
        carro = FordLincolnMKS()
    else:
        raise ValueError("Unkown Car")

carro.encender()
carro.apagar()
