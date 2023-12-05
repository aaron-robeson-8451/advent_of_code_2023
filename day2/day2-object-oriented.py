import pandas as pd
import re
import math
filename = 'input.txt'
# filename = 'input_small.txt'

with open(filename, 'r') as file:
    input_string = file.read()

lines = input_string.split('\n')[0:-1]


# Part 1

class Game:
    def __init__(self, game_number, draws):
        self.game_number: int = game_number
        self.draws: List[Draw] = draws
        # Constraints
        self.n_red = 12
        self.n_green = 13
        self.n_blue = 14
    
    def __repr__(self):
        return f'Game {self.game_number}: {self.draws}\n'

    def check_self(self):
        # Check if all draws are possible given constraints
        for r in self.draws:
            if not self.check_draw(r, self.n_red, self.n_green, self.n_blue):
                return False
        return True
    
    @staticmethod
    def check_draw(r, n_red, n_green, n_blue):
        # Check if draw is possible given constraints
        if r['red'] > n_red:
            return False
        if r['green'] > n_green:
            return False
        if r['blue'] > n_blue:
            return False
        return True
    
    def get_minimum_reqs(self):
        # Get the maximum number of each color across all draws
        min_reqs = {}
        for color in ['red','green','blue']:
            min_reqs[color] = max([r[color] for r in self.draws])
        return min_reqs

def parse_draw(draw):
    # Parse draw
    r = {}
    for color in ['red', 'green', 'blue']:
        if color in draw:
            r[color] = int(re.search(fr'(\d+)(?=\s{color})', draw).group(1))
        else:
            r[color] = 0
    return r

def parse_line(line):
    game_number = line.split(':')[0].split(' ')[1]
    draws = line.split(':')[1].split(';')

    # Parse draws
    parsed_draws = []
    for draw in draws:
        parsed_draw = parse_draw(draw)
        parsed_draws.append(parsed_draw)
    game = Game(game_number, parsed_draws)
    
    return game

# Load games
games = []
for line in lines:
    games.append(parse_line(line))

# Check games with constraints
playable_games = 0
for game in games:
    if game.check_self():
        playable_games += int(game.game_number)
print('Part 1:', playable_games)


# Part 2
power_sum = 0
for game in games:
    min_reqs = game.get_minimum_reqs()
    power = math.prod(min_reqs.values())
    power_sum += power
print('Part 2:', power_sum)

# 2286 is too low