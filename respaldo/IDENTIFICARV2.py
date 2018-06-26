# -- coding: utf-8 --

import os, sys
from variables import path, ambiente

path_tablas = path+'\\resources\\tablas'

carpetas_en_el_directorio = os.listdir(path_tablas)

'''

 Se capturan todos los archivos que contentan la extension .parametros

'''
archivos_parametros = []
for name_file in carpetas_en_el_directorio:
	if '.parametros' in name_file:
		archivos_parametros.append(name_file)

'''

 Se capturan todos los archivos que contentan la palabra con el ambiente
 ingresado en la fuente variables.py

'''
f = open(path+'\\arhivos_con_ambiente.txt', 'w')

archivos_con_ambiente = []
for archivo in archivos_parametros:
	with open(path_tablas+'\\'+archivo, encoding="ISO-8859-1") as archivo_leido:
		for line in archivo_leido:
			if ('#'+ambiente) in line.lower() or \
			(' '+ambiente) in line.lower():
				palabra = ("linea: "+line)
				archivo_correspondiente = ("archivo correspondiente: "+archivo)
				f.writelines(palabra)
				f.writelines(archivo_correspondiente+'\n')
				archivos_con_ambiente.append(archivo)
				break

f.close()
