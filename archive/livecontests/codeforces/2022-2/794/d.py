import sys
"""
2354
A AB A AB BA BA A AB AB BA BB BA BB
3 As
4 Bs
4 ABs
4 BBs

1111
ABAABB

chains of 3:
ABA,BAB -> could be anything
AAB,ABB -> only AB
BAA,BBA -> only BA
AAA,BBB -> no double

3 searches:
exclusive AB and BA fill
normal AB and BA fill
single fill

1 1 2 3

current: ABAB AB BA ABAB
actual: A BA BA B BA AB AB
updated: A BA BA B BA AB AB
use greedy??

?
paint chains of 3+ (2)
exclusive fill using only 0
normal fill with 0 or 2
single fill with 0 or 2

1 3 3 10
B BA B AB AB AB B BA BA BA BA BA BA BA A BA BA

1 1 2 2
BA AB BAB BA A

chains of 4:
AABB -> must be AB
BBAA -> must be BA

search 1: AABB, BBAA
search 2: chain length, keep 3+, solve 1 and 2
search 3: ?
AB -> even A chains, odd A chains, odd B chains, even B chains
BA -> even B chains, odd B chains, odd A chains, even A chains
above uses greedy?
"""

def solve(a,b,c,d,s):
    la,lb = s.count("A"), s.count("B")
    #check if right num of As and Bs
    if la != a+c+d or lb != b+c+d: return "NO"
    n = la+lb
    h = [0]*n #track what has been used
    
    #exclusive AB/BA fill
    for i in range(n-2):
        if s[i] == "A" and s[i+1] == "B" and s[i+2] == "B" and h[i] == 0 and h[i+1] == 0 and c != 0:
            h[i] = 1
            h[i+1] = 1
            c -= 1
        elif s[i] == "B" and s[i+1] == "A" and s[i+2] == "A" and h[i] == 0 and h[i+1] == 0 and d != 0:
            h[i] = 1
            h[i+1] = 1
            d -= 1

    #normal AB/BA fill
    for j in range(n-1):
        if s[j] == "A" and s[j+1] == "B" and h[j] == 0 and h[j+1] == 0 and c != 0:
            h[j] = 1
            h[j+1] = 1
            c -= 1
        elif s[j] == "B" and s[j+1] == "A" and h[j] == 0 and h[j+1] == 0 and d != 0:
            h[j] = 1
            h[j+1] = 1
            d -= 1
    if c != 0 or d != 0: return "NO"
    for k in range(n):
        if h[k] == 0:
            if s[k] == "A": a -= 1
            else: b -= 1
    if a != 0 or b != 0: return "NO"
    return "YES"


for ireallydontknowwhattocallthis in range(int(sys.stdin.readline())):
    a,b,c,d = map(int,sys.stdin.readline().split())
    s = input()
    print(solve(a,b,c,d,s))
