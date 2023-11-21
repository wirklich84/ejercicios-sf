import string


def validate_main(list_user: list) -> str:
    '''
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

    '''
    response = None

    if not validate_length(list_user):
        print("La lista debe tener al menos 2 elementos.")
        response = False
        return response

    if not validate_only_letters(list_user):
        print("Hay caracteres invalidos en la lista.")
        response = False
        return response

    if list_user[0].isupper():
        if not validate_alphabet_upper(list_user):
            print("Todos los elemetos de la lista debes ser mayusculas.")
            response = False
            return response
    else:
        if not validate_alphabet_lower(list_user):
            print("Todos los elemetos de la lista debes ser minusculas.")
            response = False
            return response

    if not validate_order(list_user):
        print("La lista debe estar en orden consecutivo.")
        response = False
        return response

    response = missing_letter(list_user)

    return response


def validate_length(list_user: list) -> bool:
    response = True
    if len(list_user) < 2:
        response = False

    return response


def validate_only_letters(list_user: list) -> bool:
    response = True
    for letter in list_user:
        if not letter.isalpha():
            response = False
            break

    return response


def validate_alphabet_upper(list_user: list) -> bool:
    response = True
    for letter in list_user:
        if letter.islower():
            response = False
            break

    return response


def validate_alphabet_lower(list_user: list) -> bool:
    response = True
    for letter in list_user:
        if letter.isupper():
            response = False
            break

    return response


def validate_order(list_user: list) -> bool:
    response = True
    first_element = list_user[0]
    second_element = list_user[1]
    alphabet = validate_type_alphabet(list_user)

    range_user = [
        index
        for index, letter in enumerate(alphabet)
        if letter == first_element or letter == second_element
    ]

    if (range_user[1] - range_user[0]) > 2:
        response = False

    return response


def validate_type_alphabet(list_user: list) -> list:
    '''
    Funcion que verifica la primera letra para determinar
    que tipo de alfabeto regresa.

    Ejemplo: ["O","Q","R","S"] - > ABCDEFGHIJKLMNOPQRSTUVWXY
             ["a","b","c","d","f"] -> abcdefghijklmnopqrstuvwxyz
    
    Argumento:
        - Lista del usuario (List)

    Retorno:
        Alfabeto mayuscula o minuscula

    '''
    alphabet = None

    if list_user[0].isupper():
        alphabet = string.ascii_uppercase
    else:
        alphabet = string.ascii_lowercase

    return alphabet


def missing_letter(list_user: list):
    '''
    Funcion principal que realiza la busqueda de la letra
    que no se encuentra en la lista proporcionada por el 
    usuario.

    Argumento:
        - Lista del usuario (List)

    Retorno:
        Letra que no esta en la lista.
    '''
    response = None
    first_element = list_user[0]
    last_element = list_user[-1]
    alphabet = validate_type_alphabet(list_user)

    new_list = []
    new_range = []

    new_range = [
        index
        for index, letter in enumerate(alphabet)
        if letter == first_element or letter == last_element
    ]

    new_list = [
        letter
        for index, letter in enumerate(alphabet)
        if index >= new_range[0] and index <= new_range[1]
    ]

    response = [letter for letter in new_list if letter not in list_user]

    if len(response) == 0:
        print("No hay letra que buscar")
        response = False
        return response
    else:
        response = response[0]

    return response
