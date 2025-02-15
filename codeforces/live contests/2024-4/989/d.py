import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())
"""
222111000
111222000
222000111
220011210
...
000111222

there always exists a move that gets at least 1 thing to its correct position?
1's to front, 0's with 1's, 1's with 2's, passes if 1's >= 0's

use 1's to push rightmost 0's and leftmost 2's as far as possible

0201

"""
for _ in range(readint()):
    n = readint()
    ar = readar()
    singular = False
    zp,tp,olp,orp = -1,999999,999999,-1
    for i in range(n):
        if ar[i] == 0:
            zp = i
        elif ar[i] == 2 and tp == 999999:
            tp = i
        elif ar[i] == 1:
            orp = i
            singular = False
            if olp == 999999:
                olp = i
                singular = True
    ans = list()
    while zp > olp or tp < orp:
        if zp-olp > orp-tp: #swap 0 and 1
            ar[zp],ar[olp] = 1,0
            ans.append((zp+1,olp+1))
            if singular:
                olp,orp = zp,zp
            else:
                if zp > orp: orp = zp
                while ar[olp] != 1:
                    olp += 1
            # adjust 0
            while ar[zp] != 0:
                zp -= 1
        else: # swap 1 and 2
            ar[tp],ar[orp] = 1,2
            ans.append((tp+1,orp+1))
            if singular:
                olp,orp = tp,tp
            else:
                if tp < olp: olp = tp
                while ar[orp] != 1:
                    orp -= 1
            # adjust 2
            while ar[tp] != 2:
                tp += 1
    print(len(ans))
    for a in ans:
        print(a[0],a[1])
