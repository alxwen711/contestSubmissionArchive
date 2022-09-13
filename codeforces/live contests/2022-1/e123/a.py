import sys

for i in range(int(sys.stdin.readline())):
    ar = [0]*6
    s = str(input())
    ans = "YES"
    for j in range(len(s)):
        if s[j] == "r":
            ar[0] += 1
        if s[j] == "g":
            ar[1] += 1
        if s[j] == "b":
            ar[2] += 1
        if s[j] == "R":
            ar[3] += 1
        if s[j] == "G":
            ar[4] += 1
        if s[j] == "B":
            ar[5] += 1
        if ar[3] > ar[0]:
            ans = "NO"
            break
        if ar[4] > ar[1]:
            ans = "NO"
            break
        if ar[5] > ar[2]:
            ans = "NO"
            break
    print(ans)
        
