#JLSJIOT

def check(a):
    if a.count('J') > 1 or a.count('L') > 1 or a.count('S') > 1 or a.count('Z') > 1 or a.count('T') > 1 or a.count('O') > 1 or a.count('I') > 1: 
        return False
    return True

for i in range(int(input())):
    x = str(input())
    seq = len(x)
    possible = 0
    for i in range(min(seq,7)):
        if check(x[:i]): #first bag clear, check remaining
            index = i
            while index < seq:
                if check(x[index:(index+7)]):
                    index += 7
                else: break
            if index >= seq:
                possible = 1
                break
    print(possible)
