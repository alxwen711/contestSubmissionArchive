import sys

def solve(ar,c,m,even,odd):
    total = m*len(ar)
    dist = total-c
    minSing = 0
    ans = 0
    singDays = 0
    doubDays = 0
    if m % 2 == 0: minSing = odd
    else: minSing = even
    remain = dist-minSing
    if minSing*2 > remain: ans = minSing*2-1
    elif minSing*2 == remain: ans = minSing*2
    else:
        ans = minSing*2
        remain = dist-(minSing*3)
        ans += 2*(remain//3)
        ans += (remain%3)
    return ans
    
    
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    m = max(ar)
    total = m*len(ar)
    odd,even,c = 0,0,0
    for j in range(len(ar)):
        x = ar[j]
        c += x
        if x % 2 == 0: even += 1
        else: odd += 1
    print(min(solve(ar,c,m,even,odd),solve(ar,c,m+1,even,odd)))
    """
    if minSing > (dist+1)//3:
        singDays = minSing
        remain = dist-minSing
        doubDays = remain//2
        if remain % 2 == 1: singDays += 1
    else:
        singDays = dist//3
        doubDays = dist//3
        if dist % 3 == 1: singDays += 1
        elif dist % 3 == 2: doubDays += 1
    if singDays > doubDays:
        ans = 2*singDays-1
    else:
        ans = 2*doubDays
    """
