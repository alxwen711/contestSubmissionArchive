import sys
def solve(ar,early,late,k,n):
    if n == 2: #edge case, make sure this is correct
        if ar[0] == 0 and ar[1] == 0: return 0
        elif ar[0] == 0 and ar[1] == 1: return 1
        elif ar[0] == 1 and ar[1] == 1: return 11
        elif ar[0] == 1 and ar[1] == 0 and k != 0: return 1
        else: return 10
    #end swap
    es = False
    cost = n-late-1
    if k >= cost:
        ar[late] = 0
        ar[-1] = 1
        k -= cost
        es = True
    #front swap if possible
    cost = early
    if early == late and es == True: cost = 9853476983478408020704670
    if k >= cost:
        ar[early] = 0
        ar[0] = 1
    y = sum(ar)
    return (y-ar[-1])*10+(y-ar[0])
    
        

for i in range(int(sys.stdin.readline())):
    n,k = map(int,sys.stdin.readline().split())
    s = input()
    #1.........1 is optimal
    ar = list()
    early = 99999999999
    late = -9999999999999999999
    for j in range(n):
        x = int(s[j])
        ar.append(x)
        if x == 1: late = j
        if x == 1 and early == 99999999999: early = j
    print(solve(ar,early,late,k,n))
