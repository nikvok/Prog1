import sys
from typing import NamedTuple
Coupon = NamedTuple("Coupon",[("store", str),("product", str),("discount", int)])
def line_to_coupon(line: str) -> Coupon:
    tokens = line.strip().split(";")
    return Coupon((tokens[0]),tokens[1],int(tokens[2]))
def distinct_stores(line: list[Coupon]) -> list[Coupon]:
    setnumbers = set()
    return setnumbers.add(Coupon.store)
def main():
    n = int(input())
    coupons = []
    for i in range(n):
        line = input()
        print(distinct_stores(line_to_coupon(line)))

if __name__ == "__main__":
    main()
