import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())
"""
odd length array: literally impossible
even length array: as long as there is no clear majority
1 2 1 2 1 2
a_i is from 1 to 3, very big clue there
1 1 2 2 3 3 ?
1 2 3 2 1 ?

1 1 1 1 2 2 2 2 3 3 3 3
2 1
"""

for _ in range(readint()):
    n,q = readints()
    ar = readar()
    one = [0]
    two = [0]
    three = [0]
    for i in range(n):
        one.append(one[-1])
        two.append(two[-1])
        three.append(three[-1])
        if ar[i] == 1: one[-1] += 1
        elif ar[i] == 2: two[-1] += 1
        else: three[-1] += 1
    #print(one)
    #print(two)
    #print(three)
    for _ in range(q):
        a,b = readints()
        if (b-a) % 2 == 0: print("No")
        else:
            x = max(one[b]-one[a-1],two[b]-two[a-1],three[b]-three[a-1])
            print("Yes" if 2*x == (b-a+1) else "No")
