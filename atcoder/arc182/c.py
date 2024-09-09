import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
up to n elements in the list
determine what factor combinations are possible
only 2,3,5,7,11,13 can exist in the setup

1,1,1,1,1,1,1
1,3,10

1 -> 1,1,1,1,1,1,1
2 -> 1,3,6,10,15
3 -> 1,?

up to 16 variables, 1 for each vector used
calculate how many unique vectors in the space
where the coefficients sum at most n

and all coefficients are non negative

16 -> 8 -> 4 -> 2 -> 1
9 -> 3
"""

vectors = [[0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [1,0,0,0,0,0],
           [0,1,0,0,0,0],
           [2,0,0,0,0,0],
           [0,0,1,0,0,0],
           [1,1,0,0,0,0],
           [0,0,0,1,0,0],
           [3,0,0,0,0,0],
           [0,2,0,0,0,0],
           [1,0,1,0,0,0],
           [0,0,0,0,1,0],
           [2,1,0,0,0,0],
           [0,0,0,0,0,1],
           [1,0,0,1,0,0],
           [0,1,1,0,0,0],
           [4,0,0,0,0,0]]

n,m = readints()
