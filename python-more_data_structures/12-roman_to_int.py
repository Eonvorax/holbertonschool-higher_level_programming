#!/usr/bin/python3

def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.

    Args:
        roman_string (str): The Roman numeral to convert.

    Returns:
        int: Decimal notation of the Roman numeral,
        None if the input is invalid.
    """
    if (not roman_string or not isinstance(roman_string, str)):
        # input is either None, or not a string ; returning default value
        return 0

    # Simple translation table from roman numerals to decimals
    table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    decimal = 0
    length = len(roman_string)

    for i in range(0, length):
        if (roman_string[i] not in ("IVXLCDM")):
            # Input string is not a valid roman numeral
            return 0
        # More memory-intensive that I'd like but had to respect 80-char limit
        if ((i + 1) < length and roman_string[i:i+2] in ["IV", "IX"]):
            # Special case: subtract 1, then keep going to add 'V' or 'X' next
            decimal -= 1
        else:
            # Usual case: find numeral value in the table and add to the sum
            decimal += table[roman_string[i]]
    return decimal
