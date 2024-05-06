import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

# either swap with first cow, second cow, or first cow you lose to
# if you win against everyone, go to front

def c(ar,k,fb):
    ar[k],ar[fb] = ar[fb],ar[k] # cow in pos fb
    score = 0
    if fb <= 1:
        if ar[fb] == max(ar[0],ar[1]):
            score += 1
            for snth in range(2,len(ar)):
                if ar[fb] > ar[snth]: score += 1
                else: break
    else:
        if ar[fb] > max(ar[:fb]):
            score += 1
            for snt in range(fb+1,len(ar)):
                if ar[fb] > ar[snt]: score += 1
                else: break
    ar[k],ar[fb] = ar[fb],ar[k] # revert
    return score

for _ in range(readint()):
    n,k = readints()
    k -= 1
    ar = readar()
    fb = -1
    for i in range(k):
        if ar[i] > ar[k]:
            fb = i
            break
    ans = 0
    if fb != -1: ans = max(ans,c(ar,k,fb))
    ans = max(ans,c(ar,k,0))
    ans = max(ans,c(ar,k,1))
    print(ans)
