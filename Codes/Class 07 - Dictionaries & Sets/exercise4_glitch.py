#REFAZER FAZENDO MAP (FAZER TESTE COM "aabb", "xyxy")

def character_count(astring):
    char = []
    for i in astring:
        if i not in char:
            char.append(i)
    return len(char)

def isomorphic(astring1, astring2):
    #se as strings tem a msm qntd de caracteres, sao isomorficas
    if character_count(astring1) == character_count(astring2):
        return f"'{astring1}' and '{astring2}' are isomorphic"
    else:
        return f"'{astring1}' and '{astring2}' are not isomorphic"