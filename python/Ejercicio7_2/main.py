import time
import operahora

horalimite = time.strptime("19:00:00", "%H:%M:%S")
horaactual = time.strptime(time.strftime("%X"), "%H:%M:%S")

horalimitesec = operahora.horasasegundos(horalimite)
horaactualsec = operahora.horasasegundos(horaactual)
difhoras = horalimitesec - horaactualsec

if difhoras <= 0:
    print("¡¡¡A Casa!!!!")
else:
    print("¡A currar! Quedan", operahora.segundosahora(difhoras), "horas")