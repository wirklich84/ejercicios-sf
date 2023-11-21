from utils.helpers import calculations


def persistence(number: int) -> int:
    '''
    Funcion que realiza la persistencia multiplicativa de un número.
    Ejemplo: (Porque 3*9 = 27, 2*7 = 14, 1*4 = 4 y 4 tiene solo un dígito)

    Argumetos:
        - number (int)

    Retorno:
        No. de pasos para llegar a un digito.

    '''
    no_steps = 0

    if len(str(number)) == 1:
        return 0
    else:
        while True:
            response = calculations(number)
            if len(str(response)) == 1:
                no_steps += 1
                return no_steps
            else:
                no_steps += 1
                number = response