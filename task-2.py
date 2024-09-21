def roman_to_int(roman):
    # Define Roman numeral values
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    # Process each symbol in the Roman numeral
    for symbol in reversed(roman):
        value = roman_values[symbol]
        # Apply subtraction rule if a smaller value precedes a larger one
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total

# Testing the function with an example
roman_to_int("XXVII")
