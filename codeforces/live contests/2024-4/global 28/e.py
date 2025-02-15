import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
there cannot exist a clique of 4 points, two on each side
where all edges between them have the same colour

there cannot exist a rectangle in the grid
1 2 1
2 1 2
1 1 2
2 1 1

this setup has a 6 chain of 1's (1,1,3,2,3,3)

enclosed perimeter must not be creatable by alternating between
vertical and horizontal steps

1 2 1
2 1 2
1 1 2
2 2 1

this would be a valid solution

1 1 2 2
2 2 1 1
1 2 1 2
2 1 2 1

2 4 has no solution?
assume any case of x 2x has no solution

if a solution is found with 1/mth of the edges, maybe a cyclic solution exists?


3 5
1 2 3 1 2
2 3 1 2 3
3 1 2 3 1
1 1 2 2 3
2 2 3 3 1
3 3 1 1 2

3 6?
1 2 3 1 2 3
2 3 1 2 3 1
3 1 2 3 1 2
1 1 2 2 3 3
3 1 1 2 2 3
1 2 3 2 1 3



4 7
1 2 3 4 1 2 3
2 3 4 1 2 3 4
3 4 1 2 3 4 1
4 1 2 3 4 1 2
1 2 3 1 2 3 4
2 3 4 2 3 4 1
"""

for _ in range(readint()):
    n,m = readints()
    #if n >= m: # assign each m node a unique colour
    #    print("YES")
    #    ar = list()
    #    for i in range(m):
    #        ar.append(i+1)
    #    for _ in range(2*n):
    #        print(*ar)
    if 2*n > m:
        print("YES")
        #ar = list()
        #for i in range(m):
        #    ar.append(i%n+1)    
        for j in range(n):
            aar = list()
            for k in range(m):
                aar.append((j+k) % n + 1)
            print(*aar)
        #br = list()
        #for l in range(m):
        #    br.append((l//2+k)%n+1)
        for o in range(n):
            bbr = list()
            for p in range(m%n):
                bbr.append((p+o) % n + 1)
            for q in range(m//n*n):
                bbr.append((q+o) % n + 1)
            
            print(*bbr)
        
    else: 
        print("NO")
