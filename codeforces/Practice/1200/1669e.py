import sys

def s(ar,p,q):
    if ar[p][q] == 0: return 0
    mul = ar[p][q]
    row = sum(ar[p])-mul
    col = 0
    for t in range(11):
        if t != p: col += ar[t][q]
    return mul*(row+col)


for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list()
    for j in range(11):
        tmp = [0]*11
        ar.append(tmp)
    for k in range(n):
        x = input()
        ar[ord(x[0])-97][ord(x[1])-97] += 1
    ans = 0
    for p in range(11):
        for q in range(11):
            ans += s(ar,p,q)
    print(ans//2)
