import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
ans can never be 0 since both paths will collide
ans is at most 2n-3

both sides are literally simple dp, no need to think
about which tiles need both to be changed for both paths
since this is literally impossible

5am back to back head, oops lmao
"""
