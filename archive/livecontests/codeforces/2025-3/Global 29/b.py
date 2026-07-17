import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
1 1
1 2 1 2
1 3 1 2 3 2

"""


for _ in range(readint()):
    n = readint()
    x = n
    ans = [0]*(2*n)
    order = list()
    for i in range(n,1,-2):
        order.append(i)
    for j in range(n-1,1,-2):
        order.append(j)
    order.append(1)
    ptr = 0
    for i in range(2*n):
        if ptr == n: break
        if ans[i] == 0:
            ans[i] = order[ptr]
            for snth in range(i+order[ptr],2*n,order[ptr]):
                if ans[snth] == 0:
                    ans[snth] = order[ptr]
                    break
            ptr += 1
    print(*ans)
            
