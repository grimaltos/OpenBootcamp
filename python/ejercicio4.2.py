numeroinicial = int(input('Introduzca el numero inicial: '))
numerofinal = int(input('Introduzca el numero final: '))
while numerofinal <= numeroinicial:
    print(f'El numero final: {numerofinal} no es mayor que el numero inicial: {numeroinicial}')
    numerofinal = int(input('Introduzca el numero final correcto: '))
numnerospares = []

while numerofinal >= numeroinicial:
    if(numeroinicial % 2 == 0):
       numnerospares.append(numeroinicial)
    numeroinicial += 1
print(numnerospares)