import sys

def s(ar,n):
    maxsum = 0
    cursum = 0
    streak = 0
    pos = False
    for k in range(n):
        if pos == False:
            if ar[k] > 0: pos = True
        if pos:
            cursum += ar[k]
            if ar[k] < 0: streak = 0
            else: streak += ar[k]
            if streak > cursum: cursum = streak
            if cursum > maxsum: maxsum = cursum
    return maxsum

for i in range(int(sys.stdin.readline())):
    n,x = map(int,sys.stdin.readline().split())
    ar = list(map(int,sys.stdin.readline().split()))
    h = [0]*n
    print(s(ar,n),end=" ")
    pastsum = -999999999
    pastindex = -999999999
    for j in range(n):
        index = 0
        high = -999999999
        for m in range(n):
            if h[m] == 0:
                ar[m] += x
                tmp = s(ar,n)
                if tmp > high:
                    index = m
                    high = tmp
                ar[m] += -x
        if pastsum != -999999999 and pastindex != -999999999 and high == pastsum:
            back = -99999
            front = 99999
            for b in range(pastindex):
                if h[pastindex-b-1] == 0:
                    back = pastindex-b-1
                    break
            for f in range(n-pastindex-1):
                if h[pastindex+f+1] == 0:
                    front = pastindex+f+1
                    break
            if pastindex - back < front - pastindex: index = back
            elif pastindex - back > front - pastindex: index = front
            elif min(ar[back]+x,0) > min(ar[front]+x,0): index = back
            elif min(ar[back]+x,0) < min(ar[front]+x,0): index = front
            else:
                tie = 1
                while True:
                    if back - tie < 0:
                        index = front
                        break
                    elif front + tie >= n:
                        index = back
                        break
                    elif min(ar[back-tie]+x,0) > min(ar[front+tie]+x,0):
                        index = back
                        break
                    elif min(ar[back-tie]+x,0) < min(ar[front+tie]+x,0):
                        index = front
                        break
                    tie += 1
        pastsum = high
        pastindex = index
        print(high,end=" ")
        h[index] = 1
        ar[index] += x
        #print(ar)
    print()
