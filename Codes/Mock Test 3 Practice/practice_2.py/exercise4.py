def list_paths(dirtree):
    #str represents a file name
    #a tuple (dir, subtree) of the name of a directory, as a string, plus a list os subtrees

    if type(dirtree) == str:
        return dirtree
    
    path_list = []
    for element in dirtree[1]:
        aux = list_paths(element)

        #element is a file
        if type(aux) == str:
            path_list.append(dirtree[0] + "/" + aux)
        
        #element is not a file, is a ful dir
        else:
            for item in aux:
                path_list.append(dirtree[0] + "/" + item)

    return path_list


print(list_paths(("Home", [("a", []), ("b", ["b.py", "b.c"]), ("c", []), "d.py", "e.c"])))
print(list_paths(("home", [("a", ["f.txt","g.py"]), ("b", ["f.py","g.c"]), ("d",["f.dat"])])))
print(list_paths(("home", [("a", []), ("b", []), ("c", [])])))
print(list_paths(("root", [("a",[("e",["i"]),"f.py","g.c", "h.lst"]),"b.txt", "c.dat", ("d", ["j","d.py","d.ext","k"])])))