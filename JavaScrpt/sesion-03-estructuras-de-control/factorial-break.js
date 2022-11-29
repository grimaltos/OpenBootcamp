let factorial = 1
let contador = 1

while(true){
    factorial += factorial * contador
    console.log(factorial)
    if(contador===9)
    {
        break
    }
    contador++
}