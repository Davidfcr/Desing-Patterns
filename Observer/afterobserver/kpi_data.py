from collections import namedtuple
from itertools import starmap

data = (('nuevo', 10), ('abierto', 20), ('cerrado', 30), )
nt = namedtuple('KPI', 'nombre valor')
KPI_Data = starmap(nt, data)