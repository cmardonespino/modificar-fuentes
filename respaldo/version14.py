 # -- coding: utf-8 --

import os, sys, unidecode
from variables import path, ambiente, ambientes
from identificar_archivos import archivos_con_ambiente

path_tablas = path+'\\resources\\tablas'

carpetas_en_el_directorio = os.listdir(path_tablas)

#VERSION 14
os.system('mkdir '+path+'\\output')
def method(lines, ambientes, ambiente):
	ambientes_elem = set(ambientes)
	i=0 
	a=0 
	nuevo_contenido_archivo = []

	for i in range(len(lines)):
		# se agrega unidecode por archivo AdministracionCampanas.parametros
		if any(word in unidecode.unidecode(lines[i].lower()) for word in ambientes):
			a = 2
			if '#' in lines[i] or ';' in lines[i]:
				nuevo_contenido_archivo.append(lines[i])
			else:
				nuevo_contenido_archivo.append('#'+lines[i])
		elif ambiente in unidecode.unidecode(lines[i].lower()) or \
		'filesystem '+ambiente in unidecode.unidecode(lines[i].lower()):
			# condición agregada por atmpagodeservicios.parametros
			if ambiente+':' in lines[i].lower():
				newstr = lines[i].replace("#", "")
				nuevo_contenido_archivo.append(newstr)
			else:
				# condicion agregada por archivo admMisSegurosVig.parametros
				if '#' in lines[i].lower():
					nuevo_contenido_archivo.append(lines[i])
				else:
					nuevo_contenido_archivo.append('#'+lines[i])
				a = 1
		else:
			if a == 2 and lines[i] != '\n':
				if '#' in lines[i]:
					#agregado por archivo admMisSegurosVig.parametros
					# linea 89
					if 'servicioAlertaLatinia;' in lines[i]:
						newstr = lines[i].replace("#", "")
						nuevo_contenido_archivo.append(newstr)
					#agregado por archivo Riesgo.parametros
					# linea 135
					elif ';' in lines[i].lower():
						if 'IMAGEN_PRODUCTO;' in lines[i] or 'SERVIDOR_FTP;' in lines[i] or \
						'NOMINA_VV_CCA;' in lines[i]:
							nuevo_contenido_archivo.append(lines[i])
						else:
							newstr = lines[i].replace("#", "")
							nuevo_contenido_archivo.append(newstr)
					else:
						nuevo_contenido_archivo.append(lines[i])
				elif '---' in lines[i]:
					if '#' in lines[i] or ';' in lines[i] or '.\n' in lines[i]:
						nuevo_contenido_archivo.append(lines[i])
					else:
						nuevo_contenido_archivo.append('#'+lines[i])
				# condición agregada por atmpagodeservicios.parametros
				elif 'WSDL_SERVIPAG;' in lines[i]:
					nuevo_contenido_archivo.append(lines[i])
				elif ';' in lines[i] or '==' in lines[i]:
					nuevo_contenido_archivo.append('#'+lines[i])
				else:
					nuevo_contenido_archivo.append('#'+lines[i])
			elif a == 1 and lines[i] != '\n':
				if '#' in lines[i]:
					if '---' in lines[i] or '.\n' in lines[i] or ' - ' in lines[i] or \
					'==' in lines[i] or '#\n' in lines[i]:
						nuevo_contenido_archivo.append(lines[i])
					else:
						newstr = lines[i].replace("#", "")
						nuevo_contenido_archivo.append(newstr)
				elif '---' in lines[i]:
					if '#' in lines[i] or '.\n' in lines[i]:
						nuevo_contenido_archivo.append(lines[i])
					else:
						nuevo_contenido_archivo.append('#'+lines[i])
				elif ';' in lines[i]:
					nuevo_contenido_archivo.append(lines[i])
				elif '==' in lines[i]:
					nuevo_contenido_archivo.append('#'+lines[i])
				else:
					nuevo_contenido_archivo.append(lines[i])
			else:
				a=0
				nuevo_contenido_archivo.append(lines[i])

	return nuevo_contenido_archivo

ambientes_elem = set(ambientes)
if ambiente in ambientes_elem:
	ambientes.remove(ambiente)


for archivo in archivos_con_ambiente:
	with open(path_tablas+'\\'+archivo,errors='ignore') as f:
		lines = f.readlines()
		nuevo_archivo = open(path+'\\output\\'+archivo+'.txt', 'w') 
		nuevo_archivo.writelines(method(lines, ambientes, ambiente))
