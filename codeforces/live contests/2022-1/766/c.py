import sys

for i in range(int(sys.stdin.readline())):
    node = int(sys.stdin.readline())
    edges = list()
    for j in range(node-1):
        a,b = map(int, sys.stdin.readline().split())
        x = [0]
        if a < b: x.extend([a,b,j])
        else: x.extend([b,a,j])
        edges.append(x)
    edges.sort(key = lambda t: t[1])
    #nodes = 1+2, id = 3, order = 0
    edges[0][0], front, back, start, end, chain, new = 2, edges[0][1], edges[0][2], 2, 2, 1, True

    while new:
        new = False
        for k in range(node-2):
            if edges[k+1][0] == 0:
                if edges[k+1][1] == front: #add [3] to front
                    start = ((start+1)%2)+2
                    edges[k+1][0], front, new = start, edges[k+1][2], True
                    chain += 1
                elif edges[k+1][2] == front: #add [2] to front
                    start = ((start+1)%2)+2
                    edges[k+1][0], front, new = start, edges[k+1][1], True
                    chain += 1
                elif edges[k+1][1] == back: #add [3] to back
                    end = ((end+1)%2)+2
                    edges[k+1][0], back, new = end, edges[k+1][2], True
                    chain += 1
                elif edges[k+1][2] == back: #add [2] to back
                    end = ((end+1)%2)+2
                    edges[k+1][0], back, new = end, edges[k+1][1], True
                    chain += 1
            

    if chain != node-1: print(-1)
    else:
        edges.sort(key = lambda t: t[3])
        for m in range(node-1):
            print(str(edges[m][0])+" ",end="")
        print()
