#!/usr/bin/python

import sys
import os

usuario = sys.argv[1]
clave = sys.argv[2]

basedatos = input ("¿A que base de datos quieres hacerle una copia de seguridad?")
print ("Vas a copiar la base de datos:" + basedatos)

cadena = "mysqldump -u " + usuario + " -p" + clave + " " + basedatos + " | gzip > backup.sql.gz"
print (cadena)
os.system (cadena)

#mysqldump -u usuario -pclave basedatos | gzip > backup.sql.gz
