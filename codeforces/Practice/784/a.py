import sys
for i in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    if a >= 1900: print("Division 1")
    elif a >= 1600: print("Division 2")
    elif a >= 1400: print("Division 3")
    else: print("Division 4")
