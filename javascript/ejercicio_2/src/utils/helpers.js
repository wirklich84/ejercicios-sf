function calculations(number) {
    /*
    Se convierte los numeros en lista para posteriomente
    realizar las multiplicaciones correspondientes.

    Argumentos:
        - number (int)

    Retorno:
        resultado de los numeros multiplicados (int)
    
    */
    let response = 1

    let arrayNumbers = number.toString()
        .split('')
        .map((num) => {
            return Number(num)
        })

    arrayNumbers.forEach((num) => {
        response = (response * num)
    })

    return response
}

export { calculations }