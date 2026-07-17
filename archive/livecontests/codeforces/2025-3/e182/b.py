import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

# intentionally try to screw up the permutation as much as possible

for _ in range(readint()):
    n = readint()
    ar = readar()
    if ar.count(0) != 1:
        errors = list()
        for i in range(n):
            if ar[i] != i+1:
                errors.append(i)
        if len(errors) == 0: print(0)
        else: print(errors[-1]-errors[0]+1)
    else:
        h = [0]*(n+1)
        index = -1
        for i in range(n):
            if ar[i] == 0: index = i
            else: h[ar[i]] = 1
        for j in range(1,n+1):
            if h[j] == 0:
                ar[index] = j
                break
        errors = list()
        for i in range(n):
            if ar[i] != i+1:
                errors.append(i)
        if len(errors) == 0: print(0)
        else: print(errors[-1]-errors[0]+1)
