from model import finance, kripto
import sys
def main():
    assert len(sys.argv)>1, "Az értékadás kötelező"
    n = int(sys.argv[1])
    assert n>0
    list = []
    for i in range(n):
        line = input()
        tokens = line.split(";")
        if len(tokens)==3:
            fin = finance(tokens[0], tokens[1], int(tokens[2]))
            list.append(fin)
        else:
            kripta=kripto(tokens[0], tokens[1], int(tokens[2]),tokens[3])
            list.append(kripta)
    list.sort()
    for m in list:
        print(m)
if __name__=="__main__":
    main()