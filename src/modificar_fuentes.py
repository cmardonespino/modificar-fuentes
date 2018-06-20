# -- coding: utf-8 --

import os, sys
from variables import path, ambiente
from identificar_archivos import archivos_con_ambiente

ambientes = ['desarrollo', 'produccion', 'integracion', 'certificacion']
if ambiente in ambientes:
	ambientes.remove(ambiente)

path_tablas = path+'\\resources\\tablas'

carpetas_en_el_directorio = os.listdir(path_tablas)


'''
i=0
a=0
nuevo_archivo = open(path+'\\hola.txt', 'w')
nuevo_contenido_archivo = []

for i in range(len(lines)):
	if '#'+ambiente in lines[i].lower() or \
	 '#filesystem '+ambiente in lines[i].lower():
		a =+ 1
		nuevo_contenido_archivo.append(lines[i])
		break
	if a == 1:
		if lines[i] != '\n':
			nuevo_contenido_archivo.append('#'+lines[i])
			a = 0
		else:
			break
	else:
		nuevo_contenido_archivo.append(lines[i])

nuevo_archivo.writelines(nuevo_contenido_archivo) 
''' 

'''
i=0 
a=0 
nuevo_archivo = open(path+'\\hola.txt', 'w') 
nuevo_contenido_archivo = []

for i in range(len(lines)):
	if a == 1:
		if lines[i] != '\n' and '#desarrollo' not in lines[i].lower() or \
	 		'#filesystem desarrollo' not in lines[i].lower():
				continue
		else:
			nuevo_contenido_archivo.append('#'+lines[i])
			a=0
			break
	if '#desarrollo' in lines[i].lower() or \
	'#filesystem desarrollo' in lines[i].lower():
		continue
	if '#'+ambiente in lines[i]:
		nuevo_contenido_archivo.append(lines[i])
		a =+ 1
		break
nuevo_archivo.writelines(nuevo_contenido_archivo)
'''

'''
#VERSION 1
i=0 
a=0 
nuevo_archivo = open(path+'\\hola.txt', 'w') 
nuevo_contenido_archivo = []

for i in range(len(lines)):
	if '#desarrollo' in lines[i].lower() or \
	'#integracion' in lines[i].lower() or \
	'#certificacion' in lines[i].lower() or \
	'#filesystem desarrollo' in lines[i].lower() or \
	'#filesystem integracion' in lines[i].lower() or \
	'#filesystem certificacion' in lines[i].lower():
		a = 2
		nuevo_contenido_archivo.append(lines[i])
	elif '#produccion' in lines[i].lower() or \
	'#filesystem produccion' in lines[i].lower():
		a = 1
		nuevo_contenido_archivo.append(lines[i])
	else:
		if a == 2 and lines[i] != '\n':
			if '#' in lines[i]:
				nuevo_contenido_archivo.append(lines[i])
			else:
				nuevo_contenido_archivo.append('#'+lines[i])
		elif a == 1 and lines[i] != '\n':
			if '#' in lines[i]:
				newstr = lines[i].replace("#", "")
				nuevo_contenido_archivo.append(newstr)
			else:
				nuevo_contenido_archivo.append(lines[i])
		else:
			a=0
			nuevo_contenido_archivo.append(lines[i])

nuevo_archivo.writelines(nuevo_contenido_archivo)
'''
'''
#VERSION 2
i=0 
a=0 
nuevo_archivo = open(path+'\\hola.txt', 'w') 
nuevo_contenido_archivo = []

for i in range(len(lines)):
	if '#desarrollo' in lines[i].lower() or \
	'#integracion' in lines[i].lower() or \
	'#certificacion' in lines[i].lower() or \
	'filesystem desarrollo' in lines[i].lower() or \
	'filesystem integracion' in lines[i].lower() or \
	'filesystem certificacion' in lines[i].lower():
		a = 2
		if '#' in lines[i]:
			nuevo_contenido_archivo.append(lines[i])
		else:
			nuevo_contenido_archivo.append('#'+lines[i])
	elif '#produccion' in lines[i].lower() or \
	'#filesystem produccion' in lines[i].lower():
		a = 1
		nuevo_contenido_archivo.append(lines[i])
	else:
		if a == 2 and lines[i] != '\n':
			if '#' in lines[i]:
				nuevo_contenido_archivo.append(lines[i])
			else:
				nuevo_contenido_archivo.append('#'+lines[i])
		elif a == 1 and lines[i] != '\n':
			if '#' in lines[i]:
				newstr = lines[i].replace("#", "")
				nuevo_contenido_archivo.append(newstr)
			else:
				nuevo_contenido_archivo.append(lines[i])
		else:
			a=0
			nuevo_contenido_archivo.append(lines[i])

nuevo_archivo.writelines(nuevo_contenido_archivo)
'''
os.system('mkdir '+path+'\\output')
def method(lines, archivo):
	#VERSION 3
	i=0 
	a=0 
	nuevo_archivo = open(path+'\\output\\'+archivo+'.txt', 'w') 
	nuevo_contenido_archivo = []

	for i in range(len(lines)):
		if 'desarrollo' in lines[i].lower() or \
		'integracion' in lines[i].lower() or \
		'certificacion' in lines[i].lower() or \
		'filesystem desarrollo' in lines[i].lower() or \
		'filesystem integracion' in lines[i].lower() or \
		'filesystem certificacion' in lines[i].lower():
			a = 2
			if '#' in lines[i]:
				nuevo_contenido_archivo.append(lines[i])
			else:
				nuevo_contenido_archivo.append('#'+lines[i])
		elif '#produccion' in lines[i].lower() or \
		'#filesystem produccion' in lines[i].lower():
			a = 1
			nuevo_contenido_archivo.append(lines[i])
		else:
			if a == 2 and lines[i] != '\n':
				if '#' in lines[i]:
					nuevo_contenido_archivo.append(lines[i])
				else:
					nuevo_contenido_archivo.append('#'+lines[i])
			elif a == 1 and lines[i] != '\n':
				if '#' in lines[i]:
					newstr = lines[i].replace("#", "")
					nuevo_contenido_archivo.append(newstr)
				else:
					nuevo_contenido_archivo.append(lines[i])
			else:
				a=0
				nuevo_contenido_archivo.append(lines[i])

	nuevo_archivo.writelines(nuevo_contenido_archivo)

for archivo in archivos_con_ambiente:
	with open(path_tablas+'\\'+archivo) as f:
		lines = f.readlines()
		method(lines, archivo)
