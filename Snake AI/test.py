from util import print_grid, generate_output

snake_cords = [(150, 100), (150, 150), (150, 200)]  # Just a sample snake coordinate list
head_cords = (150, 100)
apple_cords = (100,100)
game_width = 950
game_height = 950

output_sample = generate_output(snake_cords, head_cords, apple_cords, game_width, game_height)
print_grid(output_sample)
print(output_sample[-1], output_sample[-2])