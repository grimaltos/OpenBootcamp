class Estudiante{
    nombre
    asignaturas
    constructor(nombre){
        this.nombre = nombre
        this.asignaturas = ['Javasdcript', 'HTML', 'CSS'] 
    }

    obtenDatos(){
        return {
            nombre: this.nombre,
            asignaturas: this.asignaturas
        }
    }
}

let vicent = new Estudiante('Vicent')

console.log(vicent.obtenDatos())