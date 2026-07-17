import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


for _ in range(readint()):
    n,q = readints()
    ar = readar()
    queries = list()
    for _ in range(q):
        tmp = readar()
        queries.append(tmp)
