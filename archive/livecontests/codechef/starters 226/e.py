import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
1,5,17,?

maximum apart distance
consider (score of sequence, last added value)
just compute all the answers up to 2000 as part of the dp
could you just not compute everything? O(n^3)??

there is some sort of O(n^2) dp equation here but if this exists
then what is stopping me from using it

so even with all this 2000 ends up with the wrong answer (645128103)
"""

base = [[0],[1]]#,[1,1],[1,2,1]] #[last added value][f value] = count
m = 998244353

for i in range(2,2001):
    if i % 10 == 0: print(i)
    tmp = [0]*i
    tmp[0] = 1
    for j in range(1,i): # j is the f value being computed
        for k in range(i-1,0,-1): # k is the previous added value
            if i-k == j:
                for l in range(min(j+1,k)):
                    tmp[j] += base[k][l]
            elif i-k < j:
                if k > j: tmp[j] += base[k][j]
            else: break # not going to add anymore anyways
        tmp[j] = tmp[j] % m
    base.append(tmp)

"""
for i in range(2,2001):
    if i % 10 == 0: print(i)
    tmp = [0]*i
    tmp[0] = 1
    for j in range(1,i):
        for k in range(j):
            tmp[max(i-j,k)] += base[j][k]
    for t in range(i):
        tmp[t] = tmp[t] % m
    base.append(tmp)
"""

ans = []
v = 0
for i in range(2001):
    for j in range(len(base[i])):
        v = (v+base[i][j]*j) % m
    ans.append(v)


for _ in range(readint()):
    n = readint()
    print(ans[n])
