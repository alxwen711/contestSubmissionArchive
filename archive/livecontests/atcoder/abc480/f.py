import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
n <= 20, m <= 100
if you can cut a 1-person slice, you do so?
"""

n,m = readints()
ar = readar()
cuts = 0
target = sum(ar)//m

br = list() # remaining slices
for i in ar:
    m -= i//target
    cuts += i//target
    if i % target != 0: br.append(i % target)


"""
remaining slices sum up to m*target to be split among m people.
All slices are smaller than target
extra cuts is m-maximum number of initial slices that can be made

there is some sort of bitset way for this......

assume we could have ~ 200000 possible sets (20 choose 10)
-> simplify further by only including counts of sizes of the slices used???

formal definition is maximal independent set
"""

n = len(br)
if n != 0:
    ordering = list()
    for i in range(1,2**n):
        s = bin(i)[2:]
        bc = 0
        t = 0
        for j in range(len(s)):
            if s[-j-1] == "1":
                bc += 1
                t += br[j]
                if t > target: break
        if t == target:
            ordering.append((bc,t))
    ordering.sort()
    dp = [0]*(2**n)
            
print(cuts)
