def double_odd_digits(s):
    uj = ""
    for k in s:
        if k.isnumeric() == True and int(k) % 2 != 0:
            uj += k
        uj += k
    print(uj)
def main():
    n = int(input())
    for k in range(n):
        string = input()
        double_odd_digits(string)
if __name__ == "__main__":
    main()