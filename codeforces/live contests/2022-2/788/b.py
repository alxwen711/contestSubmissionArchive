import sys

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    s = sys.stdin.readline()
    """
    max chain + 2+ special
    
    """
    ar = list(map(str,sys.stdin.readline().split()))
    h = [0]*26
    for j in range(int(ar[0])):
        h[ord(ar[j+1])-97] = 1
    ans = 0
    count = False
    chain = 0
    for k in range(n):
        if h[ord(s[k])-97] == 1:
            if chain >= ans:
                if chain > ans: count = False
                ans = chain
                if k > chain:
                    if h[ord(s[k-chain-1])-97] == 1: count = True
            chain = 0
        else: chain += 1
    if count: ans += 1
    print(ans)
        
