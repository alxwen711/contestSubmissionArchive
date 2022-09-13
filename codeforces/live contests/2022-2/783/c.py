import sys
from random import randint
def solve(n,ar,index):
    prev = 0
    an = 0
    for a in range(n-index-1):
        x = (prev//ar[index+a+1])+1
        an += x
        prev = x*ar[index+a+1]
    prev = 0
    for b in range(index):
        x = (prev//ar[index-b-1])+1
        an += x
        prev = x*ar[index-b-1]
    return an

def free(n,ar):
    dec = True
    c = 0
    while True:
        if c == n-1: return True
        if dec:
            if ar[c] > ar[c+1]: c += 1
            else: dec = False
        else:
            if ar[c] < ar[c+1]: c += 1
            else: return False

n = int(sys.stdin.readline())
ar = list(map(int,sys.stdin.readline().split()))
v = list()

for i in range(n):
    v.append([ar[i]-min(abs(i-(n//2)),abs(i-((n-1)//2))),-min(abs(i-(n//2)),abs(i-((n-1)//2))),i])
v.sort()
v.reverse()

ans = solve(n,ar,0)
if free(n,ar): ans = n-1
else:
    tmp = 0
    for j in range(min(n,5000)):
        index = v[j][2]
        tmp = solve(n,ar,index)
        if tmp < ans: ans = tmp
print(ans)


"""first = list()
first.append(0)
prev = 0
for j in range(n-1):
    x = (prev//ar[j+1])+1
    first.append(x)
    prev = x*ar[j+1]
print(prev)
print(*first)
   """ 
