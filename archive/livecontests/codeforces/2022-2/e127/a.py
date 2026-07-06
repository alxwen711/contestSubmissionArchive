import sys
for i in range(int(sys.stdin.readline())):
    s = input()
    ac = 0
    bc = 0
    ans = "YES"
    for j in range(len(s)):
        if s[j] == "a":
            ac += 1
            if ac == 1:
                if bc == 1:
                    ans = "NO"
                    break
            bc = 0
        else:
            bc += 1
            if bc == 1:
                if ac == 1:
                    ans = "NO"
                    break
            ac = 0
    if ac == 1 or bc == 1: ans = "NO"
    print(ans)
                        
    
