import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,b = readints()
    ar = readar()
    br = list() #contain values with 1 bits of b
    for j in ar:
        if j & b == b: br.append(j-b)
    # how to tell that two values share no other bits?
    br.sort()
    ans = "NO"
    if len(br) == 0:
        print(ans)
        continue
    c = br[0]
    for k in range(len(br)-1):
        c = c & br[k+1]
    if c == 0: ans = "YES"
    print(ans)
