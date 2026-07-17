import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
the right side should attempt to remove as many 3s as possible in
net total (1 and 2 are -, 3 is +)
after that every remaining build can be checked
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    index = n-1
    score = 1 if ar[-1] == 3 else -1
    best = score
    for i in range(n-2,1,-1):
        score += 1 if ar[i] == 3 else -1
        if score > best:
            best = score
            index = i
    # index to n-1 forms the 3rd
    br = ar[:index]
    ba,bb,bc = br.count(1),br.count(2),br.count(3)
    aa,ab,ac = 0,0,0
    ans = "NO"
    for i in range(len(br)-1):
        if br[i] == 1:
            aa += 1
            ba -= 1
        elif br[i] == 2:
            ab += 1
            bb -= 1
        else:
            ac += 1
            bc -= 1
        if aa >= ab + ac and ba + bb >= bc:
            ans = "YES"
            break
    print(ans)
