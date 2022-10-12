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