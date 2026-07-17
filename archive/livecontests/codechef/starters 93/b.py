import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
45 3? Can still do 3/9/27
20 4, computes to 2 moves, but
-1 -> 19, 4 moves

sorting into bases this is a nim game
base 3, 14 pts -> 1,1,2
moves are either take 1, or slide 1 and replace with b-1
1 space right
"""
"""
def f(x,k):
    ans = 0
    while x != 0:
        ans += (x%k)
        x //= k
    return ans

for i in range(readint()):
    n,k = readints()
    if n == 0: print("Tina")
    elif f(n,k) % 2 == 1: print("Shivansh")
    else:
        parity = f(n,k) % 2
        c = 1
        flag = False
        while c <= n:
            if f(n-c,k) % 2 == 0:
                flag = True
                break
            c *= k
        if flag: print("Shivansh")
        else: print("Tina")
        if parity == 1: print("Shivansh")

"""

for i in range(readint()):
    n,k = readints()
    if 2 == k:
        if n % 3 == 0: print("Tina")
        else: print("Shivansh")
    elif k % 2 == 1:
        if n % 2 == 0: print("Tina")
        else: print("Shivansh")
    else:
        r = n % (k+1)
        if r % 2 == 0: print("Tina")
        else: print("Shivansh")

"""
well that was a shitshow
pausing recording first, will go over unrated problems later
"""
        
