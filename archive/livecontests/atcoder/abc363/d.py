import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
num of palindromes by digit count:
[0,10,9,90,90,900,900,9000,9000]


46 -> 27
"""

n = readint()
digitcount = [0,10,9]
v = 9
for _ in range(20):
    v *= 10
    digitcount.append(v)
    digitcount.append(v)

for i in range(len(digitcount)):
    if n > digitcount[i]:
        n -= digitcount[i]
    else: # stop on i digits
        if i == 1: print(n-1)
        elif i == 2: print(n*11)
        else:
            base = (i-1)//2
            n += 10**base
            n -= 1
            s = str(n)
            if i % 2 == 0:
                print(s+s[::-1])
            else:
                print(s[:-1]+s[::-1])
        break
