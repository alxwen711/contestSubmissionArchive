import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def freq_ar(ar: list[int], limit: int) -> list[int]:
    if ar == None: return []
    h = [0]*(limit+1) #change to limit+1 for h[1] = freq of 1
    for i in range(len(ar)):
        h[ar[i]] += 1 #change to h[ar[i]] for h[1] = freq of 1
    return h

for i in range(readint()):
    n,c = readints()
    ar = readar()
    h = freq_ar(ar,100)
    ans = 0
    for j in range(101):
        ans += min(c,h[j])
    print(ans)
