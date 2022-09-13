import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n,k = readints()

"""
k = 1
1 1 2 2 3 4 5 6 7 10 12 15 
1 1 1 1 1 1 1 1 1 1  1  1
0 0 1 1 2 2 3 3 4 4  5  5
0 0 0 0 0 1 1 2 3 4  5  7
0 0 0 0 0 0 0 0 0 1  1  2

k = 2
0 1 0 1 1 1 1 2 2 2
0 1 0 1 0 1 0 1 0 1
0 0 0 0 1 0 1 1 1 1
0 0 0 0 0 0 0 0 1 0


9
1 9
3 9
5 9
7 9
1 3 9
2 6 9
4 6 9

"""
