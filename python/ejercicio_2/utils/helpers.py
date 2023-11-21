def calculations(number: int) -> int:
    '''
    Se convierte los numeros en lista para posteriomente
    realizar las multiplicaciones correspondientes.

    Argumentos:
        - number (int)

    Retorno:
        resultado de los numeros multiplicados (int)
    
    '''
    list_numbers = [int(x) for x in str(number)]

    response = 1

    for num in list_numbers:
        response = response * num

    return response

