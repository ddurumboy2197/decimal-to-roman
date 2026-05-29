def decimal_to_roman(num):
    if not isinstance(num, int) or num < 1 or num > 3999:
        return None

    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    roman_num = ''
    for value, numeral in roman_numerals.items():
        while num >= value:
            roman_num += numeral
            num -= value

    return roman_num

print(decimal_to_roman(4))  # IV
print(decimal_to_roman(9))  # IX
print(decimal_to_roman(13))  # XIII
print(decimal_to_roman(44))  # XLIV
print(decimal_to_roman(1000))  # M
