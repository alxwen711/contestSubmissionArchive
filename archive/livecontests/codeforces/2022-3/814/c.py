import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,q = readints()
    ar = readar()
    st = [0]*n
    win = [0]*n
    champ = 0
    challenger = 1
    turn = 0
    while turn < 200000:
        turn += 1    
        if ar[champ] < ar[challenger]:
            champ = challenger
        if st[champ] == 0: st[champ] = turn
        win[champ] += 1
        if ar[champ] == n:
            win[champ] = 1000000000
            break
        challenger += 1
    for j in range(q):
        a,b = readints()
        c,d = st[a-1],win[a-1]
        if c == 0 or b < c: print(0)
        else: print(min(d,b-c+1))
    
