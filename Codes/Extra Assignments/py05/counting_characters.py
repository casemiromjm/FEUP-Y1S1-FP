def count_chars(a_string):
    count_alpha = 0
    count_digit = 0
    count_symbol = 0
    for char in a_string:
        if char.isalpha():
            count_alpha += 1
        elif char.isdigit():
            count_digit += 1
        elif char.isascii():
            count_symbol += 1
    
    return (count_alpha, count_digit, count_symbol)