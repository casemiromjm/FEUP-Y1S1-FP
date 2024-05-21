def move_disk(from_pole, to_pole, count):
    """An auxiliar function to print a single move instruction."""
    print(f"{count}. Move disk from {from_pole} to {to_pole}")

def move_tower(height, from_pole, to_pole, with_pole, count):
    if height == 1:
        move_disk(from_pole, to_pole, count)
    else:
        move_tower(height - 1, from_pole, with_pole, to_pole, count)
        count2 = count + (2**(height-1) -1)
        move_disk(from_pole, to_pole, count2)
        move_tower(height-1, with_pole, to_pole, from_pole, count2+1)