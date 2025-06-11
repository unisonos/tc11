import unittest
from time import time

from matricula import simulador_matricula


class SimuladorMatriculaTest(unittest.TestCase):

    def test_simulador_matricula(self):
        tiempo = time()
        reporte = simulador_matricula()
        tiempo = time() - tiempo
        print(f"simulador_matricula() se completó en {tiempo:.6f}seg")

        self.assertLessEqual(tiempo, 120)
        self.assertTrue(all([registro['consistente'] for registro in reporte]))

