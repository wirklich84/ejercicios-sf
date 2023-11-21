def array_diff(list_a: list, list_b: list) -> list:
    '''
    Funcion que recibe dos listas (A, B), se tomara como referencia
    los elementos que se encuentren en la lista B para buscarlos
    en la lista A y posterirmente retornar una nueva lista con solo
    los elementos que no estan en la lista B.

    Argumentos:
        - Lista A (List)
        - Lista B (List)
    
    Retorno:
        Lista filtrada.
    '''
    new_list = []
    new_index = []

    for b in list_b:
        for index, a in enumerate(list_a):
            if b == a:
                new_index.append(index)

    new_list = [value for index, value in enumerate(list_a) if index not in new_index]

    return new_list
