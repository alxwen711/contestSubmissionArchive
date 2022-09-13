import sys
def solve(n,ar):
    #seperate singles
    singles = list()
    indexer = 0
    for q in range(len(ar)):
        test = ar[indexer]
        iden = True
        for qq in range(len(test)-1):
            if test[qq] != test[qq+1]:
                iden = False
                break
        if iden: singles.append(ar.pop(indexer))
        else: indexer += 1
        
    while True:
        yea = False
        x = len(ar)
        if x <= 1: break
        for a in range(x):
            for b in range(x-a-1):
                if ar[a][-1] == ar[a+b+1][0]:
                    c = ar.pop(a+b+1)
                    d = ar.pop(a)
                    f = d+c
                    ar.append(f)
                    yea = True
                    break
                elif ar[a][0] == ar[a+b+1][-1]:
                    c = ar.pop(a+b+1)
                    d = ar.pop(a)
                    f = c+d
                    ar.append(f)
                    yea = True
                    break
                if yea: break
            if yea: break
        if not yea: break
    ans = ""
    if len(ar) == 1: ans = ar[0]
    else:
        for k in range(len(ar)):
            ans += ar[k]
    if ans != "":
        t = [0]*26
        ch = ans[0]
        for m in range(len(ans)-1):
            if ans[m+1] != ch:
                t[ord(ch)-65] = 1
                ch = ans[m+1]
                if t[ord(ch)-65] == 1: return "IMPOSSIBLE"
    #add back in singles
    for v in range(len(singles)):
        addin = singles[v]
        added = False
        for why in range(len(ans)):
            if ans[why] == addin[0]:
                ans = ans[:why]+addin+ans[why:]
                added = True
                break
        if not added: ans += addin
    
    return ans
    
    
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(str,input().split()))
    print("Case #"+str(i+1)+": "+solve(n,ar))
    
    
