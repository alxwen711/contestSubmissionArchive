import sys
for i in range(int(sys.stdin.readline())):
    x,y,z = map(int,sys.stdin.readline().split())
    a = input()
    b = input()
    aa = [0]*26
    bb = [0]*26
    for j in range(len(a)):
        aa[ord(a[j])-97] += 1
    for k in range(len(b)):
        bb[ord(b[k])-97] += 1
    a = ""
    b = ""
    for m in range(26):
        a += chr(m+97)*aa[m]
    for n in range(26):
        b += chr(n+97)*bb[n]
    #print(a,b)
    achain = 0
    bchain = 0
    ma = len(a)
    mb = len(b)
    sa = 0
    sb = 0
    ans = ""
    while True:
        if sa == ma or sb == mb: break
        if achain == z:
            achain = 0
            bchain = 1
            ans += b[sb]
            sb += 1
        elif bchain == z:
            bchain = 0
            achain = 1
            ans += a[sa]
            sa += 1
        elif ord(a[sa]) < ord(b[sb]):
            achain += 1
            bchain = 0
            ans += a[sa]
            sa += 1
        else:
            bchain += 1
            achain = 0
            ans += b[sb]
            sb += 1

    print(ans)
