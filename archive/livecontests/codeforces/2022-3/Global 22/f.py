import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n,ar):
    h = [0]*n
    d = {}
    for i in range(n):
        if h[i] == 0 and ar[i] != 0:
            for j in range(ar[i]):
                print("?",str(i+1),flush=True)
                x = readint()-1
                if d.get(x) == None: d[x] = list()
                if d.get(i) == None: d[i] = list()
                d[i].append(x)
                d[x].append(i)
                h[i] += 1
                h[x] += 1
    colour = 0
    c = [0]*n
    q = list()
    index = 0
    while index < n:
        if len(q) == 0:
            while index < n:
                if c[index] == 0:
                    q.append(index)
                    break
                else: index += 1
        else:
            search = q.remove(0)
            if c[search] == 0:
                colour += 1
                c = colour
            l = d[colour]
            for snth in range(len(l)):
                if c[l[snth]] == 0:
                    c[l[snth]] = colour
                    q.append(l[snth])
    print("!",*ar)
    flush()
    return


for i in range(readint()):
    n = readint()
    ar = readar()
    solve(n,ar)
