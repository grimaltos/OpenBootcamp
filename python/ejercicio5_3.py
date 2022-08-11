def esbisiesto(anyo):
    if (anyo % 4 == 0 & (anyo % 100 == 0 or anyo % 400 == 0)):
        return True

anyousuario = int(input('Introduzca el año: '))
if (esbisiesto(anyousuario)):
    print(f'En año {anyousuario} es bisiesto')
else:
    print(f'En año {anyousuario} NO es bisiesto')