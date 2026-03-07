import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readfloats = lambda: list(map(float,sys.stdin.readline().split()))

"""
tti - transmission time interval
"""




def normal(frame,r):
    n = len(frame)
    s = sum(frame)
    if s == 0: return [0]*n #no frames actually active at this time
    ans = list()
    for c in frame:
        ans.append(r*(c/s))
    """
    if sum(ans) > r:
        diff = (sum(ans)-r) #extremely small marginal
        for u in range(n):
            ans[u] = max(ans[u]-diff,0)
    """
    return ans

















# actual input and processing starts here
n = readint()
k = readint()
t = readint()
r = readint()
sinrs = list() #interpret as [time (t)][cell (k)][rgb (r)][user (n)]
for _ in range(t):
    tmp3 = list()
    for _ in range(k):
        tmp2 = list()
        for _ in range(r):
            tmp = readfloats()
            tmp2.append(tmp)
        tmp3.append(tmp2)
    sinrs.append(tmp3)

#interference factors, interpret as [cell (k)][rgb (r)][user (m)][user (n)]
#interference between two users m/n, m==n should be 0?
intfactors = list()
for _ in range(k):
    tmp3 = list()
    for _ in range(r):
        tmp2 = list()
        for _ in range(n):
            tmp = readfloats()
            tmp2.append(tmp)
        tmp3.append(tmp2)
    intfactors.append(tmp3)
"""
frames
for frames[x]:

frames[x][0] -> frame ID
frames[x][1] -> TBS size
frames[x][2] -> user ID
frames[x][3] -> TTI start time
frames[x][4] -> TTI's allowed (time limit)
"""
j = readint()
frames = list()
for _ in range(j):
    tmp = readar()
    frames.append(tmp)

# R is the limit of how much power we can throw per time frame

loadset = list() #[time][user]
for _ in range(t):
    tmp = [0]*n
    loadset.append(tmp)

for f in frames:
    boost = f[1]/f[4]
    for g in range(f[3],f[3]+f[4]):
        loadset[g][f[2]] += boost

ans = list()
"""
solve frame by frame, [cell k][rgb r]
each cell can have at most R power

somehow this isn't half bad, now just rearrange values to
cause as little collision as possible
"""

rgbs = k*r

for frame in loadset:
    distribution = normal(frame,0.99999999)
    for _ in range(rgbs):
        ans.append(distribution)
for an in ans:
    print(*an)
