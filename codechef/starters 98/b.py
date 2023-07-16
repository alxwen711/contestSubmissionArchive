import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
each operation is to remove 3 adj chars in string
if r == 2, pal len 2 exists
5 -> abcba, remove middle 3
8 -> abcddcba, remove ends
anything higher subtracts 6 to get to 5/8 case

if r == 0, pal len 3?
6 -> abccba, remove middle 3 to have aba
anything else translates to 3/6 case
gap cannot be length 2

both need the edge removals multiple of 3
"""
for i in range(readint()):
    n = readint()
    s = input()
    r = n % 3
    if r == 1: print("YES") #remove until 1 chr left
    elif r == 2: #find 2 chrs with gap % 3 == 0 that are same
        ar = list()
        for j in range(26):
            ar.append(list())
        ans = "NO"
        for k in range(n):
            ar[ord(s[k])-97].append(k % 3)
        for l in range(26):
            h = [0]*3
            for m in range(len(ar[l])):
                a = ar[l][-m-1]
                h[a] = 1
                if h[(a+1)%3] == 1 and a == 0:
                    ans = "YES"
                    break
            if ans == "YES": break
        print(ans)
    else: #r == 2 but gap % 3 == 1 to get centerpiece
        ar = list()
        for j in range(26):
            ar.append(list())
        ans = "NO"
        for k in range(n):
            ar[ord(s[k])-97].append(k)
        for l in range(26):
            high = [-1]*3
            low = [-1]*3
            for m in range(len(ar[l])):
                v = ar[l][-m-1]
                a = v % 3
                if high[a] == -1: high[a] = v
                low[a] = v #and high[2]-low[0] > 2
            if low[0] != -1 and high[2] != -1 and high[2] > low[0]: ans = "YES"
            #if low[1] != -1 and high[0] != -1 and high[0]-low[1] > 2: ans = "YES"
            #if low[2] != -1 and high[1] != -1 and high[1]-low[2] > 2: ans = "YES"         
            if ans == "YES": break
        print(ans)
