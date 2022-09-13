import sys

#input/output functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
0 0
1 0
2 0
3 0
4 1
5 2
6 5
7 8
8 17
9 26
10 39
11 52
12 76
13 100
14 130
15 160
16 215
17 270
18 333
19 396
20 480
21 564
22 658
23 752
24 890
25 1028
26 1178
27 1328
28 1509
29 1690
30 1885
31 2080
32 2365
33 2650
34 2951
35 3252
36 3594
37 3936
38 4296
39 4656
40 5098
41 5540
42 6002
43 6464
44 6977
45 7490
46 8025
"""
def t(j,k,l):
    a = j ^ k
    b = k ^ l
    c = j ^ l
    if a + b > c and b + c > a and a + c > b: return True
    return False

#determine possible pattern
ar = list()
for i in range(65):
    ans = 0
    for j in range(i+1):
        for k in range(i+1):
            for l in range(i+1):
                if t(j,k,l): ans += 1
    ar.append(ans//6)
    print(bin(i),bin(ans))
for o in range(len(ar)//2):
    print(2*o+1,ar[2*o+1]//2)
    
