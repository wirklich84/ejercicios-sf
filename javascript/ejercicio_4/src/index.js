function arrayDiff(listA, listB) {
    /*
    Funcion que recibe dos listas (A, B), se tomara como referencia
    los elementos que se encuentren en la lista B para buscarlos
    en la lista A y posterirmente retornar una nueva lista con solo
    los elementos que no estan en la lista B.

    Argumentos:
        - Lista A (List)
        - Lista B (List)
    
    Retorno:
        Lista filtrada.
    */
    let newIndex = [];

    for (let b of listB) {
        for (let [index, a] of listA.entries()) {
            if (b === a) {
                newIndex.push(index);
            }
        }
    }

    let newList = listA.filter((value, index) => !newIndex.includes(index));

    return newList
}

export { arrayDiff }
