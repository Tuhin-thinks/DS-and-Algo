"""
#copied
"""


import sys

def larger(n):
    """
    given an integer n, find the smallest integer k such that:
    1- k > n
    2- str(k) and str(n) are anagrams.
    """
    # print(n)
    sn = str(n)[::-1] # parse the number from right to left
    # print(sn)
    lun = len(sn)
    i = 0
    while i < lun:
        this = sn[i]
        # print(f"{i=}, {this=}")
        for pos, that in enumerate(sn[i+1:], start=i+1):
            # print(f"{pos=}, {that=}")
            if this > that:
                group = that+sn[i+1:pos]
                # print(f"{group=}")
                # print(f"{sn[:i]} + {''.join(sorted(group, reverse=True))} + {this} + {sn[pos+1:]}")
                res = sn[:i] + "".join(sorted(group, reverse=True)) + this + sn[pos+1:]
                return int(res[::-1]) # build the new number in correct order
        i += 1
    # no suitable integer found
    return 0

def largest(n:str):
    res = n
    this = 0
    while this <= res:
        this = larger(res)
        if this == 0:
            return res
        this, res = res, this



if __name__ == '__main__':
    number = sys.argv[1]
    print(largest(int(number)))