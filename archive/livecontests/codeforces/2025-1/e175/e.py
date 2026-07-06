import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
strings that win for the first player:
00
001
0010010
010
0100100
100
00
001
010
100
00
001

ignoring transposed repeats:
00
001
0010010

assign a "score" in number of extra 0's needed to win
score can be negative if there are enough 0's
then keep track of required score values
0 adds 1 to score
1 could subtract 2 sometimes?
"""

n = readint()
s = readin()
