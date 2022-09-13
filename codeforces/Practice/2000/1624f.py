import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


"""
n = 16
+ 7
if 1-8 -> return 0
else -> return 1

9-16 -> 16-23 -> 28-35 (11,18,30)
CANNOT have a mod -1,0 situation, else not possible to complete
mid target has to be min breakpoint
"""
n = readint()
low = 1
high = n-1
added = 0
xl,xh = low,high
expected = 0
testval=1
while high - low > 1:
    mid = (high+low+1)//2
    #target = (expected+1)*n
    #assume current is mid+added
    target = (expected+1)*n
    x = target-mid-added #amount to add for mid breakpoint
    added += x
    #print(added+testval,low,high)
    print("+",str(x),flush=True)
    res = readint()
    if res > expected:
        low = mid
        expected += 1
    else: high = mid - 1

if low == high: print("!",str(low+added))
else: #one more query for high
    target = (expected+1)*n-1
    x = target-low-added #amount to add for under breakpoint
    added += x
    #print(added+testval,low,high)
    print("+",str(x),flush=True)
    res = readint()
    if res > expected:
        print("!",str(high+added))
    else: print("!",str(low+added))


