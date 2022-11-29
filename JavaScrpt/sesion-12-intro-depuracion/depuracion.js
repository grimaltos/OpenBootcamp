function fibo(num){

    let listafibo = [0, 1]

    for(let i=2; i<= num; i++){
        listafibo = [...listafibo, listafibo[i-1] + listafibo[i-2]]
    }

    return listafibo
}

listafinal = fibo(10)

console.log(listafinal)