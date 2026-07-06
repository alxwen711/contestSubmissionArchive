"""# shift < and add 1 -> x1
# shift << -> x00
#1,2,4,7,12 (fib summation)
#0,1,2,3,4 (# of remaining bits)
#p is the max num of bits
#how to remove duplicate values? (1,11,100,111,1001,1100...)
#shortened form is where the single 0 is
#sum of first n fib is f(n+2)-1
fib(bitsRemaining+3)-1

2 3
3 4
ans should be 3, but getting 2?
100 -> 1
11 -> 1

"""

def s(b):
    l = len(b)
    prev = False
    for i in range(l):
        if prev:
            if b[-i-1] != "0": return b[:l-i+1]
            else: prev = False
        else:
            if b[-i-1] == "0": prev = True
    return "1"

n,p = map(int,input().split())
ar = list(map(int,input().split()))
for j in range(n):
    ar[j] = format(ar[j],"b")

#create lookup table
a = 1
b = 1
fib = [0]*200000
for i in range(200000):
    c = (a+b) % 1000000007
    if c == 0: fib[i] = 1000000006
    else: fib[i] = c-1
    a = b
    b = c


#print(ar)
short = list()
for k in range(n):
    x = list()
    x.append(int(s(ar[k])))
    x.append(int(ar[k]))
    short.append(x)
short.sort()
#print(short)
ans = 0
f = -9084938
for m in range(n):
    if short[m][0] != f:
        f = short[m][0]
        if p-len(str(short[m][1])) >= 0: ans = (ans + fib[p-len(str(short[m][1]))]) % 1000000007
print(ans)

