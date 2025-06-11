[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/UaMXdH3M)
# IC-3002 Tarea corta 11

Consideremos el código en el módulo `matricula.py`. Este implementa una simulación 
de un proceso de matrícula universitario.

En este modelo de simulación 40 estudiantes intentan matricular los mismos 6 cursos 
para los cuales hay cupos limitados, según se especifica en la siguiente tabla:

```commandline
+---------+-------+
|  curso  | cupos |
+---------+-------+
| IC-1802 |   25  |
| IC-1803 |   25  |
| IC-1400 |   10  |
| IC-2001 |   40  |
| IC-2101 |   30  |
| IC-3002 |   30  |
+---------+-------+
```

Los datos sobre cupos de cursos y cantidad de estudiantes matriculados por curso
se almacenan en dos listas llamadas respectivamente `cupos` y `matriculados`.

Cada estudiante se representa en el modelo como un proceso concurrente que ejecuta
la función `matricular` que corresponde a la operación de intentar matricular los 6
cursos.

Matricular un curso implica decrementar su cupo en una unidad e incrementar la 
cantidad de estudiantes matriculados también en una unidad. Antes de realizar esta
operación primero se verifica que aún haya cupos disponibles, si no hay cupos 
disponibles entonces el estudiante queda en una lista de espera, también representada
como una lista llamada `en_espera`.

Al final de la simulación se emite un reporte con los resultados del proceso: cuántos
estudiantes se matricularon por curso, cuántos cupos quedaron disponibles,
cuántos estudiantes quedaron en espera, y una verificación sobre inconsistencias en
los datos. Para cada curso se verifica que no se hayan matriculado más o menos 
estudiantes según el cupo correspondiente.

```commandline
+---------+-------+--------------+-------------+--------+-------------+
|  curso  | cupos | matriculados | disponibles | espera | consistente |
+---------+-------+--------------+-------------+--------+-------------+
| IC-1802 |   25  |      26      |      0      |   15   |    False    |
| IC-1803 |   25  |      24      |      0      |   15   |    False    |
| IC-1400 |   10  |      11      |      0      |   29   |    False    |
| IC-2001 |   40  |      40      |      0      |   0    |     True    |
| IC-2101 |   30  |      30      |      0      |   10   |     True    |
| IC-3002 |   30  |      28      |      0      |   10   |    False    |
+---------+-------+--------------+-------------+--------+-------------+
```

Cada proceso concurrente accede a las mismas listas de `cupos`, `matriculados` y 
`en_espera` generando de esta forma condiciones de carrera. Puesto que el código
actualmente no sincroniza el acceso a esta memoria compartida, estas condiciones
de carrera producirán inconsistencias en los datos de algunos cursos. 

Por ejemplo el reporte de la tabla anterior muestra que en el curso `IC-1802` hay 
26 estudiantes matriculados aunque solo había 25 cupos disponibles. Por otro lado,
en el curso `IC-1803` hay únicamente 24 estudiantes matriculados y 15 en espera aunque
tenía 25 cupos disponibles, es decir todavía queda 1 cupo por matricular.

Por esta razón, la tarea consiste en incorporar `Lock`s en el código para evitar
condiciones de carrera y asegurar la consistencia de los datos resultantes.

Debe cumplir con las siguientes restricciones:
* Únicamente agregar código nuevo, no puede eliminar código existente.
* Se pueden modificar las funciones existentes agregando parámetros e instrucciones.
* A excepción del problema de consistencia, no cambiar la funcionalidad de la simulación. 
* El tiempo de ejecución de la simulación no debe superar los 120 segundos.

## Cómo instalar el ambiente de desarrollo y ejecutar las pruebas localmente

Este proyecto requiere `python3`. Asegúrese que esté instalado en su distribución de linux.

Si no lo ha hecho anteriormente, crear un ambiente virtual para las dependencias

```bash
python3 -m venv .venv
```

Activar el ambiente virtual

```bash
source .venv/bin/activate
```

Instalar las dependencias

```bash
pip3 install -r requirements.txt
```

Ejecutar las pruebas

```bash
pytest -s -W ignore::DeprecationWarning
```

## Rúbrica

### Completitud (5 pts)

* (5 pts) La producción cumple totalmente con los requerimientos solicitados.
* (3 pts) La producción cumple parcialmente con los requerimientos solicitados.
* (1 pts) La producción, en su mayor parte, no cumple con los requerimientos solicitados.

### Correctitud (5 pts)

* (5 pts) El código pasa exitosamente todas las pruebas automatizadas.
* (3 pts) El código pasa la mayoría de las pruebas automatizadas.
* (1 pts) El código no pasa la mayoría de las pruebas automatizadas.

### Diseño del algoritmo (5 pts)

* (5 pts) El código respeta las restricciones del problema.
* (0 pts) El código no respeta las restricciones del problema.
