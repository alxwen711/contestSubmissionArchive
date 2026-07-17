import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
A -> C
A -> D
B -> D
ABCD
ABDC
BACD
BADC
ACBD

place all apples (a)
place all grapes (d)
place all oranges, with some parameter being how many oranges at the end (b)
place all bananas in some slotting motion (c)
"""

m = 998244353

facts = [1]
invs = [1]
for i in range(1,3000001):
    facts.append((facts[-1]*i) % m)
    invs.append(pow(facts[-1],m-2,m))
#print("done building")
a,b,c,d = readints()
ans = 0

def choose(x,y):
    if x < y: return 1
    #print(x,y)
    return (facts[x]*invs[y]*invs[x-y]) % m

for i in range(b+1):
    # a slots choose b-i -> b-i+a-1 choose a
    # d+i slots choose c -> c+d+i-1 choose d+i
    # b-i 0's, a-1 1's
    # c 0's, d+i 1's
    ans += choose(b-i+a-1,a-1)*choose(c+d+i,d+i)
print(ans % m)
