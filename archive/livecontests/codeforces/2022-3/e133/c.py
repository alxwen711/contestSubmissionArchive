import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


def solve():
    n = readint()
    ar = list()
    for j in range(2):
        ar.append(readar())
    h = [0]*(n+1)
    h[1] = ar[1][0]+1
    #calc snake path time
    time = h[1]
    for k in range(n-1):
        #calc col k+1 and place in h[k+2]
        if k % 2 == 0: #bot->top
            time = max(time,ar[1][k+1])+1
            time = max(time,ar[0][k+1])+1
        else: #top->bot
            time = max(time,ar[0][k+1])+1
            time = max(time,ar[1][k+1])+1
        h[k+2] = time
    
    #calc forward loop time
    forward = [0]*(n+1)
    time = 0
    for l in range(n):
        time = max(ar[1][-l-1],forward[l])+1
        time = max(time,2*l+2+ar[0][-l-1])
        forward[l+1] = time
    #calc backward loop time
    backward = [0]*(n+1)
    time = 0
    for m in range(n):
        time = max(ar[0][-m-1],backward[m])+1
        time = max(time,2*m+2+ar[1][-m-1])
        backward[m+1] = time
    forward[n] -= 1
    #time = max(snake+remaining tiles,loop remnant)        
    ans = 999999999999999999999
    for p in range(1,n):
        if p % 2 == 0: #forward
            ans = min(ans,max(h[p]+min(2*(n-p),2*n-1),forward[n-p]))
        else: #backward
            ans = min(ans,max(h[p]+2*(n-p),backward[n-p]))
    #print(h,forward,backward)
    #find full forward
    ans = min(ans,max(forward[n-1],ar[1][0])+1)
    return ans

for i in range(readint()):
    print(solve())
