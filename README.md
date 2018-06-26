# Modificar fuentes tabla parametros
Proyecto desarrollado en python 3+ en un ambiente Windows 7 Enterprise, el cual a través de unos scripts permiten la fácil modificación de parametros de acuerdo a las necesidades que se tengan.
En caso de querer pasar por integración, y en vez de tener que modificar la tabla de parametros y comentar las variables que no correspondan a integración uno por uno, este script facilita la tarea.
# HOWTO
* Dirigirse a la fuente [variables.py](src/variables.py) y modificar el parametro `ambiente`
* Abrir una consola Git Bash y ejecutar el comando dentro de la carpeta raíz del proyecto:

`./test-env.sh go`

## Requerimientos para compilación
Para este proyecto se utilizaron algunas dependencias que facilitaron el desarrollo de este script, las cuales se deben tener instaladas en el equipo que se requiera compilar. Las dependencias son:

* `unidecode`

Las dependencias fueron instaladas a través del administrador de paquetes [pip](https://es.wikipedia.org/wiki/Pip_(administrador_de_paquetes)).