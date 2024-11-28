from typing import Generator, Any

NUMBERS = [
    "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine"
]

# Parse through the file
def parse_file(file_path: str) -> Generator[int, Any, None]:
    with open(file_path, "r", encoding="utf-8") as file:
        lines: Generator[str, Any, Any] = (line.strip() for line in file)

        for line in lines:
            results: list[str] = parse_line(line)

            if results:
                results = [
                    str(NUMBERS.index(result.lower()) + 1) if result.lower() in NUMBERS else result
                    for result in results
                ]
                yield int(results[0] + results[-1])
            else:
                break

# Parse through the line string within each line in the file
def parse_line(text: str):
    results = []
    index = 0

    while index < len(text):
        # Check for digits first
        if text[index].isdigit():
            results.append(text[index])
            index += 1
            continue

        for word in NUMBERS:
            if text[index:].startswith(word):
                results.append(word)
                index += len(word) - 2
                break

        index += 1

    return results

calibration_values: list[int] = list(parse_file("input.txt"))

print(sum(calibration_values))
