import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


def bsearch(ar,a,b): #how many vals in between a and b inclusive
    n = len(ar)
    low = 0
    high = n-1
    while high-low > 1:
        mid = (low+high)//2
        if ar[mid] >= a: high = mid
        else: low = mid
    lb = low
    if ar[low] < a: lb = high
    if ar[high] < a: lb = high+1

    low = 0
    high = n-1
    while high-low > 1:
        mid = (low+high)//2
        if ar[mid] <= b: low = mid
        else: high = mid
    rb = high
    if ar[high] > b: rb = low
    if ar[low] > b: rb = low-1
    #print(lb,rb,ar,a,b)
    return max(rb-lb+1,0)

for _ in range(readint()):
    n,c = readints()
    ar = readar()

    odd = list()
    even = list()
    for i in ar:
        if i % 2 == 0: even.append(i)
        else: odd.append(i)
    ans = ((c+1)*(c+2))//2
    #addition cases
    for a in ar:
        if a <= c:
            ans -= (a//2)
            ans -= 1
        else:
            mv = a-c
            r = c-mv+1
            ans -= max(0,(r+1)//2)
    #subtraction cases, check for double counting here
    for b in ar:
        if b <= c:
            ans -= (c-b+1)
            minv = b
            maxv = 2*c-b
            if minv % 2 == 1: #search on odd
                ans += bsearch(odd,minv,maxv)
            else: #search on even
                ans += bsearch(even,minv,maxv)
    print(ans)
