import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


def cmp(a,b):
    for i in range(len(a)):
        if a[i] != b[-i-1]: return True
    return False

for i in range(readint()):
    n = readint()
    ar = list(map(str,sys.stdin.readline().split()))
    br = list()
    for j in range(len(ar)):
        br.append([len(ar[j]),ar[j]])
    br.sort()
    ans = "YES"
    for k in range(n-1):
        if cmp(br[2*k][1],br[2*k+1][1]):
            ans = "NO"
            break
    print(ans)
