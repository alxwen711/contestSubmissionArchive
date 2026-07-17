#start 7:45
import sys

for i in range(int(sys.stdin.readline())):
    w = int(sys.stdin.readline())
    bi = list(map(str,sys.stdin.readline().split()))
    answer = bi[0]
    dup = False
    for j in range(w-3):
        if bi[j][1] == bi[j+1][0]: answer = answer + bi[j+1][1]
        else:
            dup = True
            answer = answer + bi[j+1]
    if not dup: answer += "a"
    print(answer)
