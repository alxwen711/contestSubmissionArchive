import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
O(n log n) is likely needed (O(n**1.5) is extremely unlikely)
could try dual hash traversal method, probably unlikely to work

TLEs on specific cases as expected (500000 a's)
there are at most 500000 characters total in the substring queries

O(n**1.5) -> 353 million
shorter than sqrt(n) -> direct lookup
longer than sqrt(n) -> collision method

with collision method, at worst being done sqrt(n) times

technically this makes it O(n**1.5), too much overhead?

okay even with c++ I'm pretty sure this is still too slow
"""


import random

HMOD = 2147483647
HBASE1 = random.randrange(HMOD)

class Hashing:
    def __init__(self, s, mod=HMOD, base1=HBASE1):
        self.mod, self.base1 = mod, base1
        self._len = _len = len(s)
        f_hash, f_pow = [0] * (_len + 1), [1] * (_len + 1)
        for i in range(_len):
            f_hash[i + 1] = (base1 * f_hash[i] + s[i]) % mod
            f_pow[i + 1] = base1 * f_pow[i] % mod
        self.f_hash, self.f_pow = f_hash, f_pow
        
    def hashed(self, start, stop):
        return (self.f_hash[stop] - self.f_pow[stop - start] * self.f_hash[start]) % self.mod

s = readin()
ar = list()
for i in s:
    ar.append(ord(i))
hs = Hashing(ar)
n = len(ar)
distances = {}
l = 1
while l <= n:
    distances[l] = {}
    for j in range(n-l+1):
        x = hs.hashed(j,j+l)
        if distances[l].get(x) == None: distances[l][x] = list()
        distances[l][x].append(j)
    l *= 2
l = 3
while l*l < n and l <= 100:
    if distances.get(l) == None:
        distances[l] = {}
        for j in range(n-l+1):
            x = hs.hashed(j,j+l)
            if distances[l].get(x) == None: distances[l][x] = list()
            distances[l][x].append(j)
    l += 1
#print(distances)
for _ in range(readint()):
    t = readin()
    br = list()
    for j in t:
        br.append(ord(j))
    bl = len(br)
    hss = Hashing(br)
    dist = 1
    while True:
        if dist*2 <= bl: dist *= 2
        else: break
    if dist == bl or (bl*bl < n and bl <= 100): # direct lookup
        x = hss.hashed(0,bl)
        if distances[bl].get(x) != None: print(len(distances[bl][x]))
        else: print(0)
    else: # collision cmp method
        x = hss.hashed(0,dist)
        target = bl-dist
        y = hss.hashed(target,bl)
        if distances[dist].get(x) != None and distances[dist].get(y) != None:
            ans = 0
            aindex = 0
            bindex = 0
            while aindex != len(distances[dist][x]) and bindex != len(distances[dist][y]):
                r = distances[dist][y][bindex]-distances[dist][x][aindex]
                if r == target:
                    ans += 1
                    aindex += 1
                    bindex += 1
                elif r > target: aindex += 1
                else: bindex += 1
            print(ans)
        else: print(0)
