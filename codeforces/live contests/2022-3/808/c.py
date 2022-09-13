import sys
for i in range(int(sys.stdin.readline())):
    n,q = map(int,sys.stdin.readline().split())
    ar = list(map(int,sys.stdin.readline().split()))
    ans = [0]*n
    m = [-1]*n
    req = 0
    #take all easy tests
    for j in range(n):
        if ar[-j-1] <= q:
            ans[-j-1] = 1
            req = max(req,ar[-j-1])
        m[-j-1] = req
    #find cost
    iq = q
    d = {}
    cost = 0
    free = 0
    for k in range(n):
        if ar[-k-1] <= iq:
            if d.get(ar[-k-1]) == None: d[ar[-k-1]] = 0
            d[ar[-k-1]] += 1
        else:
            cost += 1
            if d.get(iq) != None: cost += d[iq]
            iq -= 1
        free += 1
        if cost >= q: break #overcost, will have to sack a few
    #print(free)
    for s in range(free):
        ans[-s-1] = 1
    print(*ans, sep="")
