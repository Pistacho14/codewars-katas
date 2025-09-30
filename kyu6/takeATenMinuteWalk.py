def is_valid_walk(walk):
    coordinates = [0, 0]
    on_time = False
    if len(walk) == 10:
        on_time = True
    for direction in walk:
        if direction == 'n':
            coordinates[0] += 1
        elif direction == 'e':
            coordinates[1] += 1
        elif direction == 's':
            coordinates[0] -= 1
        else:
            coordinates[1] -= 1
    if on_time and coordinates == [0, 0]:
        return True
    return False
