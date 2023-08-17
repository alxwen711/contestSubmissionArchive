import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
l0 is always at least 1, so it is ALWAYS optimal to
change firs into oaks

EXCEPT for if l0 == 1, then need to make longest for both segments

change first k 0's into 1's first, then repeat with each following

for n = 1 case, something else
"""


def f(ar,a,b,x): #if 1, change to 0
    index = a
    b0 = 0
    b1 = 0
    c0 = 0
    c1 = 0
    for i in range(len(x)):
        y = x[i]
        if index != b+1: #possibly adjust 
            if i == ar[index]: #auto change to 0
                y = "0"
                index += 1
        if y == "0":
            c1 = 0
            c0 += 1
            b0 = max(b0,c0)
        else:
            c0 = 0
            c1 += 1
            b1 = max(b1,c1)
    return b0,b1

def falt(ar,a,b,x): #if 0, change to 1
    index = a
    b0 = 0
    b1 = 0
    c0 = 0
    c1 = 0
    for i in range(len(x)):
        y = x[i]
        if index != b+1: #possibly adjust 
            if i == ar[index]: #auto change to 0
                y = "1"
                index += 1
        if y == "0":
            c1 = 0
            c0 += 1
            b0 = max(b0,c0)
        else:
            c0 = 0
            c1 += 1
            b1 = max(b1,c1)
    return b0,b1




for i in range(readint()):
    n,k = readints()
    x = input()

    if k == 0: #no changes, just calc string
        a,b = f([],1,0,x)
        ans = list()
        for sn in range(1,n+1):
            ans.append(a*sn+b)
        print(*ans)
        continue
    
    ar = list()
    br = list()
    for j in range(n):
        if x[j] == "1": ar.append(j)
        else: br.append(j)

    possible = {}
    #max 0 cases
    if len(ar) > k:
        for l in range(len(ar)-k+1):
            a,b = f(ar,l,l+k-1,x)
            if possible.get(a) == None: possible[a] = b
            else: possible[a] = max(possible[a],b)
    else: possible[n] = 0

    #max 1 cases
    if len(br) > k:
        for m in range(len(br)-k+1):
            a,b = falt(br,m,m+k-1,x)
            if possible.get(a) == None: possible[a] = b
            else: possible[a] = max(possible[a],b)
    else: possible[0] = n
    ans = [0]*n
    for ia in possible.keys():
        b0 = ia
        b1 = possible[ia]
        for ib in range(n):
            ans[ib] = max(ans[ib],(ib+1)*b0+b1)
    print(*ans)
