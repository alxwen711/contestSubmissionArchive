import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
(I see why this took nearly an hour to understand in contest last time)

The simplified explanation is to construct a good array equal in length
to the given array that is as "close" as possible. Closeness is defined
as the sum of abs(ai-bi) for i from 1 to 2n in array A (given) and B (created)

the good array must consider EVERY partition into two sets of n values

For n = 1, only possibility is the two values must be equal
Every other n trivially has the all 0 array as an option

n = 2 has the case [2,2,2,2] as an edge case
[0,0,0,0]
[a,b,c,d]
ab = c+d
ac = b+d
ad = b+c
bc = a+d
bd = a+c
cd = a+b
3(a+b+c+d) = ab+ac+ad+bc+bd+cd = ((a+b+c+d)^2-aa-bb-cc-dd)/2

also by brute force -1,-1,-1,2 works

-1,-1,-1,-1,-1,-1,-1,4 works as well (we are kinda seeing the edge lines?)

for a in range(-3,4):
    for b in range(-3,4):
        for c in range(-3,4):
            for d in range(-3,4):
                if a+b == c*d and a+c == b*d and a+d == b*c and b+c == a*d and b+d == a*c and c+d == a*b:
                    print(a,b,c,d)
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    if n == 1:
        print(abs(ar[0]-ar[1]))
    else:
        ans = 0
        for i in ar:
            ans += abs(i)
        if n == 2: # edge case with 2
            tmp = 0
            for j in ar:
                tmp += abs(j-2)
            ans = min(ans,tmp)
        if n % 2 == 0:
            br = [-1]*(2*n)
            br[-1] = n
            ar.sort()
            tmp = 0
            for k in range(2*n):
                tmp += abs(ar[k]-br[k])
            ans = min(ans,tmp)
        print(ans)


            



        
                
