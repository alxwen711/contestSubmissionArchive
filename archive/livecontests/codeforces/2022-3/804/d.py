import sys
#O(n^2) is allowed, dp?? maybe brute force greed method
def solve(n,ar):
    h = [0]*(n+1) #need to reach n zeroes
    for j in range(n):
        h[ar[j]] += 1
    x = n
    while h.count(0) < n:
        yank = 0
        c = 99999999999999
        for k in range(x-1):
            if ar[k] != ar[k+1]: #norm candidate
                p = max(h[ar[k]],h[ar[k+1]])
                if p < c:
                    yank = k
                    c = p
        a = ar.pop(yank)
        b = ar.pop(yank)
        h[a] -= 1
        h[b] -= 1
        x -= 2
        print(ar)

    return max(h)

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    print(solve(n,ar))
