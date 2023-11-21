import { calculations } from './utils/helpers.js'

function persistence(number) {
    /*
    Funcion que realiza la persistencia multiplicativa de un número.
    Ejemplo: (Porque 3*9 = 27, 2*7 = 14, 1*4 = 4 y 4 tiene solo un dígito)

    Argumetos:
        - number (int)

    Retorno:
        No. de pasos para llegar a un digito.

    */
    let noSteps = 0
    let response = null
    let loop = true

    if (number.toString().length == 1) {
        return response = 0
    } else {

        while (loop == true) {
            response = calculations(number)

            if (response.toString().length == 1) {
                noSteps += 1
                return noSteps
            } else {
                noSteps += 1
                number = response
            }
        }

    }
}

export { persistence }




