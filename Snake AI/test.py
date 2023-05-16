from util import generate_output

snake_cords = [[0, 950], [0, 900], [0, 850]]

apple_cords = (150, 800)

game_height = 950

game_width = 950

current_dir = (-1,0)

print("snake head")
print(snake_cords[0])
print("")
print("snake tail")
print(snake_cords[-1])
print("")
print("apple cords")
print(apple_cords)
print("")
print("game_height")
print(game_height)
print("")
print("game_width")
print(game_width)
print("")
print("output")
print(generate_output(snake_cords, apple_cords, game_width, game_height))