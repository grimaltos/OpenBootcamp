class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas={}

    def setNota(self, asignatura, nota):
        self.notas.update({asignatura: nota})

    def dameNotas(self):
        return self.notas

    def __str__(self):
        return "Notas de {}".format(self.nombre)

vicent = Alumno("Vicent")

vicent.setNota("Python", 10)
vicent.setNota("Java", 6)
print(vicent)
notas = vicent.dameNotas()
for x, y in notas.items():
    print(x, ' --> ', y)
    if(y >= 5):
        print("APROBADA")
    else:
        print("SUSPENSA")