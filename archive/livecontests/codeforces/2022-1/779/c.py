"""
x = [
     [1,4,3,2],
     [2,1,4,3],
     [3,2,1,4],
     [4,3,2,1],]

4,1,2,3
3,2,1,2
3,1,2,2
3,3,1,2
2,2,3,1
2,2,2,1



3,1,2
2,2,1
find single 1, then compare to ascending line row or something
"""

import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    if ar.count(1) != 1 or ar.count(n) > 1: print("NO")
    elif ar.count(n) == 1:
        x = ar.index(1)
        ans = "YES"
        for j in range(n):
            if ar[(x+j)%n] != (j+1):
                ans = "NO"
                break
        print(ans)

    else:
        x = ar.index(1)
        ans = "YES"
        for j in range(n):
            if ar[(x+j)%n] > (j+1):
                ans = "NO"
                break
        
        
        #maximum test
        c = max(ar)
        r = n-c
        if ar.count(c) > 1:
            x = list()
            for z in range(n):
                if ar[z] == c:
                    x.append(z)
            x.append(x[0])
            h = 0
            for q in range(len(x)):
                if abs(x[q] - x[q+1]) > r: h += 1
                if h == 2:
                    ans = "NO"
                    break
        a = max(ar)
        b = 0
        if ar.count(a-1) == 0 and n != 1: ans = "NO"
        
        print(ans)
