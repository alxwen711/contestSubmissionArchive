import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
reconstruct ar based on maximum prefixes in br

pause sequence everytime a new maximum is attained
if there is multiple blanks, use it to decrease the sum
as far as possible until the last one places it just in range
if only one blank exists, numerical value is forced
then verify the array is actually correct (greedy?)
"""

blankval = -500000000000 # large enough to outscale inputs

for _ in range(readint()):
    n = readint()
    s = readin()
    ar = readar()
    br = readar()
    mv = -9999999999999999999999999999999999999
    blanks = list()
    cs = 0 # current sum
    for i in range(n):
        if s[i] == "0":
            blanks.append(i)
        else:
            cs += ar[i]
        if br[i] > mv: # fill in blanks (if existing)
            mv = br[i]
            if len(blanks) != 0:
                for j in range(len(blanks)-1):
                    ar[blanks[j]] = blankval
                    cs += blankval
                ar[blanks[-1]] = mv-cs
                cs = mv
            blanks = list()
    for b in blanks:
        ar[b] = blankval
    ans = "Yes"
    mv = -99999999999999999999999999999
    cs = 0
    for ii in range(n):
        cs += ar[ii]
        mv = max(mv,cs)
        if mv != br[ii]:
            ans = "No"
            break
    print(ans)
    if ans == "Yes":
        print(*ar)
    
