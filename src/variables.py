# -- coding: utf-8 --

import os

#variables = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
#	+ '/another_folder/')

path_ubicado = os.getcwd()
path = os.path.abspath(os.path.join(path_ubicado, '..'))

ambiente = 'produccion'
ambientes = [
	'produccion', 
	'desarrollo', 
	'certificacion',
	'integracion',
]
