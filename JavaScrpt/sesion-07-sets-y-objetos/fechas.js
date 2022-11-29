const hoy = new Date()
console.log(hoy)
const fechaNacimiento = new Date(1987, 0, 28)
console.log(fechaNacimiento)

let masTarde = hoy.getTime() > fechaNacimiento.getTime()

console.log(masTarde)

const diaNacimiento = fechaNacimiento.getDate()
console.log(diaNacimiento)

const mesNacimiento = fechaNacimiento.getMonth() + 1
console.log(mesNacimiento)

const anyoNacimiento = fechaNacimiento.getFullYear()
console.log(anyoNacimiento)