import sys

def update(d,p): #choose tasks by most to least
    while not d[p]:
        p -= 1
        if p == 0: break
    return p


for i in range(int(sys.stdin.readline())):
    n,m = map(int,sys.stdin.readline().split())
    ar = list(map(int,sys.stdin.readline().split()))
    #optimal is to assign proficient tasks if possible
    h = [0]*n
    for j in range(m):
        h[ar[j]-1] += 1
    d = {}
    xxx = max(h)
    for f in range(xxx):
        d[f+1] = list()
    for why in range(n):
        if h[why] != 0: d[h[why]].append(why)
    """
    simulate the work?
    
    use dictionary to store tasks with key being quantity of a task remaining
    keep track of the highest key active, once this reaches 0, break
    d[task frequency][task number]
    workers go from 0 to n-1
    """
    w = [0]*n
    progress = xxx
    ans = 0
    spec = list()
    unspec = list()
    escape = False
    while True:
        if not d[progress]: #empty, find new list
            progress = update(d,progress)
        if progress == 0: break #all tasks assigned
        ans += 1 #increment hour
        spec.clear()
        unspec.clear()
        for k in range(n):
            if w[k] == 0:
                if h[k] == 0: unspec.append(k)
                else: spec.append(k)
            else: w[k] = 0
        for g in range(len(spec)):
            d[h[spec[g]]].remove(spec[g])
            h[spec[g]] -= 1
            if h[spec[g]] != 0: d[h[spec[g]]].append(spec[g])
            
        for s in range(len(unspec)):
            if not d[progress]: #update
                progress = update(d,progress)
            if progress == 0:
                escape = True
                break #all tasks assigned
            task = d[progress].pop(0)
            h[task] -= 1
            if h[task] != 0: d[h[task]].append(task)
            w[unspec[s]] = 1
        if escape: break
    if sum(w) != 0: ans += 1
    print(ans)
            
