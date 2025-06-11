from multiprocessing import Process, Array
from random import randint
from time import sleep

from prettytable import PrettyTable


def imprimir(reporte):
    pretty_table = PrettyTable()
    pretty_table.field_names = reporte[0].keys()
    for curso in reporte:
        pretty_table.add_row(curso.values())

    print()
    print(pretty_table)


def verificar(num_estudiantes, curso, cupos, matriculados_compartido, cupos_compartido, en_espera_compartido):
    return (cupos[curso] == matriculados_compartido[curso]) and (cupos_compartido[curso] == 0) and (
            matriculados_compartido[curso] + cupos_compartido[curso] == cupos[curso]) and (
            matriculados_compartido[curso] + en_espera_compartido[curso] == num_estudiantes)


def simulador_matricula():
    num_cursos = 6
    cursos = ["IC-1802", "IC-1803", "IC-1400", "IC-2001", "IC-2101", "IC-3002"]
    cupos = [25, 25, 10, 40, 30, 30]
    matriculados = num_cursos * [0]
    en_espera = num_cursos * [0]

    cupos_compartido = Array('i', cupos)
    matriculados_compartido = Array('i', matriculados)
    en_espera_compartido = Array('i', en_espera)

    num_estudiantes = 40

    procesos_estudiantes = []
    for estudiante in range(0, num_estudiantes):
        procesos_estudiantes.append(
            Process(target=matricular,
                    args=(estudiante, num_cursos, cupos_compartido, matriculados_compartido, en_espera_compartido))
        )

    for p in procesos_estudiantes:
        p.start()

    for p in procesos_estudiantes:
        p.join()

    reporte = []
    for i in range(0, num_cursos):
        reporte.append({
            'curso': cursos[i],
            'cupos': cupos[i],
            'matriculados': matriculados_compartido[i],
            'disponibles': cupos_compartido[i],
            'espera': en_espera_compartido[i],
            'consistente': verificar(num_estudiantes, i, cupos, matriculados_compartido, cupos_compartido,
                                     en_espera_compartido)
        })

    imprimir(reporte)
    return reporte


def matricular(estudiante, num_cursos, cupos, matriculados, en_espera):

    cursos_a_matricular = list(range(num_cursos))
    for curso in cursos_a_matricular:
        # print(f'Estudiante carnet {estudiante:06d} intentando matricular curso {curso}')
        if cupos[curso] > 0:
            cupos[curso] = cupos[curso] - 1
            # simular tiempo de operación del sistema
            sleep(randint(1, 3))
            matriculados[curso] = matriculados[curso] + 1
        else:
            en_espera[curso] = en_espera[curso] + 1


#esto es una prueba de texto