import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
ai * bi * (i mod j)

B multipliers:
00000000000
10101010101
12012012012
12301230123
12340123401
12345012345
12345601234
12345670123
12345678012
12345678901

the number of segments to adjust should keep decreasing by
iterating through b mults

number of segments should drop fast enough for this to be computable
"""

p = 998244353

n,m = readints()
ar = readar()
br = readar()

prefix = [0]*(n+1) # reverse of [0,an,2an+a{n-1}...]
for i in range(n-1,-1,-1):
    prefix[i] = prefix[i+1]+ar[i]

prefix2 = [0]*(n+1) # reverse of [0,sum 1..n, sum 1..n+sum 1..n-1]
for j in range(n-1,-1,-1):
    prefix2[j] = prefix2[j+1]+prefix[j]
    

segments = [0]*n
ans = 0
for i in range(1,m):
    mv = i+1 # also segment length
    nsegments = [0]*((n+mv-1)//mv)
    for s in range(len(nsegments)):
        # fixes from position s*i to s*i+i-1
        a,b = s*mv,min(s*mv+mv-1,n-1) # a mod is 0, b mod is i-1 unless at end
        score = prefix2[a]-prefix2[b+1]-(prefix[b+1]*(b-a+1))
        if b % mv == i: score -= mv*ar[b]
        nsegments[s] = score
    segments = nsegments
    #print(segments)
    ans += sum(segments)*br[i]
print(ans % p)
