def horasasegundos(hora):
    segundos = hora.tm_hour * 3600
    segundos += hora.tm_min * 60
    segundos += hora.tm_sec

    return segundos

def segundosahora(segundos):
    horas = int(segundos / 3600)
    segundos -= horas * 3600
    minutos = int((segundos/60))
    segundos -= minutos * 60

    return f"{horas:}:{minutos}:{segundos}"