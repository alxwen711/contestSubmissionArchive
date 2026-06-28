import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
attempt greedy by trying to add on the best remaining move each time?
pseudo idea is to check if next highest increases or not??????
"""

def create_seg(ar):
    tmp = [-i for i in ar]
    seg = [tmp]
    while len(seg[-1]) != 1:
        tmp = list()
        for j in range(len(seg[-1])//2):
            tmp.append(seg[-1][2*j]+seg[-1][2*j+1])
        seg.append(tmp)
    return seg

def query(ar,li,ri):
    l,r = li,ri
    ans = 0
    for i in range(len(ar)):
        if l > r: return ans
        if l % 2 == 1:
            ans += ar[i][l]
            l += 1
        if r % 2 == 0:
            ans += ar[i][r]
            r -= 1
        l //= 2
        r //= 2
    return ans

for _ in range(readint()):
    n,d = readints()
    ar = readar()
    ar_seg = create_seg(ar)
    ans = 0
    for k in range(n):
        #hg = 0
        pen = 0
        # compute all to right
        if k+d >= n:
            #hg += query(h_seg,k+1,n-1) + query(h_seg,0,k+d-n)
            pen += query(ar_seg,k+1,n-1) + query(ar_seg,0,k+d-n)
        else:
            #hg += query(h_seg,k+1,k+d)
            pen += query(ar_seg,k+1,k+d)
        # compute all to left
        if k-d < 0:
            #hg += query(h_seg,0,k-1) + query(h_seg,n-d+k,n-1)
            pen += query(ar_seg,0,k-1) + query(ar_seg,n-d+k,n-1)
        else:
            #hg += query(h_seg,k-d,k-1)
            pen += query(ar_seg,k-d,k-1)
        #inc = (2*d-hg)*ar[k]-pen
        if 2*d*ar[k]+pen > 0:
            ans += 2*d*ar[k]+pen
    print(ans)
