import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
how to deal with tied values?
3 values in array
0 -> not pickable
1 -> pickable
2 -> picked

changing 0 -> 1 uses a clone
"""

def solve(n,ar):
    br = list()
    for i in range(n):
        br.append((ar[i],i))
    br.sort()
    br.reverse()
    ans = 0
    h = [0]*n
    prev = br[0][0]
    hv = {}
    for j in range(n):
        if prev == br[j][0]:
            hv[br[j][1]] = 1
        else: # solve all in hv
            # first try activating any 1's
            q = list()
            for i in hv.keys():
                if h[i] == 1:
                    h[i] = 2
                    q.append(i)
            while len(q) != 0:
                x = q.pop()
                if x != 0:
                    if h[x-1] == 0: h[x-1] = 1
                    if h[x-1] != 2 and hv.get(x-1) == 1:
                        q.append(x-1)
                        h[x-1] = 2
                if x != n-1:
                    if h[x+1] == 0: h[x+1] = 1
                    if h[x+1] != 2 and hv.get(x+1) == 1:
                        q.append(x+1)
                        h[x+1] = 2
            # then for any remaining 0's, activate 1 at a time
            for i in hv.keys():
                if h[i] == 0:
                    ans += 1
                    h[i] = 2
                    q.append(i)
                    while len(q) != 0:
                        x = q.pop()
                        if x != 0:
                            if h[x-1] == 0: h[x-1] = 1
                            if h[x-1] != 2 and hv.get(x-1) == 1:
                                q.append(x-1)
                                h[x-1] = 2
                        if x != n-1:
                            if h[x+1] == 0: h[x+1] = 1
                            if h[x+1] != 2 and hv.get(x+1) == 1:
                                q.append(x+1)
                                h[x+1] = 2
            # reset hv
            hv = {}
            prev = br[j][0]
            hv[br[j][1]] = 1
    # run one more time for the last hv
    # first try activating any 1's
    q = list()
    for i in hv.keys():
        if h[i] == 1:
            h[i] = 2
            q.append(i)
    while len(q) != 0:
        x = q.pop()
        if x != 0:
            if h[x-1] == 0: h[x-1] = 1
            if h[x-1] != 2 and hv.get(x-1) == 1:
                q.append(x-1)
                h[x-1] = 2
        if x != n-1:
            if h[x+1] == 0: h[x+1] = 1
            if h[x+1] != 2 and hv.get(x+1) == 1:
                q.append(x+1)
                h[x+1] = 2
    # then for any remaining 0's, activate 1 at a time
    for i in hv.keys():
        if h[i] == 0:
            ans += 1
            h[i] = 2
            q.append(i)
            while len(q) != 0:
                x = q.pop()
                if x != 0:
                    if h[x-1] == 0: h[x-1] = 1
                    if h[x-1] != 2 and hv.get(x-1) == 1:
                        q.append(x-1)
                        h[x-1] = 2
                if x != n-1:
                    if h[x+1] == 0: h[x+1] = 1
                    if h[x+1] != 2 and hv.get(x+1) == 1:
                        q.append(x+1)
                        h[x+1] = 2
    return ans

    
for _ in range(readint()):
    n = readint()
    ar = readar()
    print(solve(n,ar))
