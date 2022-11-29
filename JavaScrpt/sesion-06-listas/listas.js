let listaCompra = ['Pan', 'Leche', 'Yogurth', 'Naranjas', 'Tomates']

listaCompra.push('Aceite de girasol')

listaCompra.pop()

let pelisFav = [
    {
        titulo: 'Matrix',
        director: 'Hermanas Wachowski',
        anyo: 1999
    },
    {
        titulo: 'Titanic',
        director: 'James Cameron',
        anyo: 1997
    },
    {
        titulo: 'Grease',
        director: 'Randal Kleiser',
        anyo: 1978
    }
]

const pelis2010 = pelisFav.filter(peli => peli.anyo > 2010)
const pelisDirect = pelisFav.map(peli => peli.director)
const pelisTittle = pelisFav.map(peli => peli.titulo)
const direcTitle_list = pelisDirect.concat(pelisTittle)
const direcTitle_list2 = [...pelisDirect, ...pelisTittle]
