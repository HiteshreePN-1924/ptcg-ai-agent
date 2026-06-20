import random

def choose_best_move(state):
    moves = ["attack", "retreat", "heal"]

    scored_moves = []

    for move in moves:
        score = evaluate(move, state)
        scored_moves.append((move, score))

    # sort by best score
    scored_moves.sort(key=lambda x: x[1], reverse=True)

    best_score = scored_moves[0][1]

    # add controlled randomness (AI-like behavior)
    top_moves = [m for m, s in scored_moves if s == best_score]

    return random.choice(top_moves)


def evaluate(move, state):
    hp = state.get("hp", 50)
    energy = state.get("energy", 0)
    opponent_hp = state.get("opponent_hp", 50)

    score = 0

    # ATTACK logic
    if move == "attack":
        score += energy * 5
        score += (100 - opponent_hp) * 0.2

    # RETREAT logic
    if move == "retreat":
        score += 30 if hp < 35 else 5

    # HEAL logic
    if move == "heal":
        score += 20 if hp < 50 else 8

    # noise for variability
    score += random.uniform(0, 3)

    return score
