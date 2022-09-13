import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
uaqiaeea

[a,a,a,a,a]
  [a,a,a]
    [a]

decc
[]

[a,d,a]
[d]
"""

def solve(s):
    ar = list()
    tmp = list()
    for j in range(len(s)-1):
        if s[j]==s[j+1]: tmp.append(0)
        else: tmp.append(1)
    ar.append(tmp)
    for k in range(len(s)//2-1):
        if sum(ar[k]) == len(ar[k]): break
        tmp = list()
        for l in range(len(s)-3-(2*k)):
            a,b,c = ar[k][l],ar[k][l+1],ar[k][l+2]
            one,two,three,four = s[l],s[l+1],s[l+(2*k)+2],s[l+3+(2*k)]
            if a == 0: #43 case
                if four > three: a = -1
                if three > four: a = 1
            if b == 0: #14/41 case
                if one != four: b = 1
            if c == 0: #12 case
                if one > two: c = -1
                if two > one: c = 1
            ca = min(a,b)
            cb = min(b,c)
            #[1,2,???,3,4] cases: 12,14,41,43 lastb lastc
            tmp.append(max(ca,cb))
        ar.append(tmp)
    #print(ar)
    
    if ar[-1][0] == -1: return "Bob"
    elif ar[-1][0] == 0: return "Draw"
    else: return "Alice"
            

for i in range(readint()):
    s = input()
    print(solve(s))
    """
    """
