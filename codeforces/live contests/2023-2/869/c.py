import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
does not have to be consecutive elements
track all problem segments (length 3+)
"""

def create_sparse(ar: list) -> list:
    s = list()
    s.append(ar)
    prevrow = 0
    dist = 2 #length of subarray representation
    while dist <= len(ar):
        x = len(ar)-dist+1
        tmp = [0]*x
        for i in range(x):
            #find [i:i+dist]
            tmp[i] = s[prevrow][i]+s[prevrow][i+dist//2]
        s.append(tmp)
        prevrow += 1
        dist = dist << 1
    return s


def exact_query(l: int, h: int, ar: list):
    #default setting is to find minimum of subarray
    length = h-l+1
    s = str(bin(length))[2:]
    two = len(s)
    pt = l
    ans = 0 
    for i in range(two):
        if s[i] == "1":
            ans += ar[two-i-1][pt]
            pt += 2**(two-i-1)
    return ans

n,q = readints()
ar = readar()

st = list()
ed = list()
dud = list()
chain = 1
index = 0
for j in range(n-1):
    if ar[j] >= ar[j+1]: chain += 1
    else:
        if chain >= 3:
            st.append(index)
            ed.append(j)
            dud.append(chain-2)
        chain = 1
        index = j+1
if chain >= 3:
    st.append(index)
    ed.append(n-1)
    dud.append(chain-2)
    

#print(st)
#print(ed)
#print(dud)
h = [0]*n
for sn in range(len(st)):
    for k in range(st[sn]+1,ed[sn]):
        h[k] = 1
ds = create_sparse(h)
for i in range(q):
    a,b = readints()
    a -= 1
    b -= 1
    if b-a < 2: print(b-a+1)
    else: print(b-a+1-exact_query(a+1,b-1,ds))
"""
ds = create_sparse(dud)
m = len(st)
for i in range(q):
    a,b = readints()
    a -= 1
    b -= 1
    if b-a < 2 or m == 0: print(b-a+1)
    else:
        # find longest for [a:b]
        low = 0
        high = m-1
        while high-low > 1:
            mid = (low+high)//2
            if st[mid] >= a: high = mid
            else: low = mid
        aa = high
        if st[high] < a: aa = high+1
        if st[low] >= a: aa = low

        low = 0
        high = m-1
        while high-low > 1:
            mid = (low+high)//2
            if ed[mid] <= b: low = mid
            else: high = mid
        bb = low
        if ed[low] > b: bb = low-1
        if ed[high] <= b: bb = high
        #print(aa,bb)
        ans = b-a+1
        if aa <= bb:
            ans -= exact_query(aa,bb,ds)
            #check aa-1
            if aa != 0:
                ans -= max(ed[aa-1]-max(st[aa-1],a)-1,0)
            #check bb+1
            if bb != m-1:
                ans -= max(min(b,ed[bb+1])-st[bb+1]-1,0)
        print(ans)
        

"""
