def rm_letter_rev(ch, s):
    result = " "
    for c in s:
        if c != ch:
            result = c + result
    return result