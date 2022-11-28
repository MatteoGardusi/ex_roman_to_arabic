def verifica_stringa_legale(data_in: str) -> str:
    """
    Riceve una stringa e verifica se i caratteri
    sono legali
    :param data_in: stringa da controllare
    :return:
    """
    legal_symbol = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
    data_in = data_in.upper()
    for char in data_in:
        if char not in legal_symbol:
            return "Hai inserito un carattere illegale"
    return data_in


def convert_roman_to_arabic(roman: str) -> str:
    """
    convert a string containing a number in roman coding to a
    string containing the number in arabic (positinal) coding
    :param roman: string to be converted
    :return: converted string
    """

    return str(arabic)


roman_string = verifica_stringa_legale(input('Scrivi un numero romano: '))
print(roman_string)
