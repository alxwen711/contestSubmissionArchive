import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
n is odd, only up to 99
squares n digits long, must use same digit set


169 + a lot of 0's should work
"""

"""
def f(x):
    y = str(x)
    return (y.count("0"),y.count("1"),y.count("2"),y.count("3"),y.count("4"),y.count("5"),y.count("6"),y.count("7"),y.count("8"),y.count("9"))

def bruteforce(n):
    x = 10**(n//2)
    d = {}
    while (x*x) < 10**n:
        target = f(x*x)
        if d.get(target) == None: d[target] = list()
        d[target].append(x)
        x += 1
    for i in d.keys():
        if len(d[i]) >= n: print(i,d[i])
"""
def integerize(x):
    ans = 0
    for i in range(len(x)):
        ans *= 10
        ans += x[i]
    return ans

for _ in range(readint()):
    n = readint()
    if n == 1: print(1)
    else:
        ar = [0]*((n+1)//2)
        ar[0] = 1
        for a in range(n//2):
            ar[-a-1] = 3
            x = integerize(ar)
            print(x*x)
            ar[-a-1] = 0
        ar[0] = 3
        for b in range(n//2):
            ar[-b-1] = 1
            x = integerize(ar)
            print(x*x)
            ar[-b-1] = 0
        s = "14"+("0"*(n//2-1))
        s = int(s)
        print(s*s)
