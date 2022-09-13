import sys
for i in range(int(sys.stdin.readline())):
    mCount = int(sys.stdin.readline())
    time = list(map(int, sys.stdin.readline().split()))
    damage = list(map(int, sys.stdin.readline().split()))
    combine = list()
    for j in range(mCount):
        x = list()
        x.append(time[mCount-j-1])
        x.append(damage[mCount-j-1])
        combine.append(x)
    ans = int(combine[0][1]*(combine[0][1]+1)/2)
    strength = combine[0][1]
    minStrength = combine[0][1]
    t = combine[0][0]
    for k in range(mCount-1):
        nT = combine[k+1][0]
        timeDiff = t - nT
        if strength - timeDiff < combine[k+1][1]: #add new spell/strengthen spell
            newCost = int(combine[k+1][1]*(combine[k+1][1]+1)/2)
            incSize = combine[k+1][1]-strength+timeDiff
            incCost = int(incSize*(incSize+1)/2+incSize*strength)
            if newCost < incCost and timeDiff >= minStrength: #adding new spell
                #ans += -int(strength*(strength+1)/2)
                #ans += int(minStrength*(minStrength+1)/2)
                ans += newCost
                strength = combine[k+1][1]
                t = combine[k+1][0]
                minStrength = combine[k+1][1]
            else:
                ans += incCost
                strength += incSize
    print(ans)
        
        
