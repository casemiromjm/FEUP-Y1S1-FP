def fight(heroes, villain):
    for hero in heroes:
        if hero["category"] != villain["category"]:
            continue
        if hero["health"] >= villain["health"]: #hero wins
            hero["score"] += 1
            return f"{ hero['name']} defeated the villain and now has a score of {hero['score']}"
        else: #villain won that fight
            villain['health'] = villain['health'] - (hero['health']/2)
    
    villain['health'] = round(villain['health'], 1)
    return f"{villain['name']} prevailed with {villain['health']}HP left"