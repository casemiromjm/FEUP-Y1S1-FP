#claudio

def above(tree, name, people_above = []):
    #tree is a pair with subpairs of (manager, managed)
    if type(tree) == str:
        if name == tree and len(people_above) > 0:
            return people_above
        else:
            return None
    if name == tree[0]:
        if len(people_above) > 0:
            return people_above
        else:
            None
    for person in tree[1]:
        final_res = above(person, name, people_above = people_above + [tree[0]])
        if final_res:
            return final_res