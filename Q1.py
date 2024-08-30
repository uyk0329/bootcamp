from collections import deque
tc = 0

while tc < 3:
    num = 0
    flag = 0
    n = input()
    for x in n:
        if x.isdigit(): num += 1
        elif x == '-': flag = 1
    if n[0].isalpha() or (flag == 0 and num > 20) or (flag == 1 and num > 21):
        print('Error!')
        tc += 1
    d = deque()
    n = ''.join(reversed(n))
    temp = 0
    for x in n:
        if temp == 3:
            d.appendleft(',')
            temp = 0
        else:
            d.appendleft(x)
            temp += 1
    if num % 3 == 0: d.popleft()
    if flag == 1: d.appendleft('-')
    for x in d:
        print(x, end = '')
    print()
