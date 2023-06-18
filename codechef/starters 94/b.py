import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

m = 1000000007
def solve(n,k,s):
    ar = list()
    for i in range(n):
        x = s[i]
        if x == "a" or x == "e" or x == "i" or x == "o" or x == "u": ar.append(1)
        else: ar.append(0)
    #record min segs containing k vowels
    st = list()
    ed = list()
    c = 0
    for u in range(n):
        c += ar[u]
        if c == 1 and ar[u] == 1: #start of new seg
            st.append(u)
        if c == k: #end of new seg
            ed.append(u)
            c = 0
    ans = 1
    #print(st,ed)
    for v in range(len(st)-1):
        a = st[v+1]-ed[v]
        ans = (ans*a) % m
    return ans
        
for i in range(readint()):
    n,k = readints()
    s = input()
    print(solve(n,k,s))
