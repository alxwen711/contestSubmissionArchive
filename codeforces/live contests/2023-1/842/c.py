import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n,ar):
    a = [1]*n
    b = [1]*n
    apos = list()
    bpos = list()
    ansa = [0]*n
    ansb = [0]*n
    for i in range(n):
        x = ar[i]
        if a[x-1] == 1:
            a[x-1] = 0
            ansa[i] = x
            apos.append([x,i])
        elif b[x-1] == 1:
            b[x-1] = 0
            ansb[i] = x
            bpos.append([x,i])
        else: #val appears 3 times, impossible
            print("NO")
            return
    apos.sort()
    apos.reverse()
    bpos.sort()
    bpos.reverse()
    aindex = 0
    bindex = 0
    for j in range(n-1,-1,-1):
        if a[j] == 1:
            val = j+1
            if val > bpos[aindex][0]:
                print("NO")
                return
            ansa[bpos[aindex][1]] = val
            aindex += 1
        if b[j] == 1:
            val = j+1
            if val > apos[bindex][0]:
                print("NO")
                return
            ansb[apos[bindex][1]] = val
            bindex += 1
    print("YES")
    print(*ansa)
    print(*ansb)
    return


for i in range(readint()):
    n = readint()
    ar = readar()
    solve(n,ar)
