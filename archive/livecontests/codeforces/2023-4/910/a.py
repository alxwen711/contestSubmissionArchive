import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for _ in range(readint()):
    n,k = readints()
    s = input()
    b = s.count('B')
    if b == k: print(0)
    else:
        print(1)
        if b > k:
            diff = b-k
            for i in range(n):
                if s[i] == "B": diff -= 1
                if diff == 0:
                    print(i+1,"A")
                    break
        else:
            diff = k-b
            for j in range(n):
                if s[j] == "A": diff -= 1
                if diff == 0:
                    print(j+1,"B")
                    break
            
            
