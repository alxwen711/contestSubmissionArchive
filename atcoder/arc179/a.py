import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
if k > 0, then order sort

"""
n,k = readints()
ar = readar()
if k > 0:
    print("Yes")
    ar.sort()
    print(*ar)
else:
    ar.sort()
    ar.reverse()
    ans = "Yes"
    c = 0
    for i in ar:
        c += i
        if c < k:
            ans = "No"
            break
    print(ans)
    if ans == "Yes": print(*ar)
