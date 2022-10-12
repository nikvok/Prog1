def is_strictly_monotone_decreasing(line):
    numbers = []

    tokens = line.split(" ")
    for token in tokens:
        numbers.append(int(token))                    # sort bekér, splitel, átalakítja a stringeket int re
    if len(numbers) == 1:                             # ha egy elemet tartalmaz a lista akkor megfelel a feladat paramétereinek
        return True
    while True:                                       # amig az ellenőrzés alatt szigorúan csökkenő a monotonitás, próbálkozik de ha talál egy számot ami megtori,False értéket ad vissza
        try:
            for c in range(len(numbers)):
                if numbers[c] <= numbers[c+1]:
                    return False
        except IndexError:
            return True


def main():
    while True:                                      # állományvégjelig olvas (ctrl+d)
        try:
            line = input()
            print(is_strictly_monotone_decreasing(line)) # printelem True vagy False értéket
        except EOFError:                             # eof nél breakel( állományvégjelig)
            break
if __name__ == "__main__":
    main()