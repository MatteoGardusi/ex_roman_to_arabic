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


def convert_roman_to_arabic(data_input: str) -> str:
    """
    converte la stringa in ingresso in numero arabo
    :param data_input: stringa da convertire
    :return:
    """
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'CD': 400, 'CM': 900,
                  'IX': 9, 'XL': 40, 'XC': 90}
    roman_string = verifica_stringa_legale(data_input)
    i = 0
    arabic = 0
    while i < len(roman_string):
        if i + 1 < len(roman_string) and roman_string[i:i + 2] in roman_dict:
            arabic += roman_dict[roman_string[i:i + 2]]
            i += 2
        else:
            arabic += roman_dict[roman_string[i]]
            i += 1
    return str(arabic)


print(convert_roman_to_arabic(input('Inserisci un numero romano: ')))

'''
test_roman = open("numeri_romani.txt")
numeri = test_roman.read().split()
numeri_def = []
for num in range(len(numeri)):
    if num % 2 == 1:
        numeri_def.append(numeri[num])

lista = []
for num in numeri_def:
    lista.append(convert_roman_to_arabic(num))
cont = 0
for i, num in zip(range(1, len(lista)+1), lista):
    if int(i) == int(num):
        cont += 1
print(cont)
'''
