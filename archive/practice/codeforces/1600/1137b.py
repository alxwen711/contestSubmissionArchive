import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
101

101 101 101 101 x
1010101010101010101010101

10010010 1001001010010010 100
find smallest k such that entire t can be made from sequence of k
finish with first few letters of k
how to deal with indent?

11 0001 0001 0001 0001
11001010 11001010 111
"""

def segment(x):
    #return the last value here
    ar = [0]*len(x)
    for i in range(1,len(x)):
        v = ar[i-1]
        found = True
        while x[i] != x[v] and v > 0:
            v = ar[v-1]
        if x[i] == x[v]:
            v += 1
        ar[i] = v
    length = len(x)-ar[-1]
    """
    index = 0
    length = 1
    for i in range(1,len(x)):
        if x[index] == x[i]:
            index += 1
            if index == length:
                index = 0
        else:
            index = 0
            length = i+1
    """
    return x[:length]
    

bruh = input()
what = input()
b0,b1 = 0,0
w0,w1 = 0,0
for i in range(len(bruh)):
    if bruh[i] == "1": b1 += 1
    else: b0 += 1
what = segment(what)
for j in range(len(what)):
    if what[j] == "1": w1 += 1
    else: w0 += 1
if w0 == 0 or w1 == 0:
    print("0"*b0+"1"*b1)
else:
    maximum = min(b0//w0,b1//w1)
    #incoming shenanigans
    ans = list()
    ind = 0
    b0 -= (w0*maximum)
    b1 -= (w1*maximum)
    lololol = len(what)
    for why in range(maximum):
        for how in range(lololol):
            ans.append(what[how])
    while b0 != 0 and b1 != 0:
        if what[ind] == "0":
            b0 -= 1
            ans.append("0")
        else:
            b1 -= 1
            ans.append("1")
        ind += 1
    for ff in range(b1):
        ans.append("1")
    for potato in range(b0):
        ans.append("0")
    print(*ans,sep="")
    """
    ans = what*maximum
    ind = 0
    b0 -= (w0*maximum)
    b1 -= (w1*maximum)
    while b0 != 0 and b1 != 0:
        if what[ind] == "0":
            b0 -= 1
            ans += "0"
        else:
            b1 -= 1
            ans += "1"
        ind += 1
    ans += "1"*b1
    ans += "0"*b0
    print(ans)
    """
