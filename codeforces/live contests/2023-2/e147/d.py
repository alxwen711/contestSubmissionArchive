import sys
from heapq import *

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
total cost: distance travelled + 2*segments needed
01010101011111
start by using all segments, then remove shortest until not long enough
if all not enough then -1


greedy push until the end, count number of 1 segments that can be saved and subtract them?
maybe greedy was not the answer
"""

def solve(n,k,a,b):
    oneseg = 0
    twoseg = 0
    t = 0
    for i in range(n):
        aa,bb = a[i],b[i]
        dist = bb-aa+1
        if dist == 1: oneseg += 1
        elif dist == 2: twoseg += 1
        t += dist
        if t >= k: #find endpoint
            over = t-k
            ep = bb-over
            index = i
            ans = (index+1)*2+ep
            tans = ans
            while oneseg != 0 or twoseg != 0:
                tans -= 2
                if oneseg != 0:
                    oneseg -= 1
                    if ep == b[index]:
                        index += 1
                        if index == n: return ans
                        ep = a[index]
                        if a[index] == b[index]: oneseg += 1
                        elif a[index]+1 == b[index]: twoseg += 1
                        tans += (ep-b[index-1]+2)
                    else:
                        ep += 1
                        tans += 1
                else:
                    twoseg -= 1
                    if ep+2 <= b[index]:
                        ep += 2
                        tans += 2
                    else:
                        tans += 2
                        x = 2-(b[index]-ep)
                        while x != 0:
                            index += 1
                            tans += 2
                            if index == n: return ans
                            ep = a[index]
                            if a[index] == b[index]: oneseg += 1
                            elif a[index]+1 == b[index]: twoseg += 1
                            dist = b[index]-a[index]+1
                            if dist < x: x -= dist
                            else:
                                ep += (x-1)
                                break
                        
                ans = min(ans,tans)
            return ans
    return -1
    """
    l = 0
    h = [1]*n
    ar = list()
    for i in range(n):
        aa,bb = a[i],b[i]
        ar.append([bb-aa+1,-aa,bb,i])
        l += (bb-aa+1)
    if k > l: return -1
    pos = 0
    index = -1
    s = k
    while s > 0:
        index += 1
        aa,bb = a[index],b[index]
        pos = aa-1
        if (bb-aa+1) >= s:
            pos += s
            s = 0
            break
        s -= (bb-aa+1)
    seg = index+1
    ans = pos+2*seg
    for ri in range(n):
        l -= ar[ri][0]
        if k > l: return ans
        h[ar[ri][3]] = 0
        if ar[ri][3] <= index: # move pos
            if ar[ri][3] < index:
                seg -= 1
                s += ar[ri][0]
            #reset to start of last index
            seg -= 1
            s += (pos-a[index]+1)
            index -= 1
            while s > 0:
                index += 1
                seg += 1
                aa,bb = a[index],b[index]
                pos = aa-1
                if (bb-aa+1) >= s:
                    pos += s
                    s = 0
                    break
                s -= (bb-aa+1)
        ans = min(ans,pos+2*seg)
    return ans
    """     

for i in range(readint()):
    n,k = readints()
    ar = readar()
    br = readar()
    print(solve(n,k,ar,br))
    """
    h = list()
    best = 728768947589270892758724957938998
    s = 0
    seg = 0
    for j in range(n):
        lp,rp = ar[j],br[j]
        dist = rp-lp+1
        s += dist
        if s >= k:
            while len(h) > 0:
                if (s-h[0]) >= k:
                    seg -= 1
                    s -= h[0]
                    heappop(h)
                else: break
            heappush(h,dist)
            seg += 1
            req = k-(s-dist)
            ep = max(lp,lp+req-1)
            best = min(best,ep+2*seg)
        else:
            heappush(h,dist)
            seg += 1
        
    if best == 728768947589270892758724957938998: print(-1)
    else: print(best)
    """
