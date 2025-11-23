import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
vzvylxxmsy
vvzvylxxms
vvvzvllxxm
vvvvvllxxx

vvvvylxxms
vvvvvllxxm
vvvvvllxxx

vzvylxxmsy
vvvvvllxxx
0101212123

this processing should be done right to left

each chain in the final string has to match to a chr
from the starting string

there could be multiple matches, optimize the match with fewest k
k is maximum distance between segments

"""

for _ in range(readint()):
    n,k = readints()
    s = readin()
    t = readin()
    ans = [0]*n
    ptr = n-1
    for i in range(n-1,-1,-1):
        if ptr > i: ptr -= 1
        while ptr != -1:
            if s[ptr] == t[i]: break
            else: ptr -= 1
        if ptr == -1: break
        ans[i] = i-ptr
    if ptr == -1: print(-1)
    else:
        c = max(ans)
        if c > k: print(-1)
        else:
            print(c)
            st = list()
            ar = list()
            for _ in range(c+1):
                br = list()
                ar.append(br)
            for j in range(n):
                st.append(s[j])
                for snth in range(1,ans[j]+1):
                    ar[snth].append(j)
            for l in range(1,c+1):
                ar[l].reverse()
                for u in ar[l]:
                    st[u] = st[u-1]
                print("".join(st))




        
