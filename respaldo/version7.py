# -- coding: utf-8 --

import os, sys
from variables import path, ambiente, ambientes
from identificar_archivos import archivos_con_ambiente

path_tablas = path+'\\resources\\tablas'

carpetas_en_el_directorio = os.listdir(path_tablas)

#VERSION 7
os.system('mkdir '+path+'\\output')
def method(lines, archivo, ambientes, ambiente):
	ambientes_elem = set(ambientes)
	i=0 
	a=0 
	nuevo_archivo = open(path+'\\output\\'+archivo+'.txt', 'w') 
	nuevo_contenido_archivo = []

	for i in range(len(lines)):
		if 'desarrollo' in lines[i].lower() or \
		'integracion' in lines[i].lower() or \
		'produccion' in lines[i].lower() or \
		'filesystem desarrollo' in lines[i].lower() or \
		'filesystem integracion' in lines[i].lower() or \
		'filesystem produccion' in lines[i].lower():
			a = 2
			if '#' in lines[i]:
				nuevo_contenido_archivo.append(lines[i])
			elif ';' in lines[i]:
				nuevo_contenido_archivo.append(lines[i])
			else:
				nuevo_contenido_archivo.append('#'+lines[i])
		elif 'certificacion' in lines[i].lower() or \
		'filesystem certificacion' in lines[i].lower():
			a = 1
			nuevo_contenido_archivo.append(lines[i])
		else:
			if a == 2 and lines[i] != '\n':
				if '#' in lines[i]:
					nuevo_contenido_archivo.append(lines[i])
				elif '---' in lines[i]:
					if '#' in lines[i]:
						nuevo_contenido_archivo.append(lines[i])
					elif ';' in lines[i]:
						nuevo_contenido_archivo.append(lines[i])
					elif '.\n' in lines[i]:
						nuevo_contenido_archivo.append(lines[i])
					else:
						nuevo_contenido_archivo.append('#'+lines[i])
				elif ';' in lines[i]:
					nuevo_contenido_archivo.append('#'+lines[i])
				else:
					nuevo_contenido_archivo.append('#'+lines[i])
			elif a == 1 and lines[i] != '\n':
				if '#' in lines[i]:
					if '---' in lines[i]:
						nuevo_contenido_archivo.append(lines[i])
					elif '.\n' in lines[i]:
						nuevo_contenido_archivo.append(lines[i])
					elif ' - ' in lines[i]:
						nuevo_contenido_archivo.append(lines[i])
					else:
						newstr = lines[i].replace("#", "")
						nuevo_contenido_archivo.append(newstr)
				elif '---' in lines[i]:
					if '#' in lines[i]:
						nuevo_contenido_archivo.append(lines[i])
					elif '.\n' in lines[i]:
						nuevo_contenido_archivo.append(lines[i])
					else:
						nuevo_contenido_archivo.append('#'+lines[i])
				elif ';' in lines[i]:
					nuevo_contenido_archivo.append(lines[i])
				else:
					nuevo_contenido_archivo.append(lines[i])
			else:
				a=0
				nuevo_contenido_archivo.append(lines[i])

	nuevo_archivo.writelines(nuevo_contenido_archivo)

ambientes_elem = set(ambientes)
if ambiente in ambientes_elem:
	ambientes.remove(ambiente)


for archivo in archivos_con_ambiente:
	with open(path_tablas+'\\'+archivo) as f:
		lines = f.readlines()
		method(lines, archivo, ambientes, ambiente)
