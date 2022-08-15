from pydoc import importfile

import pydoc as p

f = open("python/Ejercicio8_1/ejemplo.txt", 'w')
f.write("Estoy escribiendo en el fichero por primera vez\n")
f.close
f = open("python/Ejercicio8_1/ejemplo.txt", 'a')
f.write("Se me ha olvidado añadir esto")
f.close