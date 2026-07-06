import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
attempt to build as many ab and ba strings as possible
because if there are too many, they can just be broken into a and b

ABABABABABABABABABAB

(10,0)
(8,1)
...
(0,9)

bababab babababab bababab babab

slice the string into chains of abababa... or bababab....
that are as long as possible, then the optimal states can be
computed (kinda)

prioritize the assignment to:

ab even -> as many ab as possible
ba even -> as many ba as possible
ab odd -> 1 a, then ab or ba spam can be used
ba odd -> 1 b, then ba or ab spam can be used

once there are no more ab/ba allocated, just use the singulars (if they exist)

abababab

process the even chains first, ideally shortest to longest
"""

def f(n,s,a,b,ab,ba):
    chain = 1
    start = s[0]
    prev = s[0]
    extrapairs = 0
    for i in range(1,n):
        if prev != s[i]:
            chain += 1
        else:
            print(start,chain,a,b,ab,ba)
            # determine if it is possible
            if start == "A":
                if chain % 2 == 0: # ab even
                    if ab >= chain//2: ab -= chain//2
                    elif a == 0 or b == 0: return "NO"
                    else:
                        a -= 1
                        b -= 1
                        c = ab
                        ab = 0
                        c += 1
                        if ba >= chain//2-c: ba -= chain//2-c
                        else:
                            r = chain//2-c-ba
                            ba = 0
                            if min(a,b) < r: return "NO"
                            else:
                                a -= r
                                b -= r
                else: # ab odd
                    if a == 0: return "NO"
                    a -= 1
                    extrapairs += chain//2
            else:
                if chain % 2 == 0: # ba even
                    if ba >= chain//2: ba -= chain//2
                    elif a == 0 or b == 0: return "NO"
                    else:
                        a -= 1
                        b -= 1
                        c = ba
                        ba = 0
                        c += 1
                        if ab >= chain//2-c: ab -= chain//2-c
                        else:
                            r = chain//2-c-ab
                            ab = 0
                            if min(a,b) < r: return "NO"
                            else:
                                a -= r
                                b -= r
                else: # ba odd
                    if b == 0: return "NO"
                    b -= 1
                    extrapairs += chain//2
            
            # reset chain
            chain = 1
            start = s[i]
        prev = s[i]

    # compute last chain
    print(start,chain,a,b,ab,ba)
    if start == "A":
        if chain % 2 == 0: # ab even
            if ab >= chain//2: ab -= chain//2
            elif a == 0 or b == 0: return "NO"
            else:
                a -= 1
                b -= 1
                c = ab
                ab = 0
                c += 1
                if ba >= chain//2-c: ba -= chain//2-c
                else:
                    r = chain//2-c-ba
                    ba = 0
                    if min(a,b) < r: return "NO"
                    else:
                        a -= r
                        b -= r
        else: # ab odd
            if a == 0: return "NO"
            a -= 1
            extrapairs += chain//2
    else:
        if chain % 2 == 0: # ba even
            if ba >= chain//2: ba -= chain//2
            elif a == 0 or b == 0: return "NO"
            else:
                a -= 1
                b -= 1
                c = ba
                ba = 0
                c += 1
                if ab >= chain//2-c: ab -= chain//2-c
                else:
                    r = chain//2-c-ab
                    ab = 0
                    if min(a,b) < r: return "NO"
                    else:
                        a -= r
                        b -= r
        else: # ba odd
            if b == 0: return "NO"
            b -= 1
            extrapairs += chain//2
    extrapairs -= ab
    extrapairs -= ba
    if min(a,b) < extrapairs: return "NO"
    return "YES"

for _ in range(readint()):
    s = readin()
    a,b,ab,ba = readints()
    n = len(s)
    ar = list()
    br = list()
    print(f(n,s,a,b,ab,ba))
    """
    acount = 0
    bcount = 0
    for i in range(n):
        if s[i] == "A":
            acount += 1
            if i+1 != n:
                if s[i+1] == "B":
                    ar.append(i)
        else:
            bcount += 1
            if i+1 != n:
                if s[i+1] == "A":
                    br.append(i)
    """
