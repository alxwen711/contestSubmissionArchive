import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def create_sparse(ar: list, f) -> list:
    s = list()
    s.append(ar)
    prevrow = 0
    dist = 2 #length of subarray representation
    while dist <= len(ar):
        x = len(ar)-dist+1
        tmp = [0]*x
        for i in range(x):
            #find [i:i+dist]
            tmp[i] = (f(s[prevrow][i],s[prevrow][i+dist//2]))
        s.append(tmp)
        prevrow += 1
        dist = dist << 1
    return s


def query(l: int, h: int, ar: list, f):
    length = h-l+1
    #find largest x where 2**x <= length
    two = 1
    ex = 0
    while True:
        ex += 1
        two = two << 1
        if two > length:
            two = two >> 1
            ex -= 1
            break
    if length == two: return ar[ex][l]
    else: return f(ar[ex][l],ar[ex][h-two+1])

# k is given
n,k = readints()
ar = readar() # permutation
h = [0]*(n+1)
for i in range(n):
    h[ar[i]] = i
mi = create_sparse(h,min)
ma = create_sparse(h,max)
ans = 987653896598763
for t in range(n-k+1):
    ans = min(ans,query(t+1,t+k,ma,max)-query(t+1,t+k,mi,min))
print(ans)
