const yo = {
    nombre: 'Vicent',
    apellido: 'Grimaltos',
    edad: 35,
    altura: 179,
    eresDesarrollador: false
}

const miedad = yo.edad;

const pandilla = [
    {...yo},
    {
    nombre: 'Vicent',
    apellido: 'Pérezz',
    edad: 31,
    altura: 175,
    eresDesarrollador: false

    },
    {
    nombre: 'Edu',
    apellido: 'Vidal',
    edad: 42,
    altura: 181,
    eresDesarrollador: false
    }
]

const pandillaPorEdad = pandilla.sort((a, b) => a.edad - b.edad)

console.log(pandilla)