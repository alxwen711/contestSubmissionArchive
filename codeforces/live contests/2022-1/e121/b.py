import sys
for i in range(int(sys.stdin.readline())):
    num = str(sys.stdin.readline())
    digit = len(num)-1
    sdc = False
    for j in range(digit-1):
        if int(num[digit-j-2]) + int(num[digit-j-1]) >= 10:
            sdc = True
            s = str(int(num[digit-j-2]) + int(num[digit-j-1]))
            if j == 0: print(num[:digit-j-2]+s)
            elif j == digit-2: print(s+num[digit-j:])
            else: print(num[:digit-j-2]+s+num[digit-j:])
            break
    if not sdc:
        s = str(int(num[0]) + int(num[1]))
        if digit == 2: print(s)
        else: print(s+num[2:])
