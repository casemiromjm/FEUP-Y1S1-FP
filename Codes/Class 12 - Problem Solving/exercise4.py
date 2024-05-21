def move_ball(board):
    if "E" in str(board):
        mov = (0, 1)
    elif "W" in str(board):
        mov = (0, -1)
    elif "S" in str(board):
        mov = (1, 0)  # referencial dos y está ao contrario
    elif "N" in str(board):
        mov = (-1, 0)
    res = []
    new_pos = pos_inicial(board, ["E", "W", "S", "N"])
    res.append(new_pos)
    while True:
        new_pos = (new_pos[0] + mov[0], new_pos[1] + mov[1])

        res.append(new_pos)

        if board[new_pos[0]][new_pos[1]] == "X":
            break
        elif board[new_pos[0]][new_pos[1]] == "\\":
            mov = (mov[1], mov[0])
        elif board[new_pos[0]][new_pos[1]] == "/":
            mov = (-mov[1], -mov[0])
    return res


def pos_inicial(board, lista):
    for j in lista:
        for i in range(len(board)):
            if j in board[i]:
                return (i, board[i].index(j))
