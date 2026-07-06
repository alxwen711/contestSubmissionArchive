import sys
from copy import deepcopy
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def e(ar):
    if len(ar) == 0: return 0,-1
    ar.sort()
    prev = ar[0][1]
    for k in range(1,len(ar)):
        ar[k][0] = prev+1
        prev = max(ar[k][1],prev)
    br = list()
    ans = 0
    for l in range(len(ar)):
        if ar[l][0] <= ar[l][1]:
            br.append([ar[l][0],ar[l][1],ar[k][2]])
            ans += (ar[l][1]-ar[l][0]+1)*2
    return ans,br

def f(ranges,ar):
    ai = 0
    bi = 0
    ans = list()
    area = 0
    while ai != len(ranges) and bi != len(ar):
        if ranges[ai][1] < ar[bi][0]: ai += 1 #case 6
        elif ranges[ai][0] < ar[bi][1]: bi += 1 #case 1
        elif ranges[ai][0] >= ar[bi][0] and ranges[ai][1] <= ar[bi][1]: #case 3
            ans.append([ranges[ai][0],ranges[ai][1],ar[bi][2]])
            area += (ranges[ai][1]-ranges[ai][0]+1) 
            ai += 1
        elif ar[bi][0] > ranges[ai][0] and ar[bi][1] < ranges[ai][1]: #case 4
            ans.append([ar[bi][0],ar[bi][1],ar[bi][2]])
            area += (ar[bi][1]-ar[bi][0]+1)
            ranges[ai][0] = ar[bi][1]+1
            bi += 1
        elif ar[bi][0] <= ranges[ai][0] and ar[bi][1] < ranges[ai][1]: #case 2
            ans.append([ranges[ai][0],ar[bi][1],ar[bi][2]])
            area += (ar[bi][1]-ranges[ai][0]+1)
            ranges[ai][0] = ar[bi][1]+1
            bi += 1
        else: #case 5
            ans.append([ar[bi][0],ranges[ai][1],ar[bi][2]])
            area += (ranges[ai][1]-ar[bi][0]+1)
            ai += 1
    return area,ans

#always a way to get the same area?
for i in range(readint()):
    n = readint()
    ar = list()
    highest = -4
    for j in range(n):
        a,b,c,d = readints()
        ar.append([a,b,c,d,j])
        highest = max(highest,d)
    #find unique double coverage, use in full
    #check remaining doubles?
    #find single coverage not hit
    bruh = list()
    sin = list()
    dob = list()
    for k in range(n):
        if ar[k][0] == 1 and ar[k][2] == 2:
            bruh.append([ar[k][1],ar[k][3],ar[k][4]])
        elif ar[k][0] == 1 and ar[k][2] == 1:
            sin.append([ar[k][1],ar[k][3],ar[k][4]])
        else:
            dob.append([ar[k][1],ar[k][3],ar[k][4]])
    sin.sort()
    dob.sort()
    area,ranges = e(bruh)
    gaps = list()
    if ranges != -1:
        for snth in range(len(ranges)-1):
            if ranges[snth][1]+1 != ranges[snth+1][0]:
                gaps.append([ranges[snth][1]+1,ranges[snth+1][0]-1])
    else:
        gaps = [[1,highest]]
    top,topr = f(deepcopy(gaps),sin)
    bot,botr = f(deepcopy(gaps),dob)
    area += top
    area += bot
    ans = list()
    for nth in range(n):
        ans.append([0]*4)
    for aa in range(len(topr)):
        iid = topr[aa][2]
        ans[iid] = [1,topr[aa][0],1,topr[aa][1]]
        ans.append([topr[aa][2]])
    
    for bb in range(len(botr)):
        iid = botr[bb][2]
        ans[iid] = [2,botr[bb][0],2,botr[bb][1]]
        ans.append([botr[bb][2]])
    if ranges != -1:
        for cc in range(len(ranges)):
            iid = ranges[cc][2]
            ans[iid] = [1,ranges[cc][0],2,ranges[cc][1]]
            ans.append([ranges[cc][2]])

    print(area)
    for dd in range(n):
        print(*ans[dd])
