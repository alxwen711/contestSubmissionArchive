import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
on each row, use a n letter word and the ith position
to then write the word horizontally
words can be duplicated
"""

ar = list()
v = list()
n = readint()
for _ in range(n):
    a,b = readints()
    ar.append((a,b))
    tmp = [0]*26
    v.append(tmp)
m = readint()

words = list()
for _ in range(m):
    s = readin()
    words.append(s)
    for i in range(n):
        if len(s) == ar[i][0]:
            v[i][ord(s[ar[i][1]-1])-97] = 1

for w in words:
    if len(w) != n: print("No")
    else:
        ans = "Yes"
        for i in range(n):
            if v[i][ord(w[i])-97] == 0:
                ans = "No"
                break
        print(ans)



            
