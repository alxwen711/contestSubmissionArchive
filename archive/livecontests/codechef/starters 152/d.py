import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())
"""
2N/3 1's are possible (101101101101...)
look for chains of 0's?

000 -> 101
001 -> 100
010 -> 010
011 -> 010
100 -> 001
101 -> 000
110 -> 010
111 -> 010


"""
