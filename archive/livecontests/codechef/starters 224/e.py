import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
ordering of values does not matter

keep track of following:

(lowest frequency up to break, smallest total to break/breakpoint)

there is a certain point at which f(S) will never decrease further

break finished entries can be aggregated to a single sum
0,0,0,0,0,0,0,5,5,5??? ans here is 4

actually not on frequency

fastest paths? -> decrease higher to empty point, decrement all by 1
"""

facts = [1]
invs = [1]
m = 998244353

for i in range(1,100001):
    facts.append((facts[-1]*i) % m)
    invs.append(pow(facts[-1],m-2,m))


for _ in range(readint()):
    n = readint()
    ar = readar()
    ar.sort()
