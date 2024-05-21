def camel_case(phrase):
    next_upper = False
    camel_phrase = ""
    for char in phrase:
        if char.isalpha():
            if next_upper:
                camel_phrase = camel_phrase + char.upper()
                next_upper = False
            else:
                camel_phrase = camel_phrase + char.lower()
        else:
            next_upper = True
    return camel_phrase