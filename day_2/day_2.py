from typing import Dict, List
import re

class GameChecker:
    DEFAULT_FILENAME = 'test.txt'
    DEFAULT_CONSTRAINTS = {
        'red': 12,
        'green': 13,
        'blue': 14
    }


    def __init__(self, filename: str = DEFAULT_FILENAME, constraints: Dict[str, int] = None):
        self.filename = filename
        self.constraints = constraints or self.DEFAULT_CONSTRAINTS
        self.game_dict = None  
        self.power_sum = 0 # sum of the powers of the min colors of each valid game


    def parse_games(self) -> Dict[str, List[Dict[str, int]]]:
        """
        Parse the games from the specified file and set the instance variable game_dict.
        """
        self.game_dict = {}
        with open(self.filename, 'r') as f:
            for content in f:
                match = re.match(r'Game (\d+): (.+)', content)
                if match:
                    game_number, game_content = match.groups()
                    self.game_dict[game_number] = []
                    parts = game_content.split(';')
                    for part in parts:
                        part = part.strip()
                        color_counts = {}
                        color_matches = re.findall(r'(\d+) (\w+)', part)
                        for count, color in color_matches:
                            color_counts[color] = int(count)
                        self.game_dict[game_number].append(color_counts)
        return self.game_dict


    def check_and_add_games(self) -> int:
        """
        Check games against constraints and return the sum of valid games.
        """
        game_sum = 0
        for game in self.game_dict:
            if not self.should_skip_game(self.game_dict[game]):
                game_sum += int(game)
        return game_sum


    def should_skip_game(self, cubes_list: List[Dict[str, int]]) -> bool:
        """
        Check if a game should be skipped based on constraints.
        """
        for cubes in cubes_list:
            for color in self.constraints:
                if cubes.get(color, 0) > self.constraints[color]:
                    return True
        return False


    def minimum_cubes(self):
        """
        Find minimum number of cube color for every game and sum the multiplied value of those minimums
        """
        for game in self.game_dict:
            min_colors = {'red': 0, 'green': 0, 'blue': 0}
            for cubes in self.game_dict[game]:
                for color in cubes:
                    min_colors[color] = max(int(cubes[color]), min_colors[color])
            self.power_sum += min_colors['red'] * min_colors['green'] * min_colors['blue']
        return self.power_sum
        


if __name__ == "__main__":
    game_checker = GameChecker()

    # Part 1
    games = game_checker.parse_games()
    result = game_checker.check_and_add_games()
    print(result)

    # Part 2
    game_checker.minimum_cubes()
    print(game_checker.power_sum)

