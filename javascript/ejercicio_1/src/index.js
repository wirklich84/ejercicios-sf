function validatePIN(pin) {
    /*
    Validacion del PIN

    Argumentos: 
        - PIN (str)

    Retorna: 
        True or False (bool)
    */

    if (!/^\d+$/.test(pin)) {
        return false;
    }

    if (pin.length < 4 || pin.length > 6 || pin.length === 5) {
        return false;
    }

    return true;

}

