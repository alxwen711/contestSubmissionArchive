import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
2250 > 1000 points with similar solve rate, may as well skip C2

layering in the brackets is important

swap can occur between any ( and following ) on same layer

if the count of numbers is the same, then there must be a solve? No

(()()((())())())

each outer bracket layer acts as a shell for the inner children
after each swap, there has to be the same number of children contained
empty brackets can be considered as having no children

if a setup has children, the number can vary but it must keep at least 1,
and cannot have all of the children

configure so that each parent has the correct number of children

((()))()()()() -> (1)(0)(0)(0)(0) could have two brackets with children
how many brackets are encapsulating other brackets? (case 4 fails)

number of raw components same, impossible
((()))(()) -> (1)(1)
()((())()) -> (0)(2), could transform to (1)(0)(0) or (0)(0)(1)

anything on 0 must stay at 0
"""

for _ in range(readint()):
    n = readint()
    s = readin()
    t = readin()
    si = 0
    sc = 0
    while si < n:
        if si == n-1:
            si += 1
            sc += 1
        elif s[si] == "(" and s[si+1] == ")": si += 2
        else:
            si += 1
            sc += 1
    ti = 0
    tc = 0
    while ti < n:
        if ti == n-1:
            ti += 1
            tc += 1
        elif t[ti] == "(" and t[ti+1] == ")": ti += 2
        else:
            ti += 1
            tc += 1
    print("YES" if sc == tc else "NO")
    print(sc,tc)
