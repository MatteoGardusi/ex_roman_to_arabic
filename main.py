def verifica_stringa_legale(data_in: str):
    """
    Riceve una stringa e verifica se i caratteri
    sono legali
    :param data_in: stringa da controllare
    :return:
    """
    legal_symbol = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
    data_in = data_in.upper()
    for char in data_in:
        if char in legal_symbol:
            pass
        else:
            raise ValueError
    return data_in


def convert_roman_to_arabic(roman: str) -> str:
    """
    convert a string containing a number in roman coding to a
    string containing the number in arabic (positinal) coding
    :param roman: string to be converted
    :return: converted string
    """
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                  'CD': 400, 'CM': 900}
    roman_string = verifica_stringa_legale(roman)
    i = 0
    arabic = 0
    while i < len(roman_string):
        if i + 1 < len(roman_string) and roman[i:i + 2] in roman_dict:
            arabic += roman_dict[roman_string[i:i + 2]]
            i += 2
        else:
            # print(i)
            arabic += roman_dict[roman_string[i]]
            i += 1
    return str(arabic)


print(convert_roman_to_arabic(input('Inserisci un numero romano: ')))
