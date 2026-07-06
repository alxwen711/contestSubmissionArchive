import sys
from random import randint


#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def create_sparse(ar):
    s = list()
    s.append(ar)
    prevrow = 0
    dist = 2 #length of subarray representation
    while dist <= len(ar):
        x = len(ar)-dist+1
        tmp = [0]*x
        for i in range(x):
            #find [i:i+dist]
            tmp[i] = (max(s[prevrow][i],s[prevrow][i+dist//2]))
        s.append(tmp)
        prevrow += 1
        dist = dist << 1
    return s

def freq_dict(ar, pos):
    d = {}
    if ar == None: return d
    for i in range(len(ar)):
        x = ar[i]
        if d.get(x) == None:
            if pos: d[x] = list()
            else: d[x] = 0
        if pos: d[x].append(i)
        else: d[x] += 1
    return d

def query(l, h, ar):
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
    else: return max(ar[ex][l],ar[ex][h-two+1])

def find(m,d,l,r):
    if d.get(m) == None: return [l] #will lead to wa
    ar = d[m]
    lar = len(ar)
    if lar == 1: return ar
    al,ah = 0,lar-1
    while ah-al > 1:
        mid = (al+ah)//2
        if ar[mid] >= l: ah = mid
        else: al = mid
    ansa = al
    if ar[al] < l: ansa = ah
    bl,bh = 0,lar-1
    while bh-bl > 1:
        mid = (bl+bh)//2
        if ar[mid] <= r: bl = mid
        else: bh = mid
    ansb = bh
    if ar[bh] > r: ansb = bl
    return ar[ansa:(ansb+1)]

def solve(n,a,b,l,r,c,d):
    ans = list()
    #handle nil case here
    if l > r: return ans
    #handle single case?
    if l == r:
        if a[l] != b[r]: ans.append(b[r])
        return ans
    #find maximum height
    m = query(l,r,c)

    #det indicies where max height is a thing (bin)
    indices = find(m,d,l,r)
    #check if cut is even needed
    #when at max height, split into sub problem
    cut = False
    prev = l
    for j in range(len(indices)):
        if a[indices[j]] != b[indices[j]]: cut = True
        ans += solve(n,a,b,prev,indices[j]-1,c,d)
        prev = indices[j]+1
    ans += solve(n,a,b,prev,r,c,d)
    #add max height if needed, return
    if cut: ans.append(m)
    return ans

def verify(a,b):
    for snth in range(len(a)):
        if a[snth] < b[snth]: return False
    return True

for i in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    r = readint()
    cr = readar()
    if verify(ar,br):
        nnnn = create_sparse(br)
        why = freq_dict(br,True)
        req = solve(n,ar,br,0,n-1,nnnn,why)
        #check if req razors are in cr
        #print(req)
        #sv = randint(0,42069)
        af = freq_dict(req,False)
        bf = freq_dict(cr,False)
        ccc = list(af.keys())
        #print(af,bf)
        #print(ccc)
        ans = "YES"
        for j in range(len(ccc)):
            if bf.get(ccc[j]) == None:
                ans = "NO"
                break
            if af[ccc[j]] > bf[ccc[j]]:
                ans = "NO"
                break
        print(ans)
    else: print("NO")
