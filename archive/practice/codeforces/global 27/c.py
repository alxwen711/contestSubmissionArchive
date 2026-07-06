import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())


"""
and or and or and or...
for the permutation

maximum is 2**x-1, 2**x is highest bit in the permutation
if odd, strategy is to reach n with last and
if even, get everything except highest bit filled then max throw

7
6 1 5 2 3 4 7

15
(?????????) 1 5 2 3 4 7 8 15

11
6 9 10 1 5 2 3 4 7 8 11

6 (total of 7)
6 1 5 2 3 4

"""

def solve(n):
    if n % 2 == 1:
        print(n)
        if n == 5:
            print("2 1 3 4 5")
            return
        h = [1]*n
        h[-1] = 0
        ans = [n]
        c = 1
        while 2*c < n:
            c *= 2
        while c != 2:
            ans.append(c)
            ans.append(c-1)
            h[c-1] = 0
            h[c-2] = 0
            c //= 2
        ans.append(2)
        ans.append(5)
        ans.append(1)
        h[1] = 0
        h[4] = 0
        h[0] = 0
        for i in range(n):
            if h[i] == 1:
                ans.append(i+1)
        ans.reverse()
        print(*ans)
    else:
        h = [1]*n
        c = 1
        while 2*c <= n:
            c *= 2
        print(2*c-1)
        ans = list()
        while c != 2:
            ans.append(c)
            ans.append(c-1)
            h[c-1] = 0
            h[c-2] = 0
            c //= 2
        ans.append(2)
        ans.append(5)
        ans.append(1)
        h[1] = 0
        h[4] = 0
        h[0] = 0
        for i in range(n):
            if h[i] == 1:
                ans.append(i+1)
        ans.reverse()
        print(*ans)

for _ in range(readint()):
    n = readint()
    solve(n)
