import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
how to deal with situations where 24-node tree with 22-node child
and 8-node tree with 1-node children can produce 30 (22 | 8)

counter example proves not pure greedy by highest -> lowest node count

i have more of a starting point on g
get min value of s
compute value change of each bit flip
somehow get a combination of bit flips to reach s? (not greedy)

10011

00110
00100
00100
00000
00000

answer:
00001
"""
