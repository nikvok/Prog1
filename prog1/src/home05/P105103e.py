def delete_uppers(s):
    s = ''.join(ss for ss in s if not ss.isupper())
    return s
def main():
    while True:
        try:
            szoveg = input()
            print(delete_uppers(szoveg))
        except EOFError:
            break
if __name__ == "__main__":
    main()