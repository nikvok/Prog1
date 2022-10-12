def is_prime():
    a = 2
    num = int(input())
    while num > a:
        if num % a == 0 & a != num:
            print("NEM")
            break
        a += 1
    else:
        if num != 0 and num != 1:
            print("IGEN")
        else:
            print("NEM")
def main():
    n = int(input())
    for i in range(n):
        is_prime()
if __name__ == "__main__":
    main()

