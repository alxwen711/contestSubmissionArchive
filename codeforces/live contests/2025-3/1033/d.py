import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
2 2 2 -> 3 7
2 2 3 -> 3 ? (at most 27)

row count is just enough to guarantee that any a vals in a column will match
combinatorics?
"""

m = 1000000007

facts = [1]
invs = [1]



for i in range(1,201000):
    facts.append((facts[-1]*i) % m)
    invs.append(pow(facts[-1],m-2,m))

def manualcombinatoric(n,k):
    m = 1000000007
    ans = 1
    for i in range(n-k+1,n+1):
        ans = (ans*i) % m
    return (ans*invs[k]) % m

for _ in range(readint()):
    x,y,z = readints()
    rc = ((x-1)*z+1) % m
    c = manualcombinatoric(rc,x)
    print(rc,(c*(y-1)*z+1) % m)
