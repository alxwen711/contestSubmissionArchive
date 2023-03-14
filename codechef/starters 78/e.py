import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
#aabababbcabcc
def solve(a,b,k):
    if (max(a)-min(a)) > k:
        print(-1)
        return
    ans = list()
    aa = len(a)
    #try:
    for i in range(aa):
        if a[i] < 0:
            print(-1)
            break
        elif a[i] > k:
            att = a[i]
            for joeu in range(k):
                ans.append(b[i])
                a[i] -= 1
            for m in range(att-k):
                for n in range(i+1,aa):
                    ans.append(b[n])
                    a[n] -= 1
                ans.append(b[i])
                a[i] -= 1
        else:
            for j in range(a[i]):
                ans.append(b[i])
                a[i] -= 1
    #print(a)
    ans.reverse()
    print(*ans,sep="")
    #except:
        #print("asnthsnthsnthsnthsnth")


for i in range(readint()):
    n,k = readints()
    s = input()
    h = [0]*26
    for j in range(n):
        h[ord(s[j])-97] += 1
    ar = list()
    br = list()
    #print(h)
    for u in range(26):
        if h[u] != 0:
            ar.append(h[u])
            br.append(chr(u+97))
    #print(ar)
    #print(br)
    ar.reverse()
    br.reverse()
    solve(ar,br,k)
