import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]

"""
number of subarrays that have the maximum
increase subsequentially by 1 each time
inclusion/exclusion to track maximum

1121234
7604000

- find the last 1, manually compute dist
- for each 1 afterwards, either:
- it reaches with a possibly higher total (may extend further)
- hits a snag and is early cut
- optimaly each value is hit only once

WA1, testcase hidden
typo fix solved this (41)
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    ans = [0]*n
    mv = [0]*n
    for i in range(n-1,-1,-1):
        if ar[i] == 1: # starting point
            m = 1
            index = i+1
            while index != n:
                if ans[index] != 0:
                    m = max(m,mv[index])
                    index += ans[index]
                elif m+1 >= ar[index]:
                    m = max(m,ar[index])
                    index += 1
                else: break
            ans[i] = index-i
            mv[i] = m
    print(sum(ans))
