import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
90% this is cycle detection
every node is going to eventually cycle to an endpoint
if it cycles to an endpoint, track either:
the position in the track
or where in the cycle it is
so each value either gets pushed into the cycle
or not far enough and a ref table of some sort is needed

new additions are either a new path or link to an existing one

cycles can have MULTIPLE entry points (2,3,4,5,3,4)

paths and cycles would need to be tracked differently, somehow
"""

class Node:
    def __init__(self):
        self.path = -1 # path id
        self.pos = -1 # position in path

paths = list()
cyclestarts = list()

n,k = readints()
ar = readar()
br = readar()
