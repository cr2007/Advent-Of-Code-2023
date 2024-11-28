import re

# Compile the regex pattern for efficiency
GAME_PATTERN = re.compile(r'^Game (\d+): (.*)$')

def parse_line(line: str) -> tuple[int, list]:
    match = GAME_PATTERN.match(line) # RegEx pattern
    subsets = []

    if match:
        # Splits up the game number and the sets
        game, lists = match.groups()
        lists = [s.strip() for s in lists.split("; ")]

        for s in lists:
            items = s.split(", ")
            set_result = {}

            for item in items:
                if item:
                    count, color = item.split()
                    set_result[color.lower()] = int(count)

            subsets.append(set_result)

        return (int(game), subsets)
    else:
        print(f"No match found for line: {line}")
        return -1, []


def valid_code(subsets: list[dict[str, int]], red=0, green=0, blue=0) -> bool:
    limits = {"red": red, "green": green, "blue": blue}

    for subset in subsets:
        for color, limit in limits.items():
            if limit and subset.get(color, 0) > limit:
                return False

    return True

def main():
    red, green, blue = 12, 13, 14
    possible_games = []

    file_path = "input.txt"
    with open(file_path, "r") as file:
        lines = (line.strip() for line in file)

        for game, info in (parse_line(line) for line in lines):
            if game != -1 and valid_code(info, red, green, blue):
                possible_games.append(game)

    # Display results
    print(f"Number of games: {len(possible_games)}")
    print(f"Sum of the game numbers: {sum(possible_games)}")

if __name__ == "__main__":
    main()
