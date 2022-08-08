import math
from re import I
def areatriangulo(altura, base):
    return base * altura / 2

def areacirculo(radio):
    return math.pi*radio**2

opcion = 0
print('Seleccione que desea hacer:')
print('1. Calcular área de un triangulo')
print('2. Calcular área de un círculo')
while opcion < 1 or opcion > 2:
    opcion = int(input('Opción: '))
match opcion:
    case 1:
        altura = float(input('Introduzca la altura del triángulo: '))
        base = float(input('Introduzca la base del triángulo: '))
        print(f'el área del triángulo es: {round(areatriangulo(altura, base),2)}')
    case 2:
        radio = float(input('Introduzca el radio del círculo: '))
        print(f'El área del círculo es: {round(areacirculo(radio),2)}')