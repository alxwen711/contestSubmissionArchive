import sys

def rocks(a,b,c,d):
    for e in range(d):
        a[b-e][c] = "*"
    return

for i in range(int(sys.stdin.readline())):
    a,b = map(int,sys.stdin.readline().split())
    ar = list()
    ans = list()
    for j in range(a):
        ar.append(input())
        tmp = list()
        for k in range(b):
            if ar[j][k] == "o":
                tmp.append("o")
            else: tmp.append(".")
        ans.append(tmp)
    
    for m in range(b):
        r = 0
        for n in range(a):
            if ar[n][m] == "*":
                r += 1
            elif ar[n][m] == "o":
                rocks(ans,n-1,m,r)
                r = 0
        rocks(ans,a-1,m,r)
    for p in range(a):
        print(*ans[p],sep="")
    
