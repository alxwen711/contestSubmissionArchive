a,b,c,d,e,f = map(int,input().split())

"""
a is top, d is bottom
d+c is length of longest
"""

base = a
height = b+c
inc = [0]*height
for i in range(height):
    if b > i: inc[i] += 1
    else: inc[i] -= 1
for j in range(height):
    if f > j: inc[j] += 1
    else: inc[j] -= 1
for k in range(height):
    inc[k] //= 2
ans = 0
for l in range(height):
    ans += base
    base += inc[l]
    ans += base
print(ans)
