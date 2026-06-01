import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
if everything is 0 this is towers of hanoi
is this actually bfs able?

if the number is not high enough, treat it as an individual hanoi problem??

0 1 1 is treated like 1-1 disks?

0 1 0 0 is treated like 2-1-1 disks
0 1 2 0 is treated like 3-1 disks
0 1 1 0 is treated like two-one disks
0 1 1 1 is treated like 1-1-1 disks?

maybe this is just brute force???
move the lowest one first every time?

greedily moving the disks as far right as possible does not work on 0,0,0,0 case

- construct the initial towers of hanoi solution
- maybe the numbers just let us skip various parts of the recursive iteration?
"""
         

for _ in range(readint()):
    n = readint()
    ar = readar()
    # construct initial hanoi solution
    one = [i+1 for i in range(n)]
    one.reverse()
    two = []
    three = []
    anslist = list()
    mc = 0
    if n % 2 == 0: #AB,AC,BC
        while len(three) != n:
            if mc % 3 == 0:
                if len(two) == 0:
                    anslist.append((one[-1],1,2))
                    two.append(one.pop())
                elif len(one) == 0:
                    anslist.append((two[-1],2,1))
                    one.append(two.pop())
                elif one[-1] < two[0]:
                    anslist.append((one[-1],1,2))
                    two.append(one.pop())
                else:
                    anslist.append((two[-1],2,1))
                    one.append(two.pop())
            elif mc % 3 == 1:
                if len(three) == 0:
                    anslist.append((one[-1],1,3))
                    three.append(one.pop())
                elif len(one) == 0:
                    anslist.append((three[-1],3,1))
                    one.append(three.pop())
                elif one[-1] < three[0]:
                    anslist.append((one[-1],1,3))
                    three.append(one.pop())
                else:
                    anslist.append((three[-1],3,1))
                    one.append(three.pop())
            else:
                if len(three) == 0:
                    anslist.append((two[-1],2,3))
                    three.append(two.pop())
                elif len(two) == 0:
                    anslist.append((three[-1],3,2))
                    two.append(three.pop())
                elif two[-1] < three[0]:
                    anslist.append((two[-1],2,3))
                    three.append(two.pop())
                else:
                    anslist.append((three[-1],3,2))
                    two.append(three.pop())
            
            
            mc += 1        
    else: #AC,AB,BC
        while len(three) != n:
            if mc % 3 == 0:
                if len(three) == 0:
                    anslist.append((one[-1],1,3))
                    three.append(one.pop())
                elif len(one) == 0:
                    anslist.append((three[-1],3,1))
                    one.append(three.pop())
                elif one[-1] < three[0]:
                    anslist.append((one[-1],1,3))
                    three.append(one.pop())
                else:
                    anslist.append((three[-1],3,1))
                    one.append(three.pop())                
            elif mc % 3 == 1:
                if len(two) == 0:
                    anslist.append((one[-1],1,2))
                    two.append(one.pop())
                elif len(one) == 0:
                    anslist.append((two[-1],2,1))
                    one.append(two.pop())
                elif one[-1] < two[0]:
                    anslist.append((one[-1],1,2))
                    two.append(one.pop())
                else:
                    anslist.append((two[-1],2,1))
                    one.append(two.pop())
            else:
                if len(three) == 0:
                    anslist.append((two[-1],2,3))
                    three.append(two.pop())
                elif len(two) == 0:
                    anslist.append((three[-1],3,2))
                    two.append(three.pop())
                elif two[-1] < three[0]:
                    anslist.append((two[-1],2,3))
                    three.append(two.pop())
                else:
                    anslist.append((three[-1],3,2))
                    two.append(three.pop())
            mc += 1        
    
    print("YES")
    print(len(anslist))
    for u in anslist:
        print(u[0],u[1],u[2])
