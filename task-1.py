def int_to_roman(num):
    # Define Roman numeral mappings
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    # Convert integer to Roman numeral
    roman_string = ""
    for value, symbol in roman_numerals:
        while num >= value:
            roman_string += symbol
            num -= value
    return roman_string

# Testing the function with an example
int_to_roman(27)
