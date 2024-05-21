def search_tree(key, tree, keys_list = []):
    if tree == None:
        return None
    else:
        (k, value, left, right) = tree
        new_keys_list = keys_list + [k] # n usar o append pq o moodle n usa o python mais novo
        if key == k:
            return (value, new_keys_list)
        if key < k:
            return search_tree(key, left, new_keys_list)
        else:
            return search_tree(key, right, new_keys_list)

# se n pudesse criar o parametro auxiliar "keys_list", deveria usar a funcao resposta so
# para dar return em f_aux e usar f_aux para fazer oq quiser