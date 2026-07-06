def f(a,b):
    low = 0
    high = a//2
    while high - low > 1:
        mid = (low+high)//2
        if mid*(a-mid) > b: high = mid
        else: low = mid
    pa = low
    if pa*(a-pa) <= b: pa = high
    low = a//2
    high = a
    while high - low > 1:
        mid = (low+high)//2
        if mid*(a-mid) > b: low = mid
        else: high = mid
    pb = high
    if pb*(a-pb) <= b: pb = low
    return pb-pa+1

    

        
time = [59688274]
dist = [543102016641022]

ans = 1
for i in range(1):
    ans *= f(time[i],dist[i])
print(ans)
