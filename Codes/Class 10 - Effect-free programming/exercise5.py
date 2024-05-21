def transitive_closure(r):
    def composition(s1, s2):
        return {(a, c) for (a, b1) in s1 for (b2, c) in s2 if b1 == b2}

    def closure_helper(current_closure):
        new_closure = current_closure.union(composition(current_closure, r))
        if new_closure == current_closure:
            return new_closure
        else:
            return closure_helper(new_closure)

    return closure_helper(set(r))