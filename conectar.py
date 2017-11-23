#!/usr/bin/python

import sys
import os

#print ("numero argumentos"), len(sys.argv)
usuario =sys.argv[1]
clave = sys.argv[2]
basedatos = sys.argv[3]
cadena = "mysql -u " + usuario + " -p" + clave + " " + basedatos
print (cadena)
os.system (cadena)
