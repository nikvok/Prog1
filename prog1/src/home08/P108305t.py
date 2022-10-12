import sys
from typing import NamedTuple

LegoSet = NamedTuple("LegoSet", [("number", int),("name", str),("theme",str),("pieces",int)])

def line_to_lego_set(line: str) -> LegoSet:
    tokens = line.strip().split(";")
    return LegoSet(int(tokens[0]),tokens[1],tokens[2],int(tokens[3]))

def lego_set_to_line(lego_set: LegoSet) -> str:

    return f"{lego_set.name} ({lego_set.number}): {lego_set.pieces} - {lego_set.theme}"
def sort_lego_sets(lego_set):
#def sort_lego_sets(lego_sets: list[LegoSet]) -> list(LegoSet):
    return sorted(lego_set, key=lambda lego_set: (lego_set.theme, lego_set.name, lego_set.number))
#   return sorted(lego_sets, key=lambda lego_set: (lego_set.theme, lego_set.name, lego_set.number))


#parameterekkel nem mukodik -\°°/-
def main():
    lego_sets = []
    while True:
        line = input()
        if line == "END":
            break
        lego_sets.append(line_to_lego_set(line.strip()))
    lego_sets = sort_lego_sets(lego_sets)
    for lego_set in lego_sets:
        print(lego_set_to_line(lego_set))
if __name__ == "__main__":
    main()

