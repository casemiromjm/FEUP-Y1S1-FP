def min_path(path):
    minimized_path = []
    opposite_directions = {"UP":"DOWN", "DOWN":"UP", "RIGHT":"LEFT", "LEFT":"RIGHT"}
    for direction in path:
        if minimized_path and minimized_path[-1] == opposite_directions.get(direction):
            minimized_path.pop()
        else:
            minimized_path.append(direction)

    return minimized_path