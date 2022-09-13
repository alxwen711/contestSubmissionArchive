import sys

for i in range(int(sys.stdin.readline())):
    sC = int(sys.stdin.readline())
    scenes = list()
    keys = list()
    for j in range(sC):
        x = str(sys.stdin.readline())
        x = x[:-1]
        scenes.append(x)
        keys.append(x[::-1])
    ans = "NO"
    for k in range(sC):
        key = keys[k]
        lk = len(key)
        if lk == 1:
            ans = "YES"
            break
        elif lk == 2:
            e = False
            for m in range(sC-k-1):
                word = scenes[-m-1]
                if len(word) == 1:
                    e = True
                    break
                elif len(word) == 3:
                    if word[1:] == key:
                        e = True
                        break
                elif word == key:
                    e = True
                    break
            if e:
                ans = "YES"
                break
        elif lk == 3:
            e = False
            for m in range(sC-k-1):
                word = scenes[-m-1]
                if len(word) == 1:
                    e = True
                    break
                elif len(word) == 2:
                    if word == key[1:]:
                        e = True
                        break
                elif word == key:
                    e = True
                    break
            if e:
                ans = "YES"
                break
    print(ans)
