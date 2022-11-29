function siempreTrue(){
    return true
}

console.log(siempreTrue())

const holaPromesa = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve(console.log("Hola soy una promesa"))
    }, 2000);
})

holaPromesa
    .then()

function* generarId(){
    let id = 0
    while (true) {
        yield id
        id +=2
    }
}

const GId = generarId();

console.log(GId.next())
console.log(GId.next())
console.log(GId.next())