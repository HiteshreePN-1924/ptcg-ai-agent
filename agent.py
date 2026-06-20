def choose_best_move(state):
    moves = ["attack", "retreat", "heal"]

    best_move = None
    best_score = -999

    for move in moves:
        score = evaluate(move, state)

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def evaluate(move, state):
    if move == "attack":
        return 10 + state["energy"]

    if move == "retreat":
        return 5 if state["hp"] < 40 else 0

    if move == "heal":
        return 7

    return 0
