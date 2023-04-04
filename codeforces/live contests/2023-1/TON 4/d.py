import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
# 5 3 10
def one(a,b,c):
    if c == 1: return 1,a
    x = a-b
    return x*(c-2)+a+1,x*(c-1)+a

def two(a,b,low,high):
    x = a-b
    return max((low-a+x-1)//x+1,1),max((high-a+x-1)//x+1,1)

def solve(n):
    low = 0
    high = 999999999999999999999999999999
    ans = list()
    for i in range(n):
        ar = readar()
        if ar[0] == 1:
            l,h = one(ar[1],ar[2],ar[3])
            if l > high or h < low: ans.append(0)
            else:
                ans.append(1)
                low = max(l,low)
                high = min(h,high)
        else:
            a,b = two(ar[1],ar[2],low,high)
            #print(low,high,a,b)
            if a == b: ans.append(a)
            else: ans.append(-1)
    print(*ans)
for i in range(readint()):
    n = readint()
    solve(n)
