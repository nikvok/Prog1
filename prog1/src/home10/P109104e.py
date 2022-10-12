from typing import NamedTuple

LegoSet = NamedTuple("LegoSet", [("number", int), ("name", str), ("theme", str), ("pieces", int)])

def line_to_lego_set(line: str) -> LegoSet:
    tokens = line.strip().split(";")
    return LegoSet(int(tokens[0]), tokens[1], (tokens[2]), int(tokens[3]))

def distinct_themes(lego_sets: list[LegoSet]) -> set[str]:
    result = set()
    for i in range(len(lego_sets)):
        result.add(lego_sets[i][2])
    return result

def main():
    result = []
    while True:
        line = input()
        if line == "EOF":
            break
        result.append(line_to_lego_set(line.strip(";")))
    print(distinct_themes(result))

if __name__ == "__main__":
    main()
