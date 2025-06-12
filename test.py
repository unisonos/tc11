import unittest
from time import time

from matricula import simulador_matricula

tiempo = time()
reporte = simulador_matricula()
tiempo = time() - tiempo
print(f"simulador_matricula() se completó en {tiempo:.6f}seg")