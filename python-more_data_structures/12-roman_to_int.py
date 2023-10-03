#!/usr/bin/python3

def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.

    Args:
        roman_string (str): The Roman numeral to convert.

    Returns:
        int: Decimal notation of the Roman numeral,
        or None if the input is invalid.
    """
    if (not roman_string or not isinstance(roman_string, str)):
        # input is either None, or not a string ; returning default value
        return 0

    # Simple translation table from roman numerals to decimals
    table = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    decimal = 0
    length = len(roman_string)

    for i in range(0, length):
        # Ugly but had to respect 80-char limit
        if ((i + 1) < length
                and table[roman_string[i]] < table[roman_string[i + 1]]):
            # Special case: subtract numeral, then keep going to next numeral
            decimal -= table[roman_string[i]]
        else:
            # Usual case: find numeral value in the table and add to the sum
            decimal += table[roman_string[i]]
    return decimal
