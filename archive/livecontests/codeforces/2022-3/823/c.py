import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
find lowest digit and its last occurance
scan up to last occurance and remove all impurities
repeat with whatever is left in the string
keep track of freq, create ar, *ar
"""


for i in range(readint()):
    s = input()
    h = [0]*10
    n = len(s)
    index = 0
    while index != n:
        low = int(s[index])
        last = index
        for j in range(index,n):
            x = int(s[j])
            if x < low:
                low = x
                last = j
            elif x == low:
                last = j
        for k in range(index,last+1):
            x = int(s[k])
            if x == low:
                h[low] += 1
            else:
                h[min(9,x+1)] += 1
        index = last+1
    ar = list()
    for s in range(10):
        for t in range(h[s]):
            ar.append(s)
    print(*ar,sep="")
        
    
