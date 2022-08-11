class Alumno:
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)


    def resultado(self):
        if self.nota >= 5:
            print("Aprobado")
        else:
            print("Suspenso")

a1 = Alumno()
a2 = Alumno()

a1.inicializar("Vicent", 10)
a2.inicializar("Merche", 4.9)

a1.imprimir()
a1.resultado()
a2.imprimir()
a2.resultado()