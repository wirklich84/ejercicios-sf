def validate_pin(pin: str) -> bool:
    '''
    Validacion del PIN

    Argumentos: 
        - PIN (str)

    Retorna: 
        True or False (bool)
    '''
    if not pin.isnumeric():
        return False

    if (len(pin) < 4 or len(pin) > 6 or len(pin) == 5):
        return False

    return True