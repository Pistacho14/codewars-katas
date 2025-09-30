def dir_reduc(arr):
    coordinate_x = 0
    coordinate_y = 0
    clean_directions = []
    for direction in arr:
        if direction == 'NORTH':
            coordinate_x += 1
        elif direction == 'WEST':
            coordinate_y += 1
        elif direction == 'SOUTH':
            coordinate_x -=1
        elif direction == 'EAST':
            coordinate_y -= 1
    
    while coordinate_x or coordinate_y:
        if coordinate_y > 0:
            clean_directions.append('WEST')
        elif coordinate_y < 0:
            clean_directions.append('EAST')
        elif coordinate_x >0:
            clean_directions.append('NORTH')
        else:
            clean_directions.append('SOUTH')
    return clean_directions