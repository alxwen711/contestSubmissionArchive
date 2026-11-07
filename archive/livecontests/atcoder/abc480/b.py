import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n,m = readints()
candidates = list()
votes = list()
for _ in range(n):
    s = readin()
    candidates.append(s)
    votes.append(0)
    
for _ in range(m):
    t = readin()
    flag = True
    for i in range(n):
        if t == candidates[i]:
            flag = False
            votes[i] += 1
            break
    if flag: # run one count
        p = list()
        for j in range(n):
            if len(t) == len(candidates[j]):
                mi = 0
                for u in range(len(t)):
                    if t[u] != candidates[j][u]: mi += 1
                if mi == 1: p.append(j)
        if len(p) == 1: votes[p[0]] += 1

for f in votes:
    print(f)
