from utils.helpers import validate_main


def find_missing_letter(list_user: list):
    '''
    Funcion que busca la letra que no se 
    encuenta en la lista.

    Argumentos:
        - Lista de letras (list)

    Retorna:
        Letra que no esta en la lista.
    '''
    response = validate_main(list_user)

    return response
