import sys
#binary search ranges???
for i in range(int(sys.stdin.readline())):
    n,k = map(int,sys.stdin.readline().split())
    ar = list(map(int,sys.stdin.readline().split()))
    l = False
    ans = 999999999
    for j in range(k):
        low = ar[0]//(j+1)
        high = ar[0]//(j+1)
        if low == 1: l = True
        x = (j+1)
        last = ar[0]//(j+1)
        for q in range(1,n):
            tmp = x
            prev = ar[q]//tmp
            while True:
                if low <= ar[q]//tmp and ar[q]//tmp <= high:
                    x = tmp
                    break
                elif ar[q]//tmp > high:
                    prev = ar[q]//tmp
                    if tmp < k: tmp += 1
                    else: #max limit reached, must use this
                        high = ar[q]//tmp
                        x = tmp
                        break
                else: #compare current with prev
                    cur = ar[q]//tmp #prev is ar[k]//(tmp-1)
                    if low-cur < prev-high: #use low
                        x = tmp
                        low = cur
                    else:
                        x = tmp-1
                        high = prev
                    break
        if high-low < ans:
            ans = high-low
            #print(ans,low,high)
            
        print(low,high)        

        
        if l: break
    print(ans)
        
