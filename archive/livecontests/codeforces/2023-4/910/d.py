import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for _ in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    ai = -1
    best = 90999999999999999
    for a in range(n):
        x = ar[a]+br[a]+abs(ar[a]-br[a])
        if x < best:
            ai = a
            best = x
    best = -999999999999999999999
    bi = -1
    for b in range(n):
        x = ar[b]+br[b]-abs(ar[b]-br[b])
        if x > best:
            bi = b
            best = x
    ans2 = 0
    for ss in range(n):
        ans2 += abs(ar[ss]-br[ss])
    br[ai],br[bi] = br[bi],br[ai]
    ans = 0
    for snth in range(n):
        ans += abs(ar[snth]-br[snth])
    #print(ai,bi)
    print(max(ans,ans2))
