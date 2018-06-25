# -- coding: utf-8 --

import os, sys, re
import unidecode

ambiente = 'integracion'

path_ubicado = os.getcwd()
path = os.path.abspath(os.path.join(path_ubicado, '..'))

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
	with open(path_tablas+'\\'+archivo,'r') as archivo_leido:
		for line in archivo_leido:
			for word in line:
				if re.match('^[a-zA-Z_]+$', word):
			#if re.match('^[a-zA-Z_]+$', line):
				print(line)
			
f.close()
