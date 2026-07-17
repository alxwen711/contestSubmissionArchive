import sys

def bs(ar,x,l):
    if not ar: return -1
    high = l-1
    low = 0
    while high-low > 1:
        mid = (high+low)//2
        if ar[mid][0] == x: return mid
        elif ar[mid][0] > x: high = mid
        else: low = mid
    if ar[low][0] == x: return low
    elif ar[high][0] == x: return high
    else: return -1


for i in range(int(sys.stdin.readline())):
    n,x = map(int, sys.stdin.readline().split())
    ar = list(map(int, sys.stdin.readline().split()))
    ar.sort()
    arr = list()
    count = 0
    v = 8948935983
    for j in range(n):
        if ar[j] != v:
            if count != 0:
                tmp = list()
                tmp.append(v)
                tmp.append(count)
                arr.append(tmp)
            count = 1
            v = ar[j]
        else: count += 1
    last = list()
    last.append(v)
    last.append(count)
    arr.append(last)
    la = len(arr)
    a = 0
    l = n
    ans = 0
    #print(arr)
    while l != 0:
        if l == 1:
            l = 0
            ans += 1
            break
        if arr[a][1] == 0:
            a += 1
        else:
            val = arr[a][0]
            index = bs(arr,val*x,la)
            if index == -1:
                ans += 1
                l += -1
                arr[a][1] += -1
            elif arr[index][1] == 0:
                ans += 1
                l += -1
                arr[a][1] += -1
            else:
                l += -2
                arr[index][1] += -1
                arr[a][1] += -1
    print(ans)
