import sys

def solve(ar,n,s,a):
    if s == a: return 1
    #print(ar[s:])
    h = ar[s]
    if h == n: return 1
    x = a-s #2
    new = True
    checked = 1
    stop = -1
    while new:       
        for j in range(x):
            if ar[a-j-1] < h:
                stop = a-j-1
                checked = stop-s+1
                break
        new = False
        if stop-s < 0: break
        for k in range(stop-s+1):
            if ar[k+s] > h:
                h = ar[k+s]
                new = True
    if h == n: return 1
    
    return solve(ar,n,s+checked,a)+1
    

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split()))
    """
    find first 0, colour with all lower values
    search back of list for first lower value
    when found, colour all in sequence
    if new found, repeat above
    if no new found, remove front of list and start again
    """
    print(solve(ar, n, 0, n))
    
    
