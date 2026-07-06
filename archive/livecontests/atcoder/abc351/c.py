import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n = readint()
ar = readar()
br = list()
for i in ar:
    br.append(i)
    while len(br) > 1:
        if br[-1] == br[-2]:
            x = br.pop()
            br.pop()
            br.append(x+1)
        else: break
print(len(br))
