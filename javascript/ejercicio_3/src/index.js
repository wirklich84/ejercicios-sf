import { validateMain } from "./utils/helpers.js";

function findMissingLetter(listUser) {
    /*
    Funcion que busca la letra que no se 
    encuenta en la lista.

    Argumentos:
        - Lista de letras (list)

    Retorna:
        Letra que no esta en la lista.
    */
    let response = validateMain(listUser)
    return response
}

export { findMissingLetter }