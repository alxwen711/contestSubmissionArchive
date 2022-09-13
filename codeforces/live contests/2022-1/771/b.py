import sys
 
def isSorted(x):
    for j in range(len(x)-1):
        if x[j] > x[j+1]: return 0
    return 1
 
 
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split()))
    if n == 1: print("Yes")
    else:
        odd = list()
        even = list()
        for k in range(n):
            if ar[k] % 2 == 1: odd.append(ar[k])
            else: even.append(ar[k])
        a = isSorted(odd)
        b = isSorted(even)
        if (a == 1 and b == 1): print("Yes")
        else: print("No")
