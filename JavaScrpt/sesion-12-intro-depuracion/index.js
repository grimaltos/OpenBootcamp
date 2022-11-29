const persona = {
    nombre: 'Vicent',
    edad: 35
}

console.log(persona)

function obtenDobleEdad(edad){
    return 2 * edad
}

const dobleEdad = obtenDobleEdad(persona.edad)

persona.edad = dobleEdad

console.log(dobleEdad)