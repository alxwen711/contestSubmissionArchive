import sys
for i in range(int(sys.stdin.readline())):
    h = int(input())
    x = str(input())
    ans = 0
    first = False
    one = 0
    ar = list()
    for j in range(h):
        if x[j] == "0":
            if not first: first = True
            else:
                ar.append(one)
                if one < 2:
                    ans += (2-one)
            one = 0
        else: one += 1
    #print(ar)
    print(ans)
