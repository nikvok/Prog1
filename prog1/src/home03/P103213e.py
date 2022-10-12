import math

def pythagorean_rounded(line):
    tokens = line.split(" ")
    a = float(tokens[0])
    b = float(tokens[1])
    d = int(tokens[2])
    c = a*a+b*b
    cc = round(math.sqrt(c), d)

    print(cc)
def main()
    while True:
        try:
            sor = input()
            pythagorean_rounded(sor)
        except EOFError:
            break
if __name__ == "__main__":
    main()
