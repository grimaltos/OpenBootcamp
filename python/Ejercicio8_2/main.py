import pickle
import pydoc as p

class Vehiculo:
    ruedas = 0
    puertas = 0
    color = ''

    def __init__(self, ruedas, puertas, color):
        self.ruedas = ruedas
        self.puertas = puertas
        self.color = color

v1 = Vehiculo(4, 5, 'gris')

f = open('python/Ejercicio8_2/savedobject.bin', 'wb')
pickle.dump(v1, f)
f.close

f = open('python/Ejercicio8_2/savedobject.bin', 'rb')
v2 = pickle.load(f)
f.close
print (v2.color)
