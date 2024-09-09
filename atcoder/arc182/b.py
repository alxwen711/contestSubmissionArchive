import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    n,k = readints()
    ans = [1]*n
    q = [n]
    for _ in range(k-1):
        nq = list()
        for i in q:
            if i != 1:
                nq.append(i//2)
                nq.append((i+1)//2)
            else:
                nq.append(1)
        q = nq
        index = 0
        c = 0
        v = 0
        for j in range(n):
            ans[j] *= 2
            ans[j] += v
            c += 1
            if c == q[index]:
                index += 1
                c = 0
                v ^= 1
    print(*ans)
    """
    d = {}
    for j in ans:
        while j != 0:
            d[j] = 1
            j //= 2
    print(len(list(d.keys()))+1)
    """
