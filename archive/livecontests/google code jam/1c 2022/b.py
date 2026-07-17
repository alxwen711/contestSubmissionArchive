import sys

def h(x,s,a):
    # pos means sumsquare is higher
    # neg means squaresum is higher
    # 0 means ans is found
    return (x+a)**2 - (s+(a*a))

def solve():
    n,k = map(int,sys.stdin.readline().split())
    ar = list(map(int,sys.stdin.readline().split()))
    #cover k = 1 case first for possible tb
    x = sum(ar)
    s = 0
    ans = -987654321123456789987654321
    for j in range(len(ar)):
        s += (ar[j]*ar[j])
    xx = x*x
    if xx == s:
        return 0
    if x == 0: return ans
    if xx > s and x > 0:
        high = 0
        low = -x
        while high - low > 1:
            mid = (high+low)//2
            test = h(x,s,mid)
            if test == 0: return mid
            elif test > 0: high = mid
            else: low = mid
        if h(x,s,high) == 0: return high
        elif h(x,s,low) == 0: return low
        high = -x
        low = -(10**18)
        while high - low > 1:
            mid = (high+low)//2
            test = h(x,s,mid)
            if test == 0: return mid
            elif test > 0: low = mid
            else: high = mid
        if h(x,s,high) == 0: return high
        elif h(x,s,low) == 0: return low
        else: return ans
        
    if xx < s and x > 0:
        high = 10**18
        low = 0
        while high - low > 1:
            mid = (high+low)//2
            test = h(x,s,mid)
            if test == 0: return mid
            elif test > 0: high = mid
            else: low = mid
        if h(x,s,high) == 0: return high
        elif h(x,s,low) == 0: return low
        high = -x*2
        low = -(10**18)
        while high - low > 1:
            mid = (high+low)//2
            test = h(x,s,mid)
            if test == 0: return mid
            elif test > 0: low = mid
            else: high = mid
        if h(x,s,high) == 0: return high
        elif h(x,s,low) == 0: return low
        else: return ans
        
    if xx > s and x < 0:
        high = -x
        low = 0
        while high - low > 1:
            mid = (high+low)//2
            test = h(x,s,mid)
            if test == 0: return mid
            elif test > 0: low = mid
            else: high = mid
        if h(x,s,high) == 0: return high
        elif h(x,s,low) == 0: return low
        low = -x
        high = 10**18
        while high - low > 1:
            mid = (high+low)//2
            test = h(x,s,mid)
            if test == 0: return mid
            elif test > 0: high = mid
            else: low = mid
        if h(x,s,high) == 0: return high
        elif h(x,s,low) == 0: return low
        else: return ans
        
    if xx < s and x < 0:
        low = -(10**18)
        high = 0
        while high - low > 1:
            mid = (high+low)//2
            test = h(x,s,mid)
            if test == 0: return mid
            elif test > 0: low = mid
            else: high = mid
        if h(x,s,high) == 0: return high
        elif h(x,s,low) == 0: return low
        low = -x*2
        high = 10**18
        while high - low > 1:
            mid = (high+low)//2
            test = h(x,s,mid)
            if test == 0: return mid
            elif test > 0: high = mid
            else: low = mid
        if h(x,s,high) == 0: return high
        elif h(x,s,low) == 0: return low
        else: return ans
        
    
        
                
for i in range(int(sys.stdin.readline())):
    ans = solve()
    if ans == -987654321123456789987654321:
        print("Case #"+str(i+1)+": IMPOSSIBLE")
    else: print("Case #"+str(i+1)+": "+str(ans))
    
