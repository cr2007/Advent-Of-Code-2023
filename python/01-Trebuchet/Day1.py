import re
from typing import Generator, Any

def parse_file(file_path: str) -> Generator[int, Any, None]:
    with open(file_path, "r", encoding="utf-8") as file:
        lines = (line.strip() for line in file)

        for line in lines:
            result = re.findall(r'\d', line)
            if result:
                yield int(result[0] + result[-1])
            else:
                break

calibration_values: list[int] = list(parse_file("input.txt"))

print(sum(calibration_values))
