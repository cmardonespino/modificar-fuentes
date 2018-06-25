

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
'''
#VERSION 3
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
'''

'''
#VERSION 4
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
			elif ';' in lines[i]:
				nuevo_contenido_archivo.append(lines[i])
			else:
				nuevo_contenido_archivo.append('#'+lines[i])
		elif 'produccion' in lines[i].lower() or \
		'filesystem produccion' in lines[i].lower():
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
#VERSION 5
os.system('mkdir '+path+'\\output')
def method(lines, archivo):
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
			elif ';' in lines[i]:
				nuevo_contenido_archivo.append(lines[i])
			else:
				nuevo_contenido_archivo.append('#'+lines[i])
		elif 'produccion' in lines[i].lower() or \
		'filesystem produccion' in lines[i].lower():
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
					nuevo_contenido_archivo.append(lines[i])
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
'''
'''
#VERSION 6
os.system('mkdir '+path+'\\output')
def method(lines, archivo, ambientes):
	ambientes_elem = set(ambientes)
	i=0 
	a=0 
	nuevo_archivo = open(path+'\\output\\'+archivo+'.txt', 'w') 
	nuevo_contenido_archivo = []

	for i in range(len(lines)):
		if any(ext in lines[i].lower() for ext in ambientes_elem) or \
		'filesystem desarrollo' in lines[i].lower() or \
		'filesystem integracion' in lines[i].lower() or \
		'filesystem certificacion' in lines[i].lower():
			a = 2
			if '#' in lines[i]:
				nuevo_contenido_archivo.append(lines[i])
			elif ';' in lines[i]:
				nuevo_contenido_archivo.append(lines[i])
			else:
				nuevo_contenido_archivo.append('#'+lines[i])
		elif 'produccion' in lines[i].lower() or \
		'filesystem produccion' in lines[i].lower():
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
					nuevo_contenido_archivo.append(lines[i])
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
'''