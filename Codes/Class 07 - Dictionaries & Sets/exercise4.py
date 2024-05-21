def get_mapping(string1, string2):
        mapping = {}
        for char1, char2 in zip(string1, string2):
            if char1 not in mapping:
                mapping[char1] = char2
            elif mapping[char1] != char2:
                return None  # Mapping conflict, not isomorphic
        return mapping

def isomorphic(astring1, astring2):
    forward_mapping = get_mapping(astring1, astring2)
    backward_mapping = get_mapping(astring2, astring1)

    if forward_mapping is not None and backward_mapping is not None:
        return f"'{astring1}' and '{astring2}' are isomorphic"
    else:
        return f"'{astring1}' and '{astring2}' are not isomorphic"