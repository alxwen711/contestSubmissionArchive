import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
the sequence length is only up to 20

the starting value is at most 1000000000
"""

sv = [100]*30
sv[3] = 1000000000
sv[4] = 1000000
sv[5] = 100000
sv[6] = 10000
sv[7] = 1000
sv[8] = 400
sv[9] = 200

n = readint()

ans = 0
for i in range(3,21):
    base = 1
    lm = sv[i]-1
    while True:
        low = 0
        high = lm
        while high-low > 1:
            mid = (low+high)//2
            v = 1
            m = base
            flag = False
            for _ in range(i):
                v *= m
                if v > n:
                    flag = True
                    break
                m += mid
            if flag: high = mid
            else: low = mid
        if low == 0:
            v = 1
            m = base
            flag = False
            for _ in range(i):
                v *= m
                if v > n:
                    flag = True
                    break
                m += high
            if flag: break
            else: low = high
        ans += low
        base += 1
        lm -= 1
print(ans)
            
        


            
