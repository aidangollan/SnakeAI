import os
import neat
from pygame.locals import *
from Game import Game
import matplotlib.pyplot as plt
import neat.graphs as graphs

def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)
    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(fitness,50)

    print(winner)

def fitness(genomes, config):
    best_net = None
    best_fitness = 0
    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        game = Game(net, show=False)
        g.fitness = game.run()

        if g.fitness >= best_fitness:
            best_fitness = g.fitness
            best_net = net

    game = Game(best_net, show=True)
    game.run()

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)