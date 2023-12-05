import re

CONSTRAINTS = {
    'red': 12,
    'green': 13,
    'blue': 14
}

FILENAME = 'test.txt'

def parse_games() -> {}:
    game_dict = {}
    with open(FILENAME, 'r') as f:
        for content in f:
            match = re.match(r'Game (\d+): (.+)', content)
            game_number, game_content = match.groups()
            game_dict[game_number] = []
            parts = game_content.split(';')
            for part in parts:
                part = part.strip()
                color_counts = {}
                color_matches = re.findall(r'(\d+) (\w+)', part)
                for count, color in color_matches:
                    color_counts[color] = int(count)
                game_dict[game_number].append(color_counts)
            
    return game_dict
                
def check_and_add_games(game_dict: dict) -> int: 
    game_sum = 0
    skip_game = False
    for game in game_dict:
        print('on this game: ', game)
        if skip_game:
            print('setting skip back to False on this game: ', game)
            skip_game = False
            pass
        else:
            for cubes in game_dict[game]:
                print('on this set of colors: ', cubes)
                # print(cubes)
                if skip_game:
                    print('breaking out of this set of colors since skip is True: ', color, ' still on this game: ', game)
                    # print('skipping')
                    break
                for color in CONSTRAINTS:
                    print('on this one color: ', color)
                    # print(color)
                    if cubes.get(color):
                        if cubes[color] > CONSTRAINTS[color]:
                            # print('too big')
                            print('this color is not valid: ', cubes[color])
                            skip_game = True
                            break

        if not skip_game:
            print('adding game: ', game)
            game_sum += int(game)
            print(' game sum is now: ', game_sum)

    return game_sum



res = parse_games()
sum = check_and_add_games(res)
print(sum)