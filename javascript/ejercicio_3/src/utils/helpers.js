function validateMain(listUser) {
    /*
    Funcion principal de validacion
    realiza todas las validaciones correspondientes:
        - Validacion de longitud de lista
        - Validacion de solo numeros.
        - Valdacion de mayusculas y minusculas.
        - Validacion de secuencia de elementos.

    Argumentos:
        Lista del usuario (list)

    Retorno:
        Letra que no se encuentra en la lista.

    */
    let response = null

    if (!validateLength(listUser)) {
        console.log("La lista debe tener al menos 2 elementos.")
        response = false
        return response
    }

    if (!validateOnlyLetters(listUser)) {
        console.log("Hay caracteres invalidos en la lista.")
        response = false
        return response
    }

    if (listUser[0] == listUser[0].toUpperCase()) {
        if (!validateAlphabetUpper(listUser)) {
            console.log("Todos los elemetos de la lista debes ser mayusculas.")
            response = false
            return response
        }
    } else {
        if (!validateAlphabetLower(listUser)) {
            console.log("Todos los elemetos de la lista debes ser minusculas.")
            response = false
            return response
        }
    }

    if (!validateOrder(listUser)) {
        console.log("La lista debe estar en orden consecutivo.")
        response = false
        return response
    }

    response = missingLetter(listUser)

    return response
}

function validateLength(listUser) {
    let response = true
    if (listUser.length < 2) {
        response = false
    }
    return response
}


function validateOnlyLetters(listUser) {
    let response = true
    let expRegOnlyLetter = "^[a-zA-ZñÑáéíóúÁÉÍÓÚ]+$"

    let findElement = listUser.some(element => {
        return element.match(expRegOnlyLetter) == null
    })

    if (findElement) {
        response = false
    }

    return response
}


function validateAlphabetUpper(listUser) {
    let response = true
    let expRegOnlyUpper = "^[a-zÑÁÉÍÓÚ]+$"

    let findElement = listUser.some(element => {
        return element.match(expRegOnlyUpper) != null
    })

    if (findElement) {
        response = false
    }
    return response
}

function validateAlphabetLower(listUser) {
    let response = true
    let expRegOnlyLower = "^[A-ZÑÁÉÍÓÚ]+$"

    let findElement = listUser.some(element => {
        return element.match(expRegOnlyLower) != null
    })

    if (findElement) {
        response = false
    }
    return response
}

function validateTypeAlphabet(listUser) {
    /*
    Funcion que verifica la primera letra para determinar
    que tipo de alfabeto regresa.

    Ejemplo: ["O","Q","R","S"] - > ABCDEFGHIJKLMNOPQRSTUVWXY
             ["a","b","c","d","f"] -> abcdefghijklmnopqrstuvwxyz
    
    Argumento:
        - Lista del usuario (List)

    Retorno:
        Alfabeto mayuscula o minuscula

    */
    let alphabet = null
    let alphabetUpper = "ABCDEFGHIJKLMNOPQRSTUVWXY"
    let alphabetLower = "abcdefghijklmnopqrstuvwxyz"

    if (listUser[0] == listUser[0].toUpperCase()) {
        alphabet = alphabetUpper
            .split('')
            .map((letter) => { return letter })
    } else {
        alphabet = alphabetLower
            .split('')
            .map((letter) => { return letter })
    }

    return alphabet
}

function validateOrder(listUser) {
    let response = true
    let firstElement = listUser[0]
    let secondElement = listUser[1]
    let alphabet = validateTypeAlphabet(listUser)

    let rangeUser = [...alphabet.entries()]
        .filter(([index, letter]) => letter == firstElement || letter == secondElement)
        .map(([index]) => index);

    if ((rangeUser[1] - rangeUser[0]) > 2) {
        response = false
    }

    return response
}

function missingLetter(listUser) {
    /*
    Funcion principal que realiza la busqueda de la letra
    que no se encuentra en la lista proporcionada por el 
    usuario.

    Argumento:
        - Lista del usuario (List)

    Retorno:
        Letra que no esta en la lista.
    */
    let response = null
    let firstElement = listUser[0]
    let lastElement = listUser.slice(-1).toString()
    let alphabet = validateTypeAlphabet(listUser)

    let rangeUser = [...alphabet.entries()]
        .filter(([index, letter]) => letter == firstElement || letter == lastElement)
        .map(([index]) => index);

    let newList = [...alphabet.entries()]
        .filter(([index, letter]) => index >= rangeUser[0] && index <= rangeUser[1])
        .map(([index, letter]) => letter)

    response = newList.filter(letter => !listUser.includes(letter)).map(letter => letter);

    if (response.length == 0) {
        console.log("No hay letras que buscar.")
        return false
    } else {
        response = response.toString()
        return response
    }

}




export { validateMain }