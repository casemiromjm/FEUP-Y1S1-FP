def mask_data(data, n_characters, position):
    if n_characters == 0:
        return data
    elif n_characters < 0 or n_characters > len(data):
        return len(data) * "*"
    else:
        if position == "begin":
            sliced_str = data[n_characters:]
            masked_str = str(n_characters * "*") + sliced_str
            return masked_str
        else:
            sliced_str = data[:(len(data) - n_characters)]
            masked_str = sliced_str + str(n_characters * "*")
            return masked_str