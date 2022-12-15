import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


def f(m,ar):
    state = 0
    for j in range(m):
        a = ar[0][j]
        b = ar[1][j]
        if state == 0:
            if a == "W" and b == "B": state = 2
            elif a == "B" and b == "W": state = 1
        elif state == 1:
            if a == "W": return "NO"
            if b == "B": state = 2
        else: #state == 2
            if b == "W": return "NO"
            if a == "B": state = 1
    return "YES"
            

for i in range(readint()):
    m = readint()
    ar = list()
    for snth in range(2):
        tmp = list()
        x = input()
        for sss in range(m):
            tmp.append(x[sss])
        ar.append(tmp)
    print(f(m,ar))
