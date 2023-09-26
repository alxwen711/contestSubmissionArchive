import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
count how many to delete at the end for factorial
after each group, mult by its size for choices of what to pick
"""
m = 998244353


def fact(ansa,m):
    x = 1
    for i in range(1,ansa+1):
        x = (x*i) % m
    return x

for i in range(readint()):
    s = sys.stdin.readline()
    chain = 1
    prev = s[0]
    ansa = 0
    ansb = 1
    for j in range(1,len(s)-1):
        if s[j] == prev:
            chain += 1
        else:
            ansa += (chain-1)
            ansb = (ansb*chain) % m
            chain = 1
            prev = s[j]
    ansa += (chain-1)
    ansb = (ansb*chain) % m
    ansb = (ansb*fact(ansa,m)) % m
    print(ansa,ansb)
