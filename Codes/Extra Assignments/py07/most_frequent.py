def most_frequent(alist):
    elements_frequency = {}

    for key in alist:
        elements_frequency[key] = elements_frequency.get(key, 0) + 1
    
    max_value = max(elements_frequency.values())
    max_keys = [key for key, value in elements_frequency.items() if value == max_value]
    
    for key in elements_frequency:
        if len(max_keys) > 1:
            key = max(max_keys)
            if elements_frequency[key] == max_value:
                return key
        if elements_frequency[key] == max_value:
                return key