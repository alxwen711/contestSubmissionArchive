import sys

def solve(t,ar):
    #pairs = [0]*(t-2)
    p, rP, rD, ones = 0, 0, 0, 0
    #dependencies = [0]*(t-2)
    for j in range(t-2):
        #pairs[j] += (ar[j+1]//2)
        #dependencies[j] += (ar[j+1]%2)
        p += (ar[j+1]//2)
        rP += (ar[j+1]//2)
        rD += (ar[j+1]%2)
        if ar[j+1] == 1: ones += 1
    lP = 0
    lD = 0
    ans = 500000000
    for j in range(t-2):
        x = ar[j+1]
        pp = x//2
        pd = x%2
        if (rP)*2 >= lD and (lP)*2 >= rD:
            dependencies = max(lD,rD)
            if ones == t-3: ans = min(ans, p+dependencies+2)
            else: ans = min(ans, p+dependencies)

        lP += x//2
        lD += x%2
        rP += -(x//2)
        rD += -(x%2)

    return ans
    
    """dependencies = 0
    ones = 0
    pairs = 0
    ser = False
    for j in range(t-2):
        if ar[j+1] % 2 == 1: dependencies += 1
        if ar[j+1] == 1: ones += 1
        pairs += (ar[j+1]//2)
        if pairs*2 >= dependencies: ser = True
    if pairs*4 < dependencies or ser == False: return -1 #dependency and left test

    ser = False
    #right test
    rd = 0
    rp = 0
    for j in range(t-2):
        if ar[t-j-1] % 2 == 1: rd += 1
        rp += (ar[t-j-1]//2)
        if rp*2 >= rd: ser = True
    if ser == False: return -1

    #possible?
    if ones+1 == t:
        

    
    min(pairs*2,dependencies)
    """


for i in range(int(sys.stdin.readline())):
    t = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split()))
    if t == 3:
        if ar[1] % 2 == 1: print(-1)
        else: print(ar[1]//2)
    else:
        y = solve(t,ar)
        if y == 500000000: print(-1)
        else: print(y)
            

        """
        pairs = 0
        sing = 0
        for j in range(t-2):
            x = ar[j+1]
            pairs += (x//2)
            sing = (x % 2)
        if pairs*4 < sing: print(-1)
        else:
            if pairs >= 2*sing:
                a = sing // 2
"""
