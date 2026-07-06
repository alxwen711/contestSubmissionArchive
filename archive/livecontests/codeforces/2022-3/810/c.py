import sys

#input/output functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


def solve(length,rows,c,ar):
    m = 2*length
    count = list()
    for j in range(c):
        if ar[j] >= (length*rows): return True #solo colour
        if ar[j] >= m: count.append(ar[j]//length)
        else: count.append(0)
    if sum(count) < rows: return False
    elif rows % 2 == 0: return True
    else:
        for k in range(c):
            if count[k] > 2: return True
        return False
        
for i in range(readint()):
    a,b,c = readints()
    ar = readar()
    #try a
    if solve(a,b,c,ar): print("Yes\n")
    #try b
    elif solve(b,a,c,ar): print("Yes\n")
    else: print("No\n")
