import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
first make sure there's an even number of ( and )
then determine min replacement/swaps to complete
take lower cost option
"""

n,a,b = readints()
s = sys.stdin.readline()
ar = list()
count = 0
for i in range(2*n):
    ar.append(s[i])
    if s[i] == "(": count += 1
    else: count -= 1
ans = 0
#print(count)
if count > 0:
    for j in range(2*n):
        if ar[-j-1] == "(":
            count -= 2
            ar[-j-1] = ")"
            ans += b
            if count == 0: break
elif count < 0:
    for j in range(2*n):
        if ar[j] == ")":
            count += 2
            ar[j] = "("
            ans += b
            if count == 0: break

count = 0
mc = 0
for k in range(2*n):
    if ar[k] == "(": count += 1
    else: count -= 1
    mc = min(mc,count)
mc = (abs(mc)+1)//2
#print(ar)
#print(mc)
ans += min(a,2*b)*mc
print(ans)
