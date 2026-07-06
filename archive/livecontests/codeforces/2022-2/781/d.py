"""
4
1 3 -> 1, 1 < 2 ans = 0
2 6 -> 2, 2 < 4 ans = 00
4 12 -> 8, 8 = 8 ans = 100
4 20 -> 8, 8 < 16, done? (0100)

11
1 3 -> 2 ans = 1
1 5 -> 4 ans = 11
1 9 -> 4 ans = 011
5 21 -> 16 ans = 1011
5 37 -> 16 ans = 01011
21 85 -> 32 ans = 001011
storing bit strings in reverse
"""

def solve():
    a = 1
    ans = ""
    for i in range(30):
        b = a + (2**(i+1))
        print("?",a,b,flush=True)
        res = int(input())
        if res < 2**(i+1):
            ans += "0"
            a += (2**i)
        else: ans += "1"
    s = 0
    for j in range(len(ans)):
        s += (2**j)*int(ans[j])
    return s



for i in range(int(input())):
    x = "! "+str(solve())
    print(x)
