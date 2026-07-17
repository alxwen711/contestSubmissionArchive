import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
might be some sort of tree dp from leaf upwards
which ever path is chosen, removing those edges should
result in the remaining path nodes ALL having even degree?

last case solutions are 25,12,13,56,57
"""
