import copy

def distance_apple(snake_cords, apple_cords, max_x, max_y, dir):
    new_cords = copy.deepcopy(snake_cords)
    i = 0
    while 0 <= new_cords[0] <= max_x and 0 <= new_cords[1] <= max_y:
        if new_cords[0] == apple_cords[0] and new_cords[1] == apple_cords[1]:
            return i * 50
        i += 1
        new_cords[0] += dir[0] * 50
        new_cords[1] += dir[1] * 50
    return -1

def distance_wall(snake_cords, max_x, max_y, dir):
    new_cords = copy.deepcopy(snake_cords)
    i = -1
    while 0 <= new_cords[0] <= max_x and 0 <= new_cords[1] <= max_y:
        new_cords[0] += dir[0] * 50
        new_cords[1] += dir[1] * 50
        i += 1
    return i * 50

def distance_snake_part(snake_cords, max_x, max_y, dir):
    new_cords = copy.deepcopy(snake_cords[0])
    i = 0
    while 0 <= new_cords[0] <= max_x and 0 <= new_cords[1] <= max_y:
        if new_cords in snake_cords[1:]:
            return i * 50
        i += 1
        new_cords[0] += dir[0] * 50
        new_cords[1] += dir[1] * 50
    return -1

def generate_output(snake_cords, apple_cords, game_width, game_height):
    directions = [(0,-1), (0,1), (-1,0), (1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
    distances = []
    for dir in directions:
        distances.append(distance_wall(snake_cords[0], game_width, game_height, dir))
        distances.append(distance_apple(snake_cords[0], apple_cords, game_width, game_height, dir))
        distances.append(distance_snake_part(snake_cords, game_width * 50, game_height, dir))
    return distances