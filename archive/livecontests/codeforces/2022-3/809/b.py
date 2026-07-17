import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    ans = [0]*n
    d = {}
    for j in range(n):
        x = ar[j]
        if d.get(x) == None: d[x] = list()
        d[x].append(j)
    for k in range(n):
        x = k+1 #test 1,2,3...
        if d.get(x) != None:
            ans[k] = 1
            c = d[x][0]
            for m in range(len(d[x])):
                if (d[x][m]-c) % 2 == 1:
                    ans[k] += 1
                    c = d[x][m]
    print(*ans)
    """
    longest chain of each number
    chain is consectuitve values seperated by odd # of positions
    """
