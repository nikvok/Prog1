def is_prime(n):                                   # függvény a prímszámokra
    if n==1:
        return False
    elif n==2:
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True
def count_of_primes():
    count = 0
    num = input()
    nums = num.split(" ")
    for c in range(len(nums)):
        nums[c] = int(nums[c])
    for s in range(len(nums)):
        if is_prime(nums[s]) is True:
            count = count + 1
    print(count)
def main():
    n = int(input())
    for i in range(n):
        count_of_primes()
if __name__ == "__main__":
    main()



