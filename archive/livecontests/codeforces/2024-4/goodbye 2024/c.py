import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
after each division process, each of the remaining segments will be equal len
thus, only odd values need to be triggered
"""

for _ in range(readint()):
    n,k = readints()
    l = n
    splits = list()
    ans = 0
    while l >= k:
        if l % 2 == 0: # even split
            splits.append(0)
        else: # observation split
            base = l//2+1
            dist = n
            count = 1
            for i in splits:
                if i == 0:
                    dist //= 2
                    base += base+(dist*count)
                    count *= 2
                else:
                    dist //= 2
                    base += base+((dist+1)*count)
                    count *= 2
            ans += base         
            splits.append(1)
        l //= 2
    print(ans)
