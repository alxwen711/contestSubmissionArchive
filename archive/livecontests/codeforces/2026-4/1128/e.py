import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
remove any case of (), move components to the ends
we can assume n/2-1 -> automatic maximum score
also baseline is however many are at the start + k, up to n/2
     VV
()(((()((())))))
(()(((((()))))))

only ( chains count so not a fully invertible problem

alternately, there is finding longest chain of ( interrupted by up
to k ), ans is number of ( - k

alternate is to just use the start?

highest +/- score with at most k ), use sparse table to work this out

number of () - 1 moves is needed to ensure maximum?

(())(()) disproves this
"""

def create_sparse(ar):
    seg = list()
    seg.append(ar)
    while len(seg[-1]) != 1:
        tmp = list()
        for i in range(len(seg[-1])//2):
            tmp.append(min(seg[-1][2*i],seg[-1][2*i+1]))
        seg.append(tmp)
    return seg

def query(seg,li,ri):
    l,r = li,ri
    ans = 4897389476892347
    for i in range(len(seg)):
        if l > r: return ans
        if l % 2 == 1:
            ans = min(ans,seg[i][l])
            l += 1
        if r % 2 == 0:
            ans = min(ans,seg[i][r])
            r -= 1
        l //= 2
        r //= 2
    return ans
        

for _ in range(readint()):
    n,k = readints() # k is at most n/2
    s = readin()
    ans = 0
    v = k
    a,b = 0,0
    flag = True
    for i in s:
        if i == "(":
            if flag: ans += 1
            else:
                a += 1
                if min(a,b) > k: break
                ans += 1
        else:
            flag = False
            b += 1
            
            
    if ans == n//2: # auto complete
        print(ans)
        continue
    # alternate plan, longest ( chain with at most k )
    ar = [0]
    for i in s:
        if i == "(": ar.append(ar[-1]+1)
        else: ar.append(ar[-1]-1)

    sparse = create_sparse(ar)

    ptr = 0
    rc = 0
    for j in range(n):
        if s[j] == ")": rc += 1
        while rc > k:
            if s[ptr] == ")": rc -= 1
            ptr += 1
        ans = max(ans,ar[j+1]-query(sparse,ptr,j+1))
    print(ans)





    
