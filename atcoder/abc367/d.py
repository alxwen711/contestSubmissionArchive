import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
note: it is possible that walking the opposite direction is faster
2 pointer to track modulo, double the array
"""
"""
def f(n,m,ar,flag):
    h = [0]*m
    br = list()
    br.append(x)
    for i in ar:
        x += i
        br.append(x)
    index = 0
    t = 0
    tt = 0
    s = br[-1]
    y = 0
    ans = 0
    for i in range(n):
        while (t+ar[index])*2 < s:
            tt += ar[index]
            t += ar[index]
            h[tt % m] += 1
            index = (index+1) % n
        if flag and (t+ar[index])*2 == s and (s//2) % m == 0: ans += 1
        print(h)
        ans += h[y % m]
        y += ar[i]
        t -= ar[i]
        if i != index:
            h[y % m] -= 1
        else:
            tt += ar[index]
            t += ar[index]
            index = (index+1) % n
    return ans
"""

def f(n,m,ar,flag):
    h = [0]*m
    br = list()
    for i in ar:
        br.append(i)
    s = sum(br)
    for i in ar:
        br.append(i)
    for i in ar:
        br.append(i)
    li,ri = 0,0
    lsum,rsum = 0,0
    ans = 0
    while li != n:
        tmp = rsum+br[ri]
        if (tmp-lsum) < s: # shift ri
            rsum = tmp
            h[rsum % m] += 1
            ri += 1
        else: # compute li, shift
            ans += h[lsum % m]
            lsum += br[li]
            li += 1
            h[lsum % m] -= 1
    return ans

n,m = readints()
ar = readar()

x = f(n,m,ar,True)
#x += f(n,m,ar,False)
print(x)
"""
    h[x % m] += 1

ans = 0
y = 0
for j in ar:
    #print(h)
    ans += h[y % m]
    y += j
    x += j
    h[y % m] -= 1
    h[x % m] += 1
print(ans)
"""
