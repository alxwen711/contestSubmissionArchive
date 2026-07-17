import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
lt binary, but there has to be some easier tricks

if same, you must always greedily choose
"""

n,x = readints()
setups = list()
for _ in range(n):
    a,p,b,q = readints()
    setups.append((a,p,b,q))

def f(n,setups,x,b):
    l = b
    cost = 0
    for s in range(n):
        a,p,b,q = setups[s][0],setups[s][1],setups[s][2],setups[s][3]
        if p == q:
            c = max(a,b)
            cost = (x+c-1)//c*p
        elif a == b:
            c = min(p,q)
            cost = (x+a-1)//a*c
        elif a*q > b*p or a*q == b*p and a > b: # use a as base
            base = (x+a-1)//a
            cost = base*p
            for i in range(base-1,max(-1,base-128),-1):
                c = i*p
                r = x-(a*i)
                c += (r+b-1)//b*q
                cost = min(cost,c)
        else: # use b as base
            base = (x+b-1)//b
            cost = base*q
            for i in range(base-1,max(-1,base-128),-1):
                c = i*q
                r = x-(b*i)
                c += (r+a-1)//a*p
                cost = min(cost,c)
        l -= cost
        if l < 0: return False
    return True

low = 1
high = 1000000000000000
while high-low > 1:
    mid = (low+high)//2
    if f(n,setups,mid,x): low = mid
    else: high = mid
if f(n,setups,high,x): print(high)
elif f(n,setups,low,x): print(low)
else: print(0)
