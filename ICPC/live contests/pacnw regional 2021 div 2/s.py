for i in range(int(input())):
    x = str(input())
    inc = True
    digit = 0
    ans = ""
    for j in range(len(x)):
        d = int(x[j])
        if inc:
            if d < digit:
                inc = False
            digit = d
            ans += str(d)
        else:
            if d <= digit:
                digit = d
                ans += str(digit)
            else:
                for k in range(len(x)-j):
                    ans += str(digit)
                break
    print(ans)
