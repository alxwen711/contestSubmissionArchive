import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

# NOTE: sequence does NOT have to be increasing

ar = list()
br = list()
for _ in range(readint()):
    l,r = readints()
    ar.append(l)
    br.append(r)
b = sum(br)
#print(ar)
#print(br)
if b >= 0 and sum(ar) <= 0:
    print("Yes") # solve from br
    for i in range(len(br)):
        diff = br[i]-ar[i]
        if diff < b:
            br[i] = ar[i]
            b -= diff
        else:
            br[i] -= b
            break
    print(*br)
else: print("No")
