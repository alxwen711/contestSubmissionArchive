#practice ver, live is inaccurate

import sys
    
for i in range(int(sys.stdin.readline())):
    t = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split()))
    pairs = 0
    if t == 3:
        if ar[1] % 2 == 1: print(-1)
        else: print(ar[1]//2)
    else:
        ones, odd = 0, 0
        for j in range(t-2):
            if ar[j+1] == 1: ones += 1
            if ar[j+1] % 2 == 1: odd += 1
            pairs += (ar[j+1]//2)
        if ones == t-2: print(-1)
        else: print(pairs+odd)

      
